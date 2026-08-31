"""Filter papers for relevance to humanoid robot learning using keyword scoring."""

import logging
import json
import sys
import yaml
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent))
from paper_model import Paper

logger = logging.getLogger(__name__)

SCRIPTS_DIR = Path(__file__).parent
CONFIG_PATH = SCRIPTS_DIR / "config.yaml"
CURATION_PATH = SCRIPTS_DIR.parent / "data" / "curation.json"


def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def load_curation() -> dict:
    """Load human-reviewed inclusion/exclusion overrides."""
    if not CURATION_PATH.exists():
        return {"exclude": {}}
    with open(CURATION_PATH) as f:
        return json.load(f)


def _has_humanoid_robot_context(title: str, abstract: str, config: dict) -> bool:
    """Require evidence that the work studies humanoid/biped robot technology.

    Mere mentions of "human-like" or a humanoid baseline are insufficient.  Title
    evidence is intentionally weighted most heavily because broad arXiv abstracts
    frequently mention humanoids only as a possible application.
    """
    title_text = title.lower()
    text = f"{title} {abstract}".lower()
    title_patterns = config["relevance_keywords"].get("title_required", [])
    platform_patterns = config["relevance_keywords"].get("platform_context", [])

    if any(pattern.lower() in title_text for pattern in title_patterns):
        return True

    # A named humanoid platform is also strong evidence, even when an acronymic
    # title omits the word "humanoid" (common for systems papers).
    return any(pattern.lower() in text for pattern in platform_patterns)


def compute_relevance_score(
    title: str, abstract: str, config: dict, *, require_context: bool = True
) -> tuple[float, list[str]]:
    """Compute relevance score and return matched high-priority keywords."""
    text = (title + " " + abstract).lower()
    relevance = config["relevance_keywords"]

    if require_context and not _has_humanoid_robot_context(title, abstract, config):
        return 0.0, []

    # Exclusion check after establishing context. These describe work that is
    # robotic but outside this collection's humanoid-learning scope.
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
    excluded_ids = load_curation().get("exclude", {})
    strict_from = config["relevance_keywords"].get("strict_filter_from", "9999-12-31")

    for paper in papers:
        if paper.arxiv_id in excluded_ids:
            logger.info(
                "  DROP [curated: %s] %s...",
                excluded_ids[paper.arxiv_id],
                paper.title[:80],
            )
            continue
        if not paper.abstract and paper.categories:
            logger.info(f"  KEEP [curated] {paper.title[:80]}...")
            relevant.append(paper)
            continue

        published_date = str(paper.published_date or f"{paper.published}-01")
        score, matched = compute_relevance_score(
            paper.title,
            paper.abstract,
            config,
            require_context=published_date >= strict_from,
        )
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
