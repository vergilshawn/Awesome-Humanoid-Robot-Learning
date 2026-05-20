"""Generate all markdown pages for the VitePress site."""

import json
import logging
import sys
from pathlib import Path
from collections import defaultdict
from datetime import date
from typing import Optional

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from paper_model import Paper

logger = logging.getLogger(__name__)

SCRIPTS_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPTS_DIR.parent
CONFIG_PATH = SCRIPTS_DIR / "config.yaml"
DATA_DIR = PROJECT_ROOT / "data"
DOCS_DIR = PROJECT_ROOT / "docs"
README_PATH = PROJECT_ROOT / "README.md"

CATEGORY_KEY_MAP = {
    "Loco-Manipulation and Whole-Body Control": "loco-manipulation-and-whole-body-control",
    "Manipulation": "manipulation",
    "Teleoperation": "teleoperation",
    "Locomotion": "locomotion",
    "Navigation": "navigation",
    "State Estimation": "state-estimation",
    "Sim-to-Real": "sim-to-real",
    "Hardware Design": "hardware-design",
    "Simulation Benchmark": "simulation-benchmark",
    "Physics-Based Character Animation": "physics-based-character-animation",
    "Human Motion Analysis and Synthesis": "human-motion-analysis-and-synthesis",
}


def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def load_papers() -> list[Paper]:
    papers_file = DATA_DIR / "papers.json"
    if not papers_file.exists():
        return []
    with open(papers_file) as f:
        raw = json.load(f)
    return [Paper(**item) for item in raw]


def ensure_dirs() -> None:
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    for key in CATEGORY_KEY_MAP.values():
        (DOCS_DIR / key).mkdir(parents=True, exist_ok=True)


def cleanup_stale_month_pages() -> None:
    """Remove previously generated month pages before regenerating categories."""
    for key in CATEGORY_KEY_MAP.values():
        cat_dir = DOCS_DIR / key
        if not cat_dir.exists():
            continue
        for path in cat_dir.glob("[0-9][0-9][0-9][0-9]-[0-9][0-9].md"):
            path.unlink()
            logger.info(f"Removed stale generated page {path}")


def format_paper_entry(paper: Paper) -> str:
    """Format a single paper entry as markdown."""
    marker = "🌟 " if paper.open_source else ""
    lines = [f"## {marker}{paper.title}", ""]

    lines.append(f"- **Paper:** [arXiv]({paper.paper_url})")

    if paper.project_url:
        lines.append(f"- **Project:** [GitHub]({paper.project_url})")

    if paper.authors:
        authors = ", ".join(paper.authors[:6])
        if len(paper.authors) > 6:
            authors += f" et al. ({len(paper.authors)} authors)"
        lines.append(f"- **Authors:** {authors}")

    lines.append(f"- **Published:** {paper.published}")

    if paper.real_robot:
        platform_str = f" — {paper.platform}" if paper.platform else ""
        lines.append(f"- **Real Robot:** ✅{platform_str}")

    if paper.tags:
        lines.append("- **Tags:**")
        for tag in paper.tags[:8]:
            lines.append(f"  - {tag}")

    lines.append("")
    lines.append(f"### Summary")
    lines.append("")
    if paper.summary:
        lines.append(paper.summary)
    elif not paper.abstract:
        lines.append("Summary unavailable. This entry was imported from a curated paper list.")
    else:
        # Use first 2 sentences of abstract as summary
        abstract = paper.abstract
        sentences = abstract.replace("\n", " ").split(". ")
        summary = ". ".join(sentences[:2]) + "."
        lines.append(summary)

    lines.append("")
    return "\n".join(lines)


def group_by_month(papers: list[Paper]) -> dict[str, list[Paper]]:
    """Group papers by publication month."""
    groups = defaultdict(list)
    for p in papers:
        if p.published:
            groups[p.published].append(p)
    return dict(sorted(groups.items(), reverse=True))


