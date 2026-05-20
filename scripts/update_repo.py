#!/usr/bin/env python3
"""Main orchestration script for the humanoid robot learning paper pipeline.

Usage:
    python scripts/update_repo.py           # Run full pipeline
    python scripts/update_repo.py --fetch   # Force fetch new papers from arXiv
    python scripts/update_repo.py --dry-run # Dry run without saving
"""

import argparse
import json
import logging
import sys
from pathlib import Path
from datetime import date

import yaml

sys.path.insert(0, str(Path(__file__).parent))

from fetch_arxiv import fetch_papers, load_existing_papers, save_papers
from semantic_filter import filter_papers
from classify_papers import classify_papers
from detect_project_links import detect_project_links
from detect_real_robot import detect_real_robot
from generate_markdown import generate_all as generate_all_markdown
from generate_vitepress import generate_all as generate_all_vitepress
from paper_model import Paper

logger = logging.getLogger(__name__)

SCRIPTS_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPTS_DIR.parent
CONFIG_PATH = SCRIPTS_DIR / "config.yaml"
DATA_DIR = PROJECT_ROOT / "data"


def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def merge_papers(existing: dict[str, Paper], new_papers: list[Paper]) -> list[Paper]:
    """Merge new papers with existing ones, preserving metadata from existing."""
    merged = {}

    # Keep existing papers with all metadata
    for arxiv_id, paper in existing.items():
        merged[arxiv_id] = paper

    # Add/update with new papers
    for paper in new_papers:
        if paper.arxiv_id in merged:
            # Preserve existing classification/annotations
            existing_paper = merged[paper.arxiv_id]
            # Update abstract if new one is longer (sometimes placeholder)
            if len(paper.abstract) > len(existing_paper.abstract):
                existing_paper.abstract = paper.abstract
            merged[paper.arxiv_id] = existing_paper
        else:
            merged[paper.arxiv_id] = paper

    return sorted(merged.values(), key=lambda p: p.published_date or date.min, reverse=True)


def run_pipeline(
    fetch_new: bool = False,
    dry_run: bool = False,
    skip_detection: bool = False,
) -> list[Paper]:
    """Run the full paper processing pipeline.

    Args:
        fetch_new: If True, fetch new papers from arXiv even if existing data exists.
        dry_run: If True, don't save any data.
    """
    config = load_config()
    logger.info("=" * 60)
    logger.info("Awesome-Humanoid-Robot-Learning Pipeline")
    logger.info("=" * 60)

    # Step 1: Load or fetch papers
    existing = load_existing_papers()
    logger.info(f"Loaded {len(existing)} existing papers from data/papers.json")

    if fetch_new or not existing:
        logger.info("Fetching new papers from arXiv...")
        new_papers = fetch_papers(config)
        logger.info(f"Fetched {len(new_papers)} papers from arXiv")

        # Step 2: Merge with existing
        all_papers = merge_papers(existing, new_papers)
        logger.info(f"Merged: {len(all_papers)} total papers")
    else:
        all_papers = list(existing.values())
        logger.info("Using existing papers (use --fetch to force refresh)")

    # Step 3: Semantic filtering
    logger.info("Filtering papers for humanoid relevance...")
    relevant = filter_papers(all_papers, config)
    logger.info(f"Filtered: {len(relevant)} relevant papers (from {len(all_papers)})")

    # Step 4: Classify
    logger.info("Classifying papers...")
    relevant = classify_papers(relevant, config)

    # Step 5/6: Detect project links and real robot experiments
    if skip_detection:
        logger.info("Skipping project-link and real-robot detection")
    else:
        logger.info("Detecting open-source project links...")
        relevant = detect_project_links(relevant, config)

        logger.info("Detecting real robot experiments...")
        relevant = detect_real_robot(relevant, config)

    if dry_run:
        logger.info("DRY RUN — skipping save/generation")
        for p in relevant[:20]:
            print(f"  {p.published} | {p.primary_category} | {'🌟' if p.open_source else ' '} | {'🤖' if p.real_robot else ' '} | {p.title[:80]}")
        return relevant

    # Step 7: Save metadata
    logger.info("Saving metadata...")
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    save_papers(relevant)

    # Save tags and categories summaries
    tags_data = {}
    for p in relevant:
        for t in p.tags:
            tags_data[t] = tags_data.get(t, 0) + 1
    with open(DATA_DIR / "tags.json", "w") as f:
        json.dump(dict(sorted(tags_data.items(), key=lambda x: x[1], reverse=True)), f, indent=2)

    cat_data = {}
    for p in relevant:
        cat_data[p.primary_category] = cat_data.get(p.primary_category, 0) + 1
    with open(DATA_DIR / "categories.json", "w") as f:
        json.dump(dict(sorted(cat_data.items(), key=lambda x: x[1], reverse=True)), f, indent=2)

    # Step 8: Generate markdown
    logger.info("Generating markdown pages...")
    generate_all_markdown(relevant)

    # Step 9: Generate VitePress config
    logger.info("Generating VitePress configuration...")
    generate_all_vitepress(relevant)

    logger.info("=" * 60)
    logger.info("Pipeline complete!")
    logger.info(f"  Total papers: {len(relevant)}")
    logger.info(f"  Real robot: {sum(1 for p in relevant if p.real_robot)}")
    logger.info(f"  Open source: {sum(1 for p in relevant if p.open_source)}")
    logger.info("=" * 60)

    return relevant


def main():
    parser = argparse.ArgumentParser(description="Update the humanoid robot learning paper portal")
    parser.add_argument("--fetch", action="store_true", help="Force fetch new papers from arXiv")
    parser.add_argument("--dry-run", action="store_true", help="Dry run without saving")
    parser.add_argument(
        "--skip-detection",
        action="store_true",
        help="Skip network-based project-link and real-robot detection",
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    try:
        run_pipeline(fetch_new=args.fetch, dry_run=args.dry_run, skip_detection=args.skip_detection)
    except Exception as e:
        logger.exception(f"Pipeline failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
