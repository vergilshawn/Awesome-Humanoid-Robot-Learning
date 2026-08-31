#!/usr/bin/env python3
"""Apply reviewed exclusions, normalize metadata, and rebuild generated pages."""

import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from classify_papers import classify_papers
from detect_real_robot import detect_real_robot_for_paper
from fetch_arxiv import load_existing_papers, save_papers
from generate_markdown import generate_all as generate_all_markdown
from generate_vitepress import generate_all as generate_all_vitepress
from semantic_filter import compute_relevance_score, load_config, load_curation

ROOT = Path(__file__).parent.parent
REPORT_PATH = ROOT / "data" / "curation-report.json"
MARKDOWN_LINK = re.compile(r"\s*,?\s*/?\s*\[[^]]+\]\((https?://[^)]+)\)")


def normalize_paper(paper):
    """Repair imported Markdown fragments and canonical arXiv metadata fields."""
    links = MARKDOWN_LINK.findall(paper.title)
    if links and not paper.project_url:
        paper.project_url = links[0]
        paper.open_source = "github.com" in links[0] or "gitlab.com" in links[0]
    paper.title = MARKDOWN_LINK.sub("", paper.title).replace("**", "").strip(" ,/")
    paper.paper_url = f"https://arxiv.org/abs/{paper.arxiv_id}"
    if paper.published_date:
        paper.published = paper.published_date.strftime("%Y-%m")
    return paper


def main():
    config = load_config()
    curation = load_curation()
    excluded = curation.get("exclude", {})
    strict_from = config["relevance_keywords"]["strict_filter_from"]
    papers = list(load_existing_papers().values())
    kept = []
    removed = []

    for paper in papers:
        if paper.arxiv_id in excluded:
            removed.append({
                "arxiv_id": paper.arxiv_id,
                "title": paper.title,
                "reason": excluded[paper.arxiv_id],
                "decision": "human-reviewed exclusion",
            })
            continue
        published_date = str(paper.published_date or f"{paper.published}-01")
        score, _ = compute_relevance_score(
            paper.title,
            paper.abstract,
            config,
            require_context=published_date >= strict_from,
        )
        if paper.abstract and score < 4:
            removed.append({
                "arxiv_id": paper.arxiv_id,
                "title": paper.title,
                "reason": "insufficient evidence that humanoid/biped robotics is the research target",
                "decision": "strict relevance gate",
            })
            continue
        kept.append(normalize_paper(paper))

    kept = classify_papers(kept, config)
    for paper in kept:
        paper.real_robot, paper.platform = detect_real_robot_for_paper(paper, config)

    save_papers(kept)
    tags = Counter(tag for paper in kept for tag in paper.tags)
    categories = Counter(paper.primary_category for paper in kept)
    (ROOT / "data" / "tags.json").write_text(
        json.dumps(dict(tags.most_common()), indent=2) + "\n"
    )
    (ROOT / "data" / "categories.json").write_text(
        json.dumps(dict(categories.most_common()), indent=2) + "\n"
    )
    previous_removed = []
    if REPORT_PATH.exists():
        previous_removed = json.loads(REPORT_PATH.read_text()).get("removed", [])
    removed_by_id = {item["arxiv_id"]: item for item in previous_removed}
    removed_by_id.update({item["arxiv_id"]: item for item in removed})
    all_removed = sorted(removed_by_id.values(), key=lambda item: item["arxiv_id"], reverse=True)
    report = {
        "input_count": len(kept) + len(all_removed),
        "kept_count": len(kept),
        "removed_count": len(all_removed),
        "human_reviewed_exclusions": sum(
            item["decision"] == "human-reviewed exclusion" for item in all_removed
        ),
        "removed": all_removed,
    }
    REPORT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    generate_all_markdown(kept)
    generate_all_vitepress(kept)
    print(
        f"Curated {report['input_count']} -> {len(kept)} papers; "
        f"removed {len(all_removed)}"
    )


if __name__ == "__main__":
    main()
