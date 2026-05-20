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


def score_categories(paper: Paper, config: dict) -> list[tuple[str, int]]:
    """Score category matches for a paper."""
    text = (paper.title + " " + paper.abstract).lower()
    scored = []

    for cat in config["categories"]:
        cat_score = 0
        for keyword in cat["keywords"]:
            if keyword.lower() in text:
                cat_score += 1
        if cat_score >= 1:
            scored.append((cat["name"], cat_score))

    return sorted(scored, key=lambda item: item[1], reverse=True)


def classify_paper(paper: Paper, config: dict) -> list[str]:
    """Classify a single paper into one or more categories."""
    text = (paper.title + " " + paper.abstract).lower()
    scored = score_categories(paper, config)
    matched = [name for name, _score in scored]

    # If no category matched, assign to most general based on content
    if not matched:
        if any(k in text for k in ["humanoid", "biped", "walk"]):
            matched.append("Locomotion")
        elif any(k in text for k in ["manipulation", "grasp", "dexterous"]):
            matched.append("Manipulation")
        else:
            matched.append("Loco-Manipulation and Whole-Body Control")

    return matched


def choose_primary_category(paper: Paper, config: dict) -> str:
    """Choose the single best category used for directory placement."""
    scored = score_categories(paper, config)
    if scored:
        return scored[0][0]

    text = (paper.title + " " + paper.abstract).lower()
    if any(k in text for k in ["humanoid", "biped", "walk"]):
        return "Locomotion"
    if any(k in text for k in ["manipulation", "grasp", "dexterous"]):
        return "Manipulation"
    return "Loco-Manipulation and Whole-Body Control"


def tag_paper(paper: Paper, config: dict) -> list[str]:
    """Assign keyword tags by matching configured tags in the title and abstract."""
    text = (paper.title + " " + paper.abstract).lower()
    tags = []

    for tag in config.get("tags", []):
        if tag.lower() in text and tag not in tags:
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
        if not paper.abstract and paper.categories:
            paper.primary_category = paper.primary_category or paper.categories[0]
        else:
            paper.categories = classify_paper(paper, config)
            paper.primary_category = choose_primary_category(paper, config)
        paper.tags = tag_paper(paper, config)
        logger.debug(f"  {paper.title[:60]}... -> {paper.primary_category} ({paper.categories})")

    logger.info(f"Classified {len(papers)} papers")
    return papers


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    from fetch_arxiv import load_existing_papers
    papers = list(load_existing_papers().values())
    papers = classify_papers(papers)
    for p in papers:
        print(f"  {p.categories} | {p.title[:70]}")
