#!/usr/bin/env python3
"""Update papers by daily arXiv windows.

Daily windows reduce arXiv result truncation and make API requests less likely
to hit rate limits than broad month-long searches.
"""

import argparse
import copy
import logging
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from classify_papers import classify_papers
from detect_project_links import detect_project_links
from detect_real_robot import detect_real_robot
from fetch_arxiv import fetch_papers, load_existing_papers, save_papers
from generate_markdown import generate_all as generate_all_markdown
from generate_vitepress import generate_all as generate_all_vitepress
from paper_model import Paper
from semantic_filter import filter_papers
from update_current_month import save_summary_files
from update_repo import DATA_DIR, load_config

logger = logging.getLogger(__name__)


def parse_day(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def day_range(start: date, end: date) -> list[date]:
    days = []
    current = start
    while current <= end:
        days.append(current)
        current += timedelta(days=1)
    return days


def replace_days(existing: dict[str, Paper], new_papers: list[Paper], days: set[date]) -> list[Paper]:
    kept = [
        paper for paper in existing.values()
        if not paper.published_date or paper.published_date not in days
    ]
    merged = {paper.arxiv_id: paper for paper in kept}
    for paper in new_papers:
        merged[paper.arxiv_id] = paper
    return sorted(merged.values(), key=lambda p: p.published_date or date.min, reverse=True)


def merge_papers(existing: dict[str, Paper], new_papers: list[Paper]) -> list[Paper]:
    merged = dict(existing)
    for paper in new_papers:
        current = merged.get(paper.arxiv_id)
        if current:
            if not current.abstract and paper.abstract:
                merged[paper.arxiv_id] = paper
            elif not current.project_url and paper.project_url:
                current.project_url = paper.project_url
                current.open_source = True
            continue
        merged[paper.arxiv_id] = paper
    return sorted(merged.values(), key=lambda p: p.published_date or date.min, reverse=True)


def fetch_one_day(config: dict, day: date) -> list[Paper]:
    day_config = copy.deepcopy(config)
    day_config["arxiv"]["date_from"] = day.isoformat()
    day_config["arxiv"]["date_to"] = (day + timedelta(days=1)).isoformat()
    logger.info(f"Fetching {day.isoformat()}...")
    return fetch_papers(day_config)


def run_daily_update(
    start: date,
    end: date,
    max_results: int | None = None,
    request_delay: float = 8.0,
    merge_only: bool = False,
    skip_detection: bool = False,
    dry_run: bool = False,
) -> list[Paper]:
    config = copy.deepcopy(load_config())
    config["arxiv"]["request_delay"] = request_delay
    config["arxiv"]["fail_on_category_error"] = False
    if max_results is not None:
        config["arxiv"]["max_results_per_category"] = max_results

    days = day_range(start, end)
    logger.info("=" * 60)
    logger.info(f"Updating {len(days)} daily arXiv window(s): {start} to {end}")
    logger.info("=" * 60)

    existing = load_existing_papers()
    logger.info(f"Loaded {len(existing)} existing papers from data/papers.json")

    candidates_by_id: dict[str, Paper] = {}
    successful_days: set[date] = set()
    failed_days: list[date] = []
    for day in days:
        try:
            day_papers = fetch_one_day(config, day)
        except Exception as exc:
            failed_days.append(day)
            logger.warning(f"Skipping {day.isoformat()} because every arXiv query failed: {exc}")
            continue

        successful_days.add(day)
        for paper in day_papers:
            candidates_by_id[paper.arxiv_id] = paper

    if not successful_days:
        logger.warning("No daily arXiv windows could be fetched successfully; keeping existing data unchanged")
        if dry_run:
            return sorted(existing.values(), key=lambda p: p.published_date or date.min, reverse=True)

        merged = sorted(existing.values(), key=lambda p: p.published_date or date.min, reverse=True)
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        save_papers(merged)
        save_summary_files(merged)
        generate_all_markdown(merged)
        generate_all_vitepress(merged)
        return merged
    if failed_days:
        failed = ", ".join(day.isoformat() for day in failed_days)
        logger.warning(f"Kept existing papers for failed day(s): {failed}")

    candidates = sorted(
        candidates_by_id.values(),
        key=lambda p: p.published_date or date.min,
        reverse=True,
    )
    logger.info(f"Fetched {len(candidates)} unique candidate papers")

    relevant = filter_papers(candidates, config)
    relevant = classify_papers(relevant, config)
    if skip_detection:
        logger.info("Skipping project-link and real-robot detection")
    else:
        relevant = detect_project_links(relevant, config)
        relevant = detect_real_robot(relevant, config)

    merged = merge_papers(existing, relevant) if merge_only else replace_days(existing, relevant, successful_days)
    mode = "Merging" if merge_only else "Replacing"
    logger.info(
        f"{mode} {len(successful_days)} fetched day(s): "
        f"{len(relevant)} papers; total after merge: {len(merged)}"
    )

    if dry_run:
        logger.info("DRY RUN - skipping save/generation")
        for paper in relevant:
            print(f"  {paper.published_date} | {paper.primary_category} | {paper.title[:90]}")
        return merged

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    save_papers(merged)
    save_summary_files(merged)
    generate_all_markdown(merged)
    generate_all_vitepress(merged)

    logger.info("=" * 60)
    logger.info("Daily update complete")
    logger.info(f"  Range: {start} to {end}")
    logger.info(f"  Fetched days: {len(successful_days)}")
    logger.info(f"  Failed days kept unchanged: {len(failed_days)}")
    logger.info(f"  Updated papers: {len(relevant)}")
    logger.info(f"  Total papers: {len(merged)}")
    logger.info("=" * 60)
    return merged


def main() -> None:
    parser = argparse.ArgumentParser(description="Update papers with daily arXiv windows")
    parser.add_argument("--date", help="Single day to update, YYYY-MM-DD. Defaults to today.")
    parser.add_argument("--start", help="Start day, YYYY-MM-DD.")
    parser.add_argument("--end", help="End day, YYYY-MM-DD.")
    parser.add_argument("--days", type=int, help="Update the most recent N days ending today.")
    parser.add_argument("--max-results", type=int, help="Override max arXiv results per query.")
    parser.add_argument("--request-delay", type=float, default=8.0, help="Delay between arXiv requests.")
    parser.add_argument("--merge-only", action="store_true", help="Add/update fetched papers without deleting existing papers in the range.")
    parser.add_argument("--skip-detection", action="store_true", help="Skip network-based project-link and real-robot detection.")
    parser.add_argument("--dry-run", action="store_true", help="Fetch and process without saving files.")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    if args.start or args.end:
        if not args.start or not args.end:
            parser.error("--start and --end must be used together")
        start = parse_day(args.start)
        end = parse_day(args.end)
    elif args.days:
        end = date.today()
        start = end - timedelta(days=args.days - 1)
    else:
        start = end = parse_day(args.date) if args.date else date.today()

    if start > end:
        parser.error("start date must be before or equal to end date")

    try:
        run_daily_update(
            start=start,
            end=end,
            max_results=args.max_results,
            request_delay=args.request_delay,
            merge_only=args.merge_only,
            skip_detection=args.skip_detection,
            dry_run=args.dry_run,
        )
    except Exception as exc:
        logger.exception(f"Daily update failed: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
