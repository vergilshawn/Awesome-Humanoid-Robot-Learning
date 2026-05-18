"""Detect whether papers include real robot experiments."""

import logging
import re
import sys
import yaml
from pathlib import Path
from typing import Optional

import requests

sys.path.insert(0, str(Path(__file__).parent))
from paper_model import Paper

logger = logging.getLogger(__name__)

SCRIPTS_DIR = Path(__file__).parent
CONFIG_PATH = SCRIPTS_DIR / "config.yaml"


def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def detect_platform(text: str, config: dict) -> Optional[str]:
    """Detect which humanoid platform was used."""
    text_lower = text.lower()
    platforms = config["real_robot_platforms"]
    for platform in platforms:
        if platform.lower() in text_lower:
            return platform
    return None


def detect_real_robot_for_paper(paper: Paper, config: dict) -> tuple[bool, Optional[str]]:
    """Check if a paper includes real robot experiments. Returns (is_real, platform)."""
    text = (paper.title + " " + paper.abstract).lower()
    indicators = config["real_robot_indicators"]

    indicator_count = 0
    for indicator in indicators:
        if indicator.lower() in text:
            indicator_count += 1

    platform = detect_platform(text, config)

    # Require at least 2 indicators OR one indicator + platform mention
    is_real = indicator_count >= 2 or (indicator_count >= 1 and platform is not None)

    # Strong signal: specific platform name
    if platform:
        is_real = True

    return is_real, platform


def fetch_arxiv_abstract_page(arxiv_id: str) -> Optional[str]:
    """Fetch the arXiv abstract page HTML."""
    url = f"https://arxiv.org/abs/{arxiv_id}"
    try:
        resp = requests.get(url, timeout=10, headers={"User-Agent": "Awesome-Humanoid-Robot-Learning/1.0"})
        if resp.status_code == 200:
            return resp.text
    except Exception as e:
        logger.debug(f"  Failed to fetch page for {arxiv_id}: {e}")
    return None


def detect_real_robot(papers: list[Paper], config: Optional[dict] = None) -> list[Paper]:
    """Detect real robot experiments for all papers."""
    if config is None:
        config = load_config()

    for paper in papers:
        is_real, platform = detect_real_robot_for_paper(paper, config)

        # If unclear from abstract, check the arXiv page for more detail
        if not is_real:
            html = fetch_arxiv_abstract_page(paper.arxiv_id)
            if html:
                # Extract text from HTML (simple tag stripping)
                html_text = re.sub(r'<[^>]+>', ' ', html)
                is_real2, platform2 = detect_real_robot_for_paper(
                    Paper(
                        arxiv_id=paper.arxiv_id,
                        title="",
                        paper_url=paper.paper_url,
                        abstract=html_text,
                    ),
                    config,
                )
                if is_real2:
                    is_real = True
                    platform = platform2 or platform

        paper.real_robot = is_real
        paper.platform = platform
        if is_real:
            logger.info(f"  🤖 Real robot: {paper.title[:60]}... [{platform or 'unknown'}]")

    real_count = sum(1 for p in papers if p.real_robot)
    logger.info(f"Detected {real_count} papers with real robot experiments")
    return papers


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    from fetch_arxiv import load_existing_papers
    papers = list(load_existing_papers().values())
    papers = detect_real_robot(papers)
    for p in papers:
        if p.real_robot:
            print(f"  🤖 [{p.platform or 'unknown'}] {p.title[:60]}")