def format_keywords(paper: Paper, limit: int = 6) -> str:
    """Format a compact keyword list for index-style pages."""
    keywords = []
    for keyword in paper.tags + paper.categories:
        if keyword and keyword not in keywords:
            keywords.append(keyword)

    if paper.real_robot and "Real Robot" not in keywords:
        keywords.append("Real Robot")
    if paper.open_source and "Open Source" not in keywords:
        keywords.append("Open Source")

    return ", ".join(f"`{keyword}`" for keyword in keywords[:limit])


def format_compact_paper_link(paper: Paper) -> str:
    """Format a paper for compact homepage indexes."""
    marker = "🌟 " if paper.open_source else ""
    item = f"{marker}[{paper.title}]({paper.paper_url})"

    if paper.project_url:
        item += f", [website]({paper.project_url})"

    keywords = format_keywords(paper)
    if keywords:
        item += f" — {keywords}"

    return item


def append_homepage_directory_index(lines: list[str], papers: list[Paper]) -> None:
    """Append a compact category/month/paper index to the homepage."""
    cat_papers = defaultdict(list)
    for paper in papers:
        cat_papers[paper.primary_category].append(paper)

    lines.extend([
        "",
        "---",
        "",
        "## 📚 Paper Directory",
        "",
    ])

    for cat_name, cat_key in CATEGORY_KEY_MAP.items():
        cp_list = sorted(
            cat_papers.get(cat_name, []),
            key=lambda p: p.published_date or date.min,
            reverse=True,
        )
        lines.append(f"### [{cat_name}](/{cat_key}/)")
        lines.append("")

        if not cp_list:
            lines.append("- No papers yet.")
            lines.append("")
            continue

        by_month = group_by_month(cp_list)
        for month, month_papers in by_month.items():
            lines.append(f"#### [{month}](/{cat_key}/{month})")
            lines.append("")
            for paper in month_papers:
                lines.append(f"- {format_compact_paper_link(paper)}")
            lines.append("")


def grouped_primary_category_papers(papers: list[Paper]) -> dict[str, list[Paper]]:
    """Group papers by the single directory category used for browsing."""
    cat_papers = defaultdict(list)
    for paper in papers:
        cat_papers[paper.primary_category].append(paper)
    return cat_papers


def generate_readme(papers: list[Paper]) -> None:
    """Generate the GitHub repository homepage README."""
    cat_papers = grouped_primary_category_papers(papers)
    total_count = len(papers)
    real_count = sum(1 for paper in papers if paper.real_robot)
    open_count = sum(1 for paper in papers if paper.open_source)

    lines = [
        "# Awesome-Humanoid-Robot-Learning",
        "",
        "A curated and automatically updated collection of humanoid robot learning research papers.",
        "",
        f"- **Total Papers:** {total_count}",
        f"- **Real Robot Papers:** {real_count}",
        f"- **Open Source Papers:** {open_count}",
        "",
        "🌟 indicates papers with detected project/code links.",
        "",
        "## Contents",
        "",
    ]

    for cat_name in CATEGORY_KEY_MAP:
        count = len(cat_papers.get(cat_name, []))
        lines.append(f"- [{cat_name}](#{cat_name.lower().replace(' ', '-').replace('&', '').replace('/', '').replace('--', '-')}) ({count})")

    lines.extend([
        "- [Usage](#usage)",
        "",
        "---",
        "",
    ])

    for cat_name in CATEGORY_KEY_MAP:
        cp_list = sorted(
            cat_papers.get(cat_name, []),
            key=lambda p: p.published_date or date.min,
            reverse=True,
        )
        lines.append(f"## {cat_name}")
        lines.append("")

        if not cp_list:
            lines.append("- No papers yet.")
            lines.append("")
            continue

        by_month = group_by_month(cp_list)
        for month, month_papers in by_month.items():
            lines.append(f"### {month}")
            lines.append("")
            for paper in month_papers:
                lines.append(f"- {format_compact_paper_link(paper)}")
            lines.append("")

    lines.extend([
        "---",
        "",
        "## Usage",
        "",
        "```bash",
        "# Install dependencies",
        "pip install -r requirements.txt",
        "npm install",
        "",
        "# Update recent papers with daily arXiv windows",
        "python scripts/update_daily.py --days 7",
        "",
        "# Preview the website",
        "npm run docs:dev",
        "```",
        "",
        "## License",
        "",
        "MIT",
        "",
    ])

    README_PATH.write_text("\n".join(lines), encoding="utf-8")
    logger.info(f"Generated {README_PATH}")


