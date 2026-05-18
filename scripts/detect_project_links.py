"""Detect open-source project links (GitHub, HuggingFace, etc.) in papers."""

import logging
import re
import sys
import yaml
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

import requests

sys.path.insert(0, str(Path(__file__).parent))
from paper_model import Paper

logger = logging.getLogger(__name__)

SCRIPTS_DIR = Path(__file__).parent
CONFIG_PATH = SCRIPTS_DIR / "config.yaml"

# Match GitHub repos, HuggingFace, etc.
URL_PATTERNS = [
    r'(?:https?://)?github\.com/[\w\-\.]+/[\w\-\.]+',
    r'(?:https?://)?gitlab\.com/[\w\-\.]+/[\w\-\.]+',
    r'(?:https?://)?huggingface\.co/[\w\-\.]+/[\w\-\.]+',
    r'(?:https?://)?bitbucket\.org/[\w\-\.]+/[\w\-\.]+',
]

# Patterns for project page mentions
PROJECT_PAGE_PATTERNS = [
    r'project\s*(?:page|website|url)?:?\s*(https?://[^\s,;]+)',
    r'code\s*(?:is\s*)?(?:available|released|open|public)?\s*(?:at|on)?:?\s*(https?://[^\s,;]+)',
    r'(?:github|code|source|repository):\s*(https?://[^\s,;]+)',
    r'(?:open.source|open source).*?(https?://[^\s,;]+)',
    r'(?:available|released|published)\s*(?:at|on)\s*(https?://github\.com[^\s,;]+)',
    r'(?:visit|see|check)\s*(?:https?://github\.com[^\s,;]+)',
]


def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def extract_urls(text: str) -> list[str]:
    """Extract all URLs from text."""
    url_pattern = r'https?://[^\s,;\)\"\]]+'
    return [re.sub(r'[;,\.\)\}\]"\']+$', '', url) for url in re.findall(url_pattern, text)]


def matches_project_pattern(url: str) -> bool:
    """Check whether a URL has the shape of a repository or model/project page."""
    return any(re.fullmatch(pattern, url, flags=re.IGNORECASE) for pattern in URL_PATTERNS)


def is_generic_platform_url(url: str) -> bool:
    """Reject common platform home/profile URLs that are not paper-specific projects."""
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    parts = [part for part in parsed.path.strip("/").split("/") if part]

    if host == "huggingface.co" and parts in ([], ["huggingface"]):
        return True
    if host in {"github.com", "gitlab.com", "bitbucket.org"} and len(parts) < 2:
        return True
    return False


def is_project_url(url: str, config: dict) -> bool:
    """Check if a URL is a project/code repository link."""
    url_lower = url.lower()
    if is_generic_platform_url(url_lower):
        return False
    if not matches_project_pattern(url):
        return False
    platforms = config.get("open_source_platforms", [])
    for platform in platforms:
        if platform in url_lower:
            return True
    return False


def find_best_project_url(urls: list[str], config: dict) -> Optional[str]:
    """Find the most likely project URL from a list."""
    candidate_urls = [u for u in urls if is_project_url(u, config)]

    if not candidate_urls:
        return None

    # Prefer GitHub
    for url in candidate_urls:
        if "github.com" in url:
            return url

    return candidate_urls[0]


def detect_project_url_for_paper(paper: Paper, config: dict) -> Optional[str]:
    """Detect project URL from paper abstract (and optionally paper page)."""
    text = (paper.title + " " + paper.abstract).lower()
    all_urls = extract_urls(text)
    return find_best_project_url(all_urls, config)


def fetch_arxiv_abstract_page(arxiv_id: str) -> Optional[str]:
    """Fetch the arXiv abstract page HTML to look for project links."""
    url = f"https://arxiv.org/abs/{arxiv_id}"
    try:
        resp = requests.get(url, timeout=10, headers={"User-Agent": "Awesome-Humanoid-Robot-Learning/1.0"})
        if resp.status_code == 200:
            return resp.text
    except Exception as e:
        logger.debug(f"  Failed to fetch abstract page for {arxiv_id}: {e}")
    return None


def detect_project_links(papers: list[Paper], config: Optional[dict] = None) -> list[Paper]:
    """Detect project URLs for all papers."""
    if config is None:
        config = load_config()

    for paper in papers:
        # First try from abstract
        url = detect_project_url_for_paper(paper, config)

        # If not found, try fetching the arXiv page
        if not url:
            html = fetch_arxiv_abstract_page(paper.arxiv_id)
            if html:
                all_urls = extract_urls(html)
                url = find_best_project_url(all_urls, config)

        if url:
            paper.project_url = url
            paper.open_source = True
            logger.info(f"  🌟 Found project: {url}")

    open_count = sum(1 for p in papers if p.open_source)
    logger.info(f"Detected {open_count} papers with open-source code")
    return papers


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    from fetch_arxiv import load_existing_papers
    papers = list(load_existing_papers().values())
    papers = detect_project_links(papers)
    for p in papers:
        if p.project_url:
            print(f"  🌟 {p.title[:60]} -> {p.project_url}")
