"""Batch metadata refresh and checkpointed audit of existing paper code links."""
import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
import time
import xml.etree.ElementTree as ET

from detect_project_links import audit_paper, fetch_text, load_config
from fetch_arxiv import load_existing_papers, save_papers
from generate_markdown import generate_all


def refresh_metadata(papers):
    found = set()
    namespace = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    by_id = {p.arxiv_id: p for p in papers}
    for start in range(0, len(papers), 80):
        ids = ",".join(p.arxiv_id for p in papers[start:start + 80])
        try:
            root = ET.fromstring(fetch_text("https://export.arxiv.org/api/query?id_list=" + ids + "&max_results=80").text)
            for entry in root.findall("a:entry", namespace):
                identifier = entry.findtext("a:id", "", namespace).split("/abs/")[-1]
                import re
                identifier = re.sub(r"v\d+$", "", identifier)
                if identifier not in by_id:
                    continue
                p = by_id[identifier]
                p.comments = entry.findtext("arxiv:comment", "", namespace)
                p.abstract = entry.findtext("a:summary", p.abstract, namespace).strip().replace("\n", " ")
                found.add(identifier)
            print(f"Metadata {min(start + 80, len(papers))}/{len(papers)}; retrieved {len(found)}", flush=True)
        except Exception as exc:
            print(f"Metadata batch {start}: {type(exc).__name__}; will use abstract pages", flush=True)
        time.sleep(3)
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--retry-unknown", action="store_true")
    parser.add_argument("--status", action="append", help="Recheck only selected statuses; repeatable")
    args = parser.parse_args()
    logging.basicConfig(level=logging.WARNING)
    existing = load_existing_papers()
    selected = [p.model_copy(deep=True) for p in existing.values() if (not args.retry_unknown or p.code_status == "unknown") and (not args.status or p.code_status in args.status)]
    config = load_config()
    config["arxiv_metadata_ids"] = refresh_metadata(selected)
    counts = Counter()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(audit_paper, p, config): p for p in selected}
        for number, future in enumerate(as_completed(futures), 1):
            p = futures[future]
            try:
                p = future.result()
            except Exception as exc:
                p.code_status = "unknown"
                p.open_source = False
                p.code_evidence = [f"Audit failed: {type(exc).__name__}"]
            existing[p.arxiv_id] = p
            counts[p.code_status] += 1
            print(f"{number}/{len(selected)} {p.arxiv_id} {p.code_status} | {dict(counts)}", flush=True)
            if number % 20 == 0:
                save_papers(list(existing.values()))
    papers = list(existing.values())
    save_papers(papers)
    generate_all(papers)
    print("FINAL", dict(Counter(p.code_status for p in papers)), flush=True)


if __name__ == "__main__":
    main()