def generate_homepage(papers: list[Paper]) -> None:
    """Generate docs/index.md."""
    by_month = group_by_month(papers)
    latest_month = next(iter(by_month)) if by_month else "2026-02"
    latest_papers = papers[:10] if papers else []

    real_count = sum(1 for p in papers if p.real_robot)
    open_count = sum(1 for p in papers if p.open_source)

    # Category stats use primary category only, so each paper is counted once.
    cat_counts = defaultdict(int)
    for p in papers:
        cat_counts[p.primary_category] += 1

    # Tag counts
    tag_counts = defaultdict(int)
    for p in papers:
        for t in p.tags:
            tag_counts[t] += 1
    top_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:30]

    lines = [
        "# Awesome-Humanoid-Robot-Learning",
        "",
        "A curated and automatically updated collection of humanoid robot learning research papers.",
        "",
        "🌟 indicates open-source code. Papers with real robot experiments are prioritized.",
        "",
        "---",
        "",
        "## 📊 Statistics",
        "",
        f"- **Total Papers:** {len(papers)}",
        f"- **Real Robot Papers:** {real_count}",
        f"- **Open Source Papers:** {open_count}",
        f"- **Latest Month:** {latest_month}",
        "",
        "### Categories",
        "",
    ]

    for cat_name, cat_key in CATEGORY_KEY_MAP.items():
        count = cat_counts.get(cat_name, 0)
        lines.append(f"- [{cat_name}](/{cat_key}/) ({count})")

    lines.extend([
        "",
        "---",
        "",
        "## 🔥 Latest Papers",
        "",
    ])

    for paper in latest_papers:
        marker = "🌟" if paper.open_source else ""
        robot = " 🤖" if paper.real_robot else ""
        cat_key = CATEGORY_KEY_MAP.get(paper.primary_category, "")
        cat_links = f"[{paper.primary_category}](/{cat_key}/)" if cat_key else ""
        lines.append(f"- {marker}{robot} [{paper.title}]({paper.paper_url}) — {paper.published}")
        if cat_links:
            lines.append(f"  - {cat_links}")

    lines.extend([
        "",
        "---",
        "",
        "## 🏷️ Top Tags",
        "",
    ])

    for tag, count in top_tags:
        lines.append(f"- **{tag}** ({count})")

    append_homepage_directory_index(lines, papers)

    lines.extend([
        "",
        "---",
        "",
        "## 📂 Navigation",
        "",
        "- [Latest Papers](/latest)",
        "- [Real Robot Papers](/real-robot)",
        "- [Open Source Papers](/open-source)",
        "- [Tags](/tags)",
        "",
    ])

    out_path = DOCS_DIR / "index.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    logger.info(f"Generated {out_path}")


def generate_latest(papers: list[Paper]) -> None:
    """Generate docs/latest.md."""
    lines = [
        "# Latest Papers",
        "",
        "All papers sorted by publication date (newest first).",
        "",
    ]

    for paper in papers:
        lines.append(format_paper_entry(paper))
        lines.append("---")
        lines.append("")

    out_path = DOCS_DIR / "latest.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    logger.info(f"Generated {out_path}")


def generate_real_robot(papers: list[Paper]) -> None:
    """Generate docs/real-robot.md."""
    real_papers = [p for p in papers if p.real_robot]
    real_papers.sort(key=lambda p: p.published_date or date.min, reverse=True)

    # Group by platform
    platform_papers = defaultdict(list)
    for p in real_papers:
        platform = p.platform or "Unknown Platform"
        platform_papers[platform].append(p)

    lines = [
        "# Real Robot Papers",
        "",
        "Papers with real humanoid robot deployment and experiments.",
        "",
    ]

    # Platform overview
    lines.append("## Platforms")
    lines.append("")
    for platform, pp in sorted(platform_papers.items()):
        lines.append(f"- **{platform}:** {len(pp)} papers")
    lines.append("")

    # All real robot papers
    lines.append("---")
    lines.append("")
    lines.append("## All Real Robot Papers")
    lines.append("")

    for paper in real_papers:
        lines.append(format_paper_entry(paper))
        lines.append("---")
        lines.append("")

    out_path = DOCS_DIR / "real-robot.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    logger.info(f"Generated {out_path}")


