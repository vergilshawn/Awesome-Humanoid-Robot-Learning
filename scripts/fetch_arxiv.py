"""Fetch recent papers from arXiv across configured categories.

Uses the arxiv 4.x API: Client().results(search) returns Result iterables.
"""

import logging
import re
import sys
import time
from pathlib import Path
from datetime import date, datetime
from typing import Optional

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from paper_model import Paper

logger = logging.getLogger(__name__)

SCRIPTS_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPTS_DIR.parent
CONFIG_PATH = SCRIPTS_DIR / "config.yaml"
DATA_DIR = PROJECT_ROOT / "data"


def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def parse_arxiv_date(d: datetime) -> str:
    return d.strftime("%Y-%m")


def extract_arxiv_id(entry_id: str) -> str:
    """Extract arxiv ID from entry_id, stripping version suffix and URL prefix.

    Handles:
      - http://arxiv.org/abs/2405.12345v1  -> 2405.12345
      - http://arxiv.org/abs/2405.12345    -> 2405.12345
      - 2405.12345v1                        -> 2405.12345
      - 2405.12345                          -> 2405.12345
      - http://arxiv.org/abs/2405.12345v10 -> 2405.12345
    """
    # If entry_id is a URL, extract the ID portion
    if "arxiv.org" in entry_id:
        entry_id = entry_id.split("/")[-1]
    # Strip version suffix (e.g., v1, v2, v10)
    entry_id = re.sub(r"v\d+$", "", entry_id)
    return entry_id


def date_range_query(date_from: datetime, date_to: Optional[datetime]) -> str:
    """Build an arXiv submittedDate range query."""
    if not date_to:
        return ""
    return (
        "submittedDate:"
        f"[{date_from.strftime('%Y%m%d')}0000 TO {date_to.strftime('%Y%m%d')}0000]"
    )


def build_search_queries(config: dict, date_from: datetime, date_to: Optional[datetime]) -> list[str]:
    """Build category and topic queries for better recall."""
    arxiv_config = config["arxiv"]
    queries = [f"cat:{cat}" for cat in arxiv_config["categories"]]

    queries.extend(arxiv_config.get("topic_queries", []))

    range_query = date_range_query(date_from, date_to)
    if range_query:
        queries = [f"({query}) AND {range_query}" for query in queries]

    return queries


def fetch_papers(config: Optional[dict] = None) -> list[Paper]:
    """Fetch papers from arXiv and return as Paper models."""
    if config is None:
        config = load_config()

    arxiv_config = config["arxiv"]
    max_results = arxiv_config["max_results_per_category"]
    date_from = datetime.strptime(arxiv_config["date_from"], "%Y-%m-%d")
    date_to = None
    if arxiv_config.get("date_to"):
        date_to = datetime.strptime(arxiv_config["date_to"], "%Y-%m-%d")
    request_delay = arxiv_config.get("request_delay", 3.0)
    fail_on_category_error = arxiv_config.get("fail_on_category_error", False)

    # Use arxiv 4.x Client API
    from arxiv import Client, Search, SortCriterion, SortOrder

    client = Client()
    all_papers: dict[str, Paper] = {}
    failed_queries: list[str] = []
    search_queries = build_search_queries(config, date_from, date_to)

    for query in search_queries:
        logger.info(f"Searching arXiv query: {query}")
        search = Search(
            query=query,
            max_results=max_results,
            sort_by=SortCriterion.SubmittedDate,
            sort_order=SortOrder.Descending,
        )

        try:
            results = list(client.results(search))
        except Exception as e:
            logger.error(f"Failed to fetch query {query}: {e}")
            failed_queries.append(query)
            continue

        for result in results:
            pub_date = result.published.date() if result.published else None
            if pub_date and pub_date < date_from.date():
                continue
            if date_to and pub_date and pub_date >= date_to.date():
                continue

            arxiv_id = extract_arxiv_id(result.entry_id)

            if arxiv_id in all_papers:
                continue

            authors = [a.name for a in result.authors] if result.authors else []
            pub_str = parse_arxiv_date(result.published) if result.published else ""

            paper = Paper(
                arxiv_id=arxiv_id,
                title=result.title.strip().replace("\n", " "),
                paper_url=f"https://arxiv.org/abs/{arxiv_id}",
                authors=authors,
                published=pub_str,
                published_date=pub_date,
                abstract=result.summary.strip().replace("\n", " "),
            )
            all_papers[arxiv_id] = paper

        logger.info(f"  Found {len(all_papers)} papers so far...")
        time.sleep(request_delay)

    if failed_queries and len(failed_queries) == len(search_queries):
        failed = ", ".join(failed_queries)
        raise RuntimeError(f"Failed to fetch every configured arXiv query: {failed}")
    if failed_queries and fail_on_category_error:
        failed = ", ".join(failed_queries)
        raise RuntimeError(f"Failed to fetch configured arXiv queries: {failed}")

    papers = sorted(all_papers.values(), key=lambda p: p.published_date or date.min, reverse=True)
    logger.info(f"Total unique papers fetched: {len(papers)}")
    return papers


def load_existing_papers() -> dict[str, Paper]:
    """Load existing papers from data/papers.json."""
    papers_file = DATA_DIR / "papers.json"
    if not papers_file.exists():
        return {}
    import json
    with open(papers_file) as f:
        raw = json.load(f)
    result = {}
    for item in raw:
        p = Paper(**item)
        result[p.arxiv_id] = p
    return result


def save_papers(papers: list[Paper]) -> None:
    """Save papers to data/papers.json."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    import json
    papers_file = DATA_DIR / "papers.json"
    papers_data = [p.model_dump() for p in papers]
    with open(papers_file, "w") as f:
        json.dump(papers_data, f, indent=2, default=str, ensure_ascii=False)
    logger.info(f"Saved {len(papers)} papers to {papers_file}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    papers = fetch_papers()
    save_papers(papers)
