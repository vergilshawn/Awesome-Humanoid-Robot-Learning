"""Multi-label classification of papers into humanoid robotics categories."""

import logging
import sys
import yaml
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent))
from paper_model import Paper

logger = logging.getLogger(__name__)

SCRIPTS_DIR = Path(__file__).parent
CONFIG_PATH = SCRIPTS_DIR / "config.yaml"


def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def classify_paper(paper: Paper, config: dict) -> list[str]:
    """Classify a single paper into one or more categories."""
    text = (paper.title + " " + paper.abstract).lower()
    matched = []

    for cat in config["categories"]:
        cat_score = 0
        for keyword in cat["keywords"]:
            if keyword.lower() in text:
                cat_score += 1
        if cat_score >= 1:
            matched.append(cat["name"])

    # If no category matched, assign to most general based on content
    if not matched:
        if any(k in text for k in ["humanoid", "biped", "walk"]):
            matched.append("Locomotion")
        elif any(k in text for k in ["manipulation", "grasp", "dexterous"]):
            matched.append("Manipulation")
        else:
            matched.append("Loco-Manipulation and Whole-Body Control")

    return matched


def tag_paper(paper: Paper, config: dict) -> list[str]:
    """Assign keyword tags by matching configured tags in the title and abstract."""
    text = (paper.title + " " + paper.abstract).lower()
    tags = []

    for tag in config.get("tags", []):
        if tag.lower() in text:
            tags.append(tag)

    for category in paper.categories:
        if category not in tags:
            tags.append(category)

    return tags


def classify_papers(papers: list[Paper], config: Optional[dict] = None) -> list[Paper]:
    """Add category labels to all papers."""
    if config is None:
        config = load_config()

    for paper in papers:
        paper.categories = classify_paper(paper, config)
        paper.primary_category = paper.categories[0] if paper.categories else "Locomotion"
        paper.tags = tag_paper(paper, config)
        logger.debug(f"  {paper.title[:60]}... -> {paper.categories}")

    logger.info(f"Classified {len(papers)} papers")
    return papers


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    from fetch_arxiv import load_existing_papers
    papers = list(load_existing_papers().values())
    papers = classify_papers(papers)
    for p in papers:
        print(f"  {p.categories} | {p.title[:70]}")