def generate_open_source(papers: list[Paper]) -> None:
    """Generate docs/open-source.md."""
    open_papers = [p for p in papers if p.open_source]
    open_papers.sort(key=lambda p: p.published_date or date.min, reverse=True)

    lines = [
        "# Open Source Papers",
        "",
        "Papers with open-source code repositories.",
        "",
    ]

    for paper in open_papers:
        lines.append(format_paper_entry(paper))
        lines.append("---")
        lines.append("")

    out_path = DOCS_DIR / "open-source.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    logger.info(f"Generated {out_path}")


def generate_tags(papers: list[Paper]) -> None:
    """Generate docs/tags.md."""
    tag_papers = defaultdict(list)
    for p in papers:
        for t in p.tags:
            tag_papers[t].append(p)

    sorted_tags = sorted(tag_papers.items(), key=lambda x: len(x[1]), reverse=True)

    lines = [
        "# Tags",
        "",
        "Browse papers by research topic and methodology.",
        "",
        "---",
        "",
    ]

    for tag, tag_paper_list in sorted_tags:
        lines.append(f"## {tag} ({len(tag_paper_list)})")
        lines.append("")
        for paper in tag_paper_list[:5]:
            marker = "🌟 " if paper.open_source else ""
            lines.append(f"- {marker}[{paper.title}]({paper.paper_url}) — {paper.published}")
        lines.append("")

    out_path = DOCS_DIR / "tags.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    logger.info(f"Generated {out_path}")


def generate_category_pages(papers: list[Paper]) -> None:
    """Generate category index and monthly pages."""
    cleanup_stale_month_pages()

    # Group papers by primary category. A paper appears in exactly one category directory.
    cat_papers = grouped_primary_category_papers(papers)

    for cat_name, cat_key in CATEGORY_KEY_MAP.items():
        cat_dir = DOCS_DIR / cat_key
        cat_dir.mkdir(parents=True, exist_ok=True)

        cp_list = cat_papers.get(cat_name, [])
        by_month = group_by_month(cp_list)

        # Category index page
        index_lines = [
            f"# {cat_name}",
            "",
            f"**{len(cp_list)} papers** in this category.",
            "",
            "## Months",
            "",
        ]

        for month, month_papers in sorted(by_month.items(), reverse=True):
            index_lines.append(f"- [{month}](/{cat_key}/{month}) ({len(month_papers)} papers)")

        index_lines.extend([
            "",
            "---",
            "",
            "## Recent Papers",
            "",
        ])

        for paper in sorted(cp_list, key=lambda p: p.published_date or date.min, reverse=True)[:20]:
            index_lines.append(format_paper_entry(paper))
            index_lines.append("---")
            index_lines.append("")

        (cat_dir / "index.md").write_text("\n".join(index_lines), encoding="utf-8")
        logger.info(f"Generated {cat_dir / 'index.md'}")

        # Monthly pages
        for month, month_papers in sorted(by_month.items(), reverse=True):
            month_lines = [
                f"# {cat_name} Papers — {month}",
                "",
                f"**{len(month_papers)} papers** from {month}.",
                "",
            ]

            for paper in month_papers:
                month_lines.append(format_paper_entry(paper))
                month_lines.append("---")
                month_lines.append("")

            (cat_dir / f"{month}.md").write_text("\n".join(month_lines), encoding="utf-8")

        # Only log once per category
        logger.info(f"Generated {cat_name}: {len(by_month)} months, {len(cp_list)} papers")


def generate_all(papers: Optional[list[Paper]] = None) -> None:
    """Generate all markdown pages."""
    if papers is None:
        papers = load_papers()

    ensure_dirs()

    generate_homepage(papers)
    generate_latest(papers)
    generate_real_robot(papers)
    generate_open_source(papers)
    generate_tags(papers)
    generate_category_pages(papers)
    generate_readme(papers)

    logger.info("All markdown pages generated successfully.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    generate_all()
