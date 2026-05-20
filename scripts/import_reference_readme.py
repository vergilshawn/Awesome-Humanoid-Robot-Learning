#!/usr/bin/env python3
"""Import curated arXiv entries from a reference awesome-list README."""

import argparse
import json
import re
from datetime import date
from pathlib import Path

import yaml

from classify_papers import tag_paper
from paper_model import Paper

SCRIPTS_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPTS_DIR.parent
CONFIG_PATH = SCRIPTS_DIR / "config.yaml"
DATA_PATH = PROJECT_ROOT / "data" / "papers.json"

CATEGORY_ALIASES = {
    "Loco-Manipulation and Whole-Body-Control": "Loco-Manipulation and Whole-Body Control",
}


def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def parse_reference_readme(path: Path, through_month: str) -> list[Paper]:
    current_category = ""
    papers = []
    category_re = re.compile(r"^## (.+)$")
    arxiv_re = re.compile(
        r"^\s*-\s*(?P<star>🌟)?\s*"
        r"\[(?:arXiv|arXib)(?: (?P<month>\d{4}\.\d{2}))?\]"
        r"\(https://(?:www\.)?arxiv\.org/(?:abs|pdf)/(?P<arxiv_id>\d{4}\.\d{4,5})(?:v\d+)?\)"
        r"(?P<rest>.*)$",
        re.IGNORECASE,
    )
    website_re = re.compile(r"\[website\]\((?P<url>[^)]+)\)")

    for line in path.read_text(encoding="utf-8").splitlines():
        category_match = category_re.match(line)
        if category_match:
            current_category = CATEGORY_ALIASES.get(category_match.group(1), category_match.group(1))
            continue

        match = arxiv_re.match(line)
        if not match or not current_category:
            continue

        arxiv_id = match.group("arxiv_id")
        published = (match.group("month") or f"20{arxiv_id[:2]}.{arxiv_id[2:4]}").replace(".", "-")
        if published > through_month:
            continue

        rest = match.group("rest").lstrip(" ,/")
        website_match = website_re.search(rest)
        project_url = website_match.group("url") if website_match else None
        title = website_re.sub("", rest).strip().rstrip(",").strip()
        title = re.sub(r"^\[website\]\s*,?\s*", "", title).strip()
        title = re.sub(r"^/\s*[^,]+,\s*", "", title).strip()

        papers.append(
            Paper(
                arxiv_id=arxiv_id,
                title=title,
                paper_url=f"https://arxiv.org/abs/{arxiv_id}",
                project_url=project_url,
                authors=[],
                published=published,
                published_date=date(int(published[:4]), int(published[5:7]), 1),
                abstract="",
                categories=[current_category],
                real_robot=False,
                open_source=bool(project_url or match.group("star")),
                platform=None,
                summary="",
                primary_category=current_category,
            )
        )

    return papers


def load_existing() -> dict[str, Paper]:
    if not DATA_PATH.exists():
        return {}
    return {Paper(**item).arxiv_id: Paper(**item) for item in json.loads(DATA_PATH.read_text())}


def merge_imported(existing: dict[str, Paper], imported: list[Paper], config: dict) -> list[Paper]:
    for paper in imported:
        if paper.arxiv_id in existing:
            current = existing[paper.arxiv_id]
            if not current.project_url and paper.project_url:
                current.project_url = paper.project_url
                current.open_source = True
            if not current.categories:
                current.categories = paper.categories
                current.primary_category = paper.primary_category
        else:
            paper.tags = tag_paper(paper, config)
            existing[paper.arxiv_id] = paper

    return sorted(existing.values(), key=lambda p: p.published_date or date.min, reverse=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Import curated entries from a reference README")
    parser.add_argument("readme", type=Path, help="Path to the reference README.md")
    parser.add_argument("--through-month", default="2026-03", help="Import entries up to YYYY-MM inclusive")
    args = parser.parse_args()

    config = load_config()
    imported = parse_reference_readme(args.readme, args.through_month)
    existing = load_existing()
    initial_count = len(existing)
    merged = merge_imported(existing, imported, config)

    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    DATA_PATH.write_text(
        json.dumps([paper.model_dump() for paper in merged], indent=2, default=str, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    added = len({paper.arxiv_id for paper in merged}) - initial_count
    print(f"Imported {len(imported)} reference entries, added {added}, total {len(merged)}")


if __name__ == "__main__":
    main()
