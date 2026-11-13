"""Shared code-status labels and review report, independent of network access."""
from collections import Counter
import json
from pathlib import Path

CODE_LABELS = {
    "unverified": "Unverified / 未核验",
    "not_found": "No project/code link found / 未发现项目或代码链接",
    "no_repository": "Project page only / 项目页未发现仓库",
    "coming_soon": "Coming soon / 代码待发布",
    "empty": "Placeholder or no implementation detected / 占位仓库或未检测到实现",
    "partial": "Partial release / 部分代码或资源待发布",
    "available": "Implementation detected (completeness unverified) / 已检测到实现，完整性未核验",
    "unknown": "Needs review / 访问失败或证据不足",
}


def write_code_report(papers):
    path = Path(__file__).resolve().parent.parent / "data" / "curation-report.json"
    report = json.loads(path.read_text()) if path.exists() else {}
    report["code_audit"] = {
        "status_counts": dict(Counter(p.code_status for p in papers)),
        "status_labels": CODE_LABELS,
        "checked_count": sum(bool(p.code_checked_at) for p in papers),
        "unverified_count": sum(p.code_status == "unverified" for p in papers),
        "needs_review_count": sum(p.code_status == "unknown" for p in papers),
        "method": "arXiv metadata and Comments; project page; GitHub README and file tree, with public HTML, blobless Git tree and bounded archive fallbacks when API access fails",
        "policy": "Source-file detection does not establish completeness, reproducibility or license compliance. Legacy links are unverified until inspected.",
        "papers": [
            {"arxiv_id": p.arxiv_id, "title": p.title, "project_url": p.project_url,
             "repository_url": p.repository_url, "status": p.code_status, "status_label": CODE_LABELS[p.code_status],
             "checked_at": p.code_checked_at, "evidence": p.code_evidence}
            for p in papers
        ],
    }
    path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
