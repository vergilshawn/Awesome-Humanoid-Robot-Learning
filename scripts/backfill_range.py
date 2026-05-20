#!/usr/bin/env python3
"""Backfill a historical date range with additive arXiv searches."""

import argparse
import copy
import logging
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from classify_papers import classify_papers
from fetch_arxiv import fetch_papers, load_existing_papers, save_papers
from generate_markdown import generate_all as generate_all_markdown
from generate_vitepress import generate_all as generate_all_vitepress
from paper_model import Paper
from semantic_filter import filter_papers
from update_current_month import save_summary_files
from update_repo import DATA_DIR, load_config

logger = logging.getLogger(__name__)

BACKFILL_QUERIES = [
    'all:"humanoid robot"',
    'all:"humanoid"',
    'all:"humanoid locomotion"',
    'all:"bipedal robot"',
    'all:"bipedal locomotion"',
    'all:"whole-body control"',
    'all:"whole body control"',
    'all:"loco-manipulation"',
    'all:"legged locomotion"',
    'all:"ground reaction force"',
    'all:"robot control"',
]


def parse_day(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def merge_papers(existing: dict[str, Paper], new_papers: list[Paper]) -> list[Paper]:
    added = 0
    for paper in new_papers:
        current = existing.get(paper.arxiv_id)
        if current:
            if not current.abstract and paper.abstract:
                existing[paper.arxiv_id] = paper
            continue
        existing[paper.arxiv_id] = paper
        added += 1

    logger.info(f"Added {added} new paper(s)")
    return sorted(existing.values(), key=lambda p: p.published_date or date.min, reverse=True)


def run_backfill(
    start: date,
    end: date,
    max_results: int,
    request_delay: float,
    dry_run: bool,
) -> list[Paper]:
    config = copy.deepcopy(load_config())
    config["arxiv"]["categories"] = []
    config["arxiv"]["topic_queries"] = BACKFILL_QUERIES
    config["arxiv"]["date_from"] = start.isoformat()
    config["arxiv"]["date_to"] = end.isoformat()
    config["arxiv"]["max_results_per_category"] = max_results
    config["arxiv"]["request_delay"] = request_delay
    config["arxiv"]["fail_on_category_error"] = False

    logger.info("=" * 60)
    logger.info(f"Backfilling {start.isoformat()} <= submitted < {end.isoformat()}")
    logger.info("=" * 60)

    existing = load_existing_papers()
    fetched = fetch_papers(config)
    relevant = filter_papers(fetched, config)
    relevant = classify_papers(relevant, config)
    merged = merge_papers(existing, relevant)

    if dry_run:
        logger.info("DRY RUN - skipping save/generation")
        for paper in relevant:
            print(f"  {paper.published_date} | {paper.primary_category} | {paper.arxiv_id} | {paper.title[:90]}")
        return merged

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    save_papers(merged)
    save_summary_files(merged)
    generate_all_markdown(merged)
    generate_all_vitepress(merged)
    logger.info(f"Backfill complete: {len(merged)} total papers")
    return merged


def main() -> None:
    parser = argparse.ArgumentParser(description="Additive arXiv backfill for a historical date range")
    parser.add_argument("--start", required=True, help="Start day, YYYY-MM-DD, inclusive")
    parser.add_argument("--end", required=True, help="End day, YYYY-MM-DD, exclusive")
    parser.add_argument("--max-results", type=int, default=100)
    parser.add_argument("--request-delay", type=float, default=10.0)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    run_backfill(
        start=parse_day(args.start),
        end=parse_day(args.end),
        max_results=args.max_results,
        request_delay=args.request_delay,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
