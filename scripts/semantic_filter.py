"""Filter papers for relevance to humanoid robot learning using keyword scoring."""

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


def compute_relevance_score(title: str, abstract: str, config: dict) -> tuple[float, list[str]]:
    """Compute relevance score and return matched high-priority keywords."""
    text = (title + " " + abstract).lower()
    relevance = config["relevance_keywords"]

    # Exclusion check first - auto reject
    for keyword in relevance["exclude"]:
        if keyword.lower() in text:
            logger.debug(f"  Rejected by exclusion keyword: {keyword}")
            return -10.0, []

    score = 0.0
    matched_high = []

    # High priority keywords (each match adds significant score)
    for keyword in relevance["high_priority"]:
        if keyword.lower() in text:
            matched_high.append(keyword)
            score += 5.0

    # Must have at least one high-priority keyword
    if not matched_high:
        return 0.0, []

    # Medium priority keywords (boost score)
    for keyword in relevance["medium_priority"]:
        if keyword.lower() in text:
            score += 1.5

    return score, matched_high


def filter_papers(papers: list[Paper], config: Optional[dict] = None) -> list[Paper]:
    """Filter papers by relevance to humanoid robotics. Returns relevant papers."""
    if config is None:
        config = load_config()

    threshold = 4.0  # Must have at least one high-priority keyword
    relevant = []

    for paper in papers:
        if not paper.abstract and paper.categories:
            logger.info(f"  KEEP [curated] {paper.title[:80]}...")
            relevant.append(paper)
            continue

        score, matched = compute_relevance_score(paper.title, paper.abstract, config)
        if score >= threshold:
            logger.info(f"  KEEP [{score:.1f}] {paper.title[:80]}... (matched: {matched})")
            relevant.append(paper)
        else:
            logger.debug(f"  DROP [{score:.1f}] {paper.title[:80]}...")

    logger.info(f"Filtered {len(papers)} -> {len(relevant)} relevant papers")
    return relevant


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    from fetch_arxiv import load_existing_papers
    papers = list(load_existing_papers().values())
    relevant = filter_papers(papers)
    for p in relevant:
        print(f"  [{p.published}] {p.title}")
