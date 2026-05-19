#!/usr/bin/env python3
"""Update only the current month's papers.

This script narrows the arXiv query to the selected month and replaces only
that month in data/papers.json. Older months are kept as-is.
"""

import argparse
import copy
import json
import logging
import sys
from datetime import date
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
from update_repo import DATA_DIR, load_config

logger = logging.getLogger(__name__)


def parse_month(month: str) -> date:
    year_str, month_str = month.split("-", maxsplit=1)
    return date(int(year_str), int(month_str), 1)


def next_month(day: date) -> date:
    if day.month == 12:
        return date(day.year + 1, 1, 1)
    return date(day.year, day.month + 1, 1)


def month_key(day: date) -> str:
    return day.strftime("%Y-%m")


def replace_month(existing: dict[str, Paper], new_papers: list[Paper], month: str) -> list[Paper]:
    kept = [paper for paper in existing.values() if paper.published != month]
    merged = {paper.arxiv_id: paper for paper in kept}
    for paper in new_papers:
        merged[paper.arxiv_id] = paper
    return sorted(merged.values(), key=lambda p: p.published_date or date.min, reverse=True)


def save_summary_files(papers: list[Paper]) -> None:
    tags_data = {}
    for paper in papers:
        for tag in paper.tags:
            tags_data[tag] = tags_data.get(tag, 0) + 1
    with open(DATA_DIR / "tags.json", "w") as f:
        json.dump(dict(sorted(tags_data.items(), key=lambda x: x[1], reverse=True)), f, indent=2)

    cat_data = {}
    for paper in papers:
        cat_data[paper.primary_category] = cat_data.get(paper.primary_category, 0) + 1
    with open(DATA_DIR / "categories.json", "w") as f:
        json.dump(dict(sorted(cat_data.items(), key=lambda x: x[1], reverse=True)), f, indent=2)


def run_current_month_update(
    month: str | None = None,
    max_results: int | None = None,
    request_delay: float = 8.0,
    dry_run: bool = False,
) -> list[Paper]:
    config = copy.deepcopy(load_config())

    start = parse_month(month) if month else date.today().replace(day=1)
    end = next_month(start)
    selected_month = month_key(start)

    config["arxiv"]["date_from"] = start.isoformat()
    config["arxiv"]["date_to"] = end.isoformat()
    config["arxiv"]["request_delay"] = request_delay
    config["arxiv"]["fail_on_category_error"] = True
    if max_results is not None:
        config["arxiv"]["max_results_per_category"] = max_results

    logger.info("=" * 60)
    logger.info(f"Updating arXiv papers for {selected_month} only")
    logger.info(f"Date range: {start.isoformat()} <= submitted < {end.isoformat()}")
    logger.info("=" * 60)

    existing = load_existing_papers()
    logger.info(f"Loaded {len(existing)} existing papers from data/papers.json")

    fetched = fetch_papers(config)
    logger.info(f"Fetched {len(fetched)} candidate papers from arXiv")

    relevant = filter_papers(fetched, config)
    logger.info(f"Filtered: {len(relevant)} relevant papers from {len(fetched)} candidates")

    relevant = classify_papers(relevant, config)
    relevant = detect_project_links(relevant, config)
    relevant = detect_real_robot(relevant, config)

    merged = replace_month(existing, relevant, selected_month)
    logger.info(f"Replacing {selected_month}: {len(relevant)} papers; total after merge: {len(merged)}")

    if dry_run:
        logger.info("DRY RUN - skipping save/generation")
        for paper in relevant:
            print(f"  {paper.published} | {paper.primary_category} | {paper.title[:90]}")
        return merged

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    save_papers(merged)
    save_summary_files(merged)
    generate_all_markdown(merged)
    generate_all_vitepress(merged)

    logger.info("=" * 60)
    logger.info("Current-month update complete")
    logger.info(f"  Updated month: {selected_month}")
    logger.info(f"  Month papers: {len(relevant)}")
    logger.info(f"  Total papers: {len(merged)}")
    logger.info("=" * 60)
    return merged


def main() -> None:
    parser = argparse.ArgumentParser(description="Update only the current month's arXiv papers")
    parser.add_argument("--month", help="Month to update in YYYY-MM format. Defaults to current month.")
    parser.add_argument("--max-results", type=int, help="Override max arXiv results per category.")
    parser.add_argument("--request-delay", type=float, default=8.0, help="Delay between arXiv category requests.")
    parser.add_argument("--dry-run", action="store_true", help="Fetch and process without saving files.")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    try:
        run_current_month_update(
            month=args.month,
            max_results=args.max_results,
            request_delay=args.request_delay,
            dry_run=args.dry_run,
        )
    except Exception as exc:
        logger.exception(f"Current-month update failed: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
