"""Discover project pages and conservatively audit code availability.

A repository URL is not evidence that code has been released. Source-file
presence is a heuristic, never a claim of reproducibility or completeness.
"""
import base64
from datetime import datetime, timezone
from html.parser import HTMLParser
import logging
import json
import tarfile
import time
import subprocess
import tempfile
import os
from pathlib import Path
import re
from typing import Optional
from urllib.parse import urljoin, urlparse, quote

import requests
import yaml

from paper_model import Paper

logger = logging.getLogger(__name__)
CONFIG_PATH = Path(__file__).with_name("config.yaml")
HOSTS = {"github.com", "gitlab.com", "bitbucket.org", "huggingface.co"}
PENDING = re.compile(r"(?:code|implementation|repository|training|evaluation|checkpoints?|weights?)[^.!?\n]{0,70}(?:coming soon|will be (?:released|available)|to be released|not (?:yet )?(?:released|available)|\bpending\b)|coming soon[^.!?\n]{0,40}(?:code|implementation)", re.I)
PARTIAL = re.compile(r"(?:partial(?:ly)? (?:code |implementation )?release|(?:only|inference.only) (?:inference|evaluation)|(?:training|evaluation|deployment) (?:code|scripts?) (?:is |are )?(?:missing|not included)|\[ \][^\n]{0,60}(?:release|publish)[^\n]{0,40}(?:code|training|checkpoint|weights))", re.I)
_API_UNAVAILABLE = False
SOURCE_SUFFIXES = {".py", ".cpp", ".cc", ".c", ".cu", ".h", ".hpp", ".jl", ".rs", ".m", ".ipynb"}


class PageParser(HTMLParser):
    """Extract visible text/anchors, optionally only arXiv abstract/comments."""
    def __init__(self, scoped=False, comments_only=False):
        super().__init__(convert_charrefs=True)
        self.scoped = scoped
        self.comments_only = comments_only
        self.stack = []
        self.text = []
        self.links = []
        self.anchor = None
        self.redirect = None

    def handle_starttag(self, tag, attrs):
        attrs = {key: value or "" for key, value in attrs}
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh":
            match = re.search(r"url\s*=\s*(.+)", attrs.get("content", ""), re.I)
            if match:
                self.redirect = match.group(1).strip(" \"'")
        parent = self.stack[-1] if self.stack else (False, False)
        classes = attrs.get("class", "").split()
        active = parent[0] or ("abstract" in classes and not self.comments_only) or "comments" in classes
        hidden = parent[1] or tag in {"script", "style", "footer"}
        if tag not in {"br", "hr", "img", "meta", "link", "input", "wbr", "source", "area", "base", "embed", "param", "track", "col"}:
            self.stack.append((active, hidden))
        if tag == "input" and attrs.get("type") == "checkbox" and not hidden:
            self.text.append("[x]" if "checked" in attrs else "[ ]")
        if tag == "a" and not hidden and (active or not self.scoped):
            self.anchor = [attrs.get("href", ""), [attrs.get("aria-label", ""), attrs.get("title", "")]]
        if tag == "img" and self.anchor:
            self.anchor[1].append(attrs.get("alt", ""))

    def handle_endtag(self, tag):
        if tag == "a" and self.anchor:
            self.links.append((self.anchor[0], " ".join(self.anchor[1])))
            self.anchor = None
        if self.stack and tag not in {"br", "hr", "img", "meta", "link", "input", "wbr"}:
            self.stack.pop()

    def handle_data(self, data):
        active, hidden = self.stack[-1] if self.stack else (False, False)
        if not hidden and (active or not self.scoped):
            self.text.append(data)
            if self.anchor:
                self.anchor[1].append(data)


def load_config():
    return yaml.safe_load(CONFIG_PATH.read_text())


def extract_urls(text):
    explicit = re.findall(r'https?://[^\s<>"\]{}\\]+', text)
    bare = re.findall(r'(?<![/\w.-])(?:github\.com|gitlab\.com|[\w.-]+\.github\.io)(?:/[^\s<>"\]{}\\]*)?', text, re.I)
    return list(dict.fromkeys(u.rstrip(".,;)}]>\'\"") for u in explicit + ["https://" + u for u in bare]))


def repository_url(url):
    parsed = urlparse(url)
    parts = parsed.path.strip("/").split("/")
    if parsed.hostname not in HOSTS or len(parts) < 2 or not all(parts[:2]):
        return None
    if parts[0] in {"features", "topics", "collections", "organizations", "sponsors", "settings"}:
        return None
    count = 3 if parsed.hostname == "huggingface.co" and parts[0] in {"datasets", "spaces"} else 2
    if len(parts) < count or not all(re.fullmatch(r"[\w.-]+", part) for part in parts[:count]):
        return None
    return f"https://{parsed.hostname}/{'/'.join(parts[:count]).removesuffix('.git')}"


def is_generic_platform_url(url):
    return urlparse(url).hostname in HOSTS and not repository_url(url)


def matches_project_pattern(url):
    return bool(repository_url(url))


def is_project_url(url, config):
    return bool(repository_url(url))


def find_best_project_url(urls, config):
    repos = [repository_url(u) for u in urls if repository_url(u)]
    return next((u for u in repos if urlparse(u).hostname == "github.com"), repos[0] if repos else None)


def project_candidates(text, comments=False):
    """Accept explicit project/code mentions and standalone URLs in Comments."""
    candidates = []
    for url in extract_urls(text):
        host = urlparse(url).hostname or ""
        if host in HOSTS and not repository_url(url):
            continue
        if host in {"arxiv.org", "doi.org", "youtube.com", "www.youtube.com", "youtu.be"}:
            continue
        prefix = text[max(0, text.find(url) - 100):text.find(url)]
        if comments or repository_url(url) or host.endswith(".github.io") or re.search(r"project|code|website|available", prefix, re.I):
            candidates.append(url)
    return list(dict.fromkeys(candidates))


def detect_project_url_for_paper(paper, config):
    urls = project_candidates(paper.abstract) + project_candidates(paper.comments, comments=True)
    return next((u for u in urls if not repository_url(u)), urls[0] if urls else None)


def fetch_text(url, api=False):
    headers = {"User-Agent": "Awesome-Humanoid-Robot-Learning/2.0"}
    if api and os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    return response


def fetch_project_page(url):
    for _ in range(4):
        response = fetch_text(url)
        parser = PageParser()
        parser.feed(response.text)
        if not parser.redirect:
            return response
        destination = urljoin(response.url, parser.redirect)
        if urlparse(destination).scheme not in {"http", "https"} or destination == url:
            break
        url = destination
    raise requests.TooManyRedirects("Project HTML redirect could not be resolved")


def fetch_arxiv_abstract_page(arxiv_id):
    try:
        return fetch_text(f"https://arxiv.org/abs/{arxiv_id}").text
    except requests.RequestException:
        return None


def github_tree(html):
    for script in re.findall(r'<script[^>]*type="application/json"[^>]*>(.*?)</script>', html, re.S):
        try:
            route = json.loads(script).get("payload", {}).get("codeViewRepoRoute", {})
            if isinstance(route, dict) and isinstance(route.get("tree"), dict):
                return route
        except (ValueError, AttributeError, TypeError):
            continue
    return None


def implementation_paths(paths):
    return [p for p in paths if Path(p).suffix.lower() in SOURCE_SUFFIXES
            and not set(Path(p).parts) & {"docs", "website", "assets", "third_party", "vendor", ".github"}
            and Path(p).name not in {"setup.py", "conf.py", "__init__.py"}]


def archive_implementation(url, branch):
    """Stream a bounded archive when GitHub blocks directory HTML requests."""
    address = "https://codeload.github.com/" + urlparse(url).path.strip("/") + "/tar.gz/" + quote(branch, safe="")
    started = time.monotonic()
    class LimitedReader:
        def __init__(self, raw):
            self.raw = raw
            self.total = 0
        def read(self, size=-1):
            if self.total > 32 * 1024 * 1024 or time.monotonic() - started > 25:
                raise OSError("Archive inspection budget exceeded")
            data = self.raw.read(min(size if size >= 0 else 65536, 65536))
            self.total += len(data)
            return data
    try:
        with requests.get(address, timeout=15, stream=True, headers={"User-Agent": "Awesome-Humanoid-Robot-Learning/2.0"}) as response:
            response.raise_for_status()
            with tarfile.open(fileobj=LimitedReader(response.raw), mode="r|gz") as archive:
                for entry in archive:
                    path = entry.name.partition("/")[2]
                    if entry.isfile() and entry.size and implementation_paths([path]):
                        return [path]
                    if time.monotonic() - started > 25:
                        break
    except (requests.RequestException, tarfile.TarError, OSError):
        pass
    return []


def inspect_git_repository(url):
    """Read a shallow, blobless clone and README; never check out or run code."""
    if urlparse(url).hostname != "github.com" or not repository_url(url):
        return None
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
    try:
        with tempfile.TemporaryDirectory(prefix="humanoid-code-tree-") as directory:
            subprocess.run(["git", "-c", "credential.helper=", "clone", "--filter=blob:none", "--depth=1", "--no-checkout", url, directory], env=env, capture_output=True, check=True, timeout=45)
            listing = subprocess.run(["git", "-C", directory, "ls-tree", "-r", "HEAD"], env=env, capture_output=True, text=True, check=True, timeout=10).stdout
            paths = [line.split("\t", 1)[1] for line in listing.splitlines() if " blob " in line and "\t" in line]
            source = implementation_paths(paths)
            readme_path = next((p for p in paths if p.lower() in {"readme.md", "readme.rst", "readme"}), None)
            readme = ""
            if readme_path:
                readme = subprocess.run(["git", "-c", "credential.helper=", "-C", directory, "show", "HEAD:" + readme_path], env=env, capture_output=True, text=True, errors="replace", check=True, timeout=20).stdout
            pending = PENDING.search(readme) or PARTIAL.search(readme)
            evidence = ["Inspected Git default-branch file tree and README (no checkout/execution): " + url]
            if pending:
                evidence.append("README: " + pending.group(0))
            if source:
                evidence += [f"Detected {len(source)} implementation files; examples: " + ", ".join(source[:5]), "Completeness and reproducibility have not been verified"]
                return ("partial" if pending else "available"), evidence
            if " commit " in listing:
                return "unknown", evidence + ["Repository contains submodules whose code was not inspected"]
            return ("coming_soon" if pending else "empty"), evidence + ["No implementation files detected in default-branch tree"]
    except (subprocess.SubprocessError, OSError):
        return None


def inspect_repository_page(url):
    """Use public HTML when anonymous API quota is exhausted; never infer absent
    implementation from an incomplete directory traversal.
    """
    response = fetch_text(url)
    route = github_tree(response.text)
    if not route:
        if "This repository is empty." in response.text:
            return "empty", ["Public GitHub page reports an empty repository: " + response.url]
        return "unknown", ["Public repository page has no readable file tree: " + response.url]
    article = re.search(r'<article[^>]*>(.*?)</article>', response.text, re.S)
    parser = PageParser()
    parser.feed(article.group(1) if article else "")
    readme = " ".join(parser.text)
    pending = PENDING.search(readme) or PARTIAL.search(readme)
    branch = route.get("refInfo", {}).get("name", "HEAD")
    queue = [route]
    paths = []
    visited = 0
    incomplete = False
    while queue and visited < 7:
        node = queue.pop(0)
        items = node["tree"].get("items", [])
        if node["tree"].get("totalCount", len(items)) > len(items):
            incomplete = True
        paths.extend(item["path"] for item in items if item.get("contentType") == "file")
        if implementation_paths(paths):
            break
        for item in items:
            if item.get("contentType") != "directory":
                if item.get("contentType") in {"submodule", "symlink"}:
                    incomplete = True
                continue
            if item["name"].lower() in {"docs", "website", "assets", "third_party", "vendor", ".github", "images", "static", "media"}:
                continue
            if visited >= 6:
                incomplete = True
                break
            visited += 1
            try:
                child = fetch_text(response.url.rstrip("/") + "/tree/" + quote(branch, safe="") + "/" + quote(item["path"]))
                subtree = github_tree(child.text)
                if subtree:
                    queue.append(subtree)
                else:
                    incomplete = True
            except requests.RequestException:
                incomplete = True
    source = implementation_paths(paths)
    if not source and (incomplete or queue):
        git_result = inspect_git_repository(response.url)
        if git_result:
            return git_result
        source = archive_implementation(response.url, branch)
    evidence = ["Inspected public GitHub page: " + response.url]
    if pending:
        evidence.append("README: " + pending.group(0))
        if source:
            return "partial", evidence + ["Implementation examples: " + ", ".join(source[:5])]
        if not incomplete and not queue:
            return "coming_soon", evidence
        return "unknown", evidence + ["Release announcement found, but implementation directories could not be fully inspected"]
    if source:
        return "available", evidence + ["Implementation examples: " + ", ".join(source[:5]), "Completeness and reproducibility have not been verified"]
    if incomplete or queue:
        return "unknown", evidence + ["Directory traversal incomplete; no conclusion about code absence"]
    return "empty", evidence + ["Inspected repository contains no detected implementation files"]


def inspect_repository(url):
    """Return status/evidence using README and recursive default-branch tree."""
    if urlparse(url).hostname != "github.com":
        return "unknown", ["Repository host is not yet supported for content inspection"]
    global _API_UNAVAILABLE
    if _API_UNAVAILABLE:
        try:
            return inspect_repository_page(url)
        except (requests.RequestException, ValueError, KeyError, TypeError) as exc:
            status = getattr(getattr(exc, "response", None), "status_code", None)
            return "unknown", [f"Public GitHub inspection failed ({status or type(exc).__name__}): {url}"]
    api = "https://api.github.com/repos/" + urlparse(url).path.strip("/")
    try:
        repo = fetch_text(api, api=True).json()
        if repo.get("size") == 0:
            return "empty", ["GitHub reports an empty repository"]
        tree = fetch_text(api + "/git/trees/" + quote(repo["default_branch"], safe="") + "?recursive=1", api=True).json()
        if tree.get("truncated"):
            return "unknown", ["GitHub file tree is truncated; review required"]
        try:
            readme_data = fetch_text(api + "/readme", api=True).json()
            readme = base64.b64decode(readme_data["content"]).decode("utf-8", errors="replace")
        except requests.HTTPError as exc:
            if exc.response.status_code != 404:
                raise
            readme = ""
        paths = [item["path"] for item in tree["tree"] if item["type"] == "blob" and item.get("size", 0) > 0]
        source = [p for p in paths if Path(p).suffix.lower() in SOURCE_SUFFIXES
                  and not set(Path(p).parts) & {"docs", "website", "assets", "third_party", "vendor", ".github"}
                  and Path(p).name not in {"setup.py", "conf.py", "__init__.py"}]
        pending = PENDING.search(readme) or PARTIAL.search(readme)
        if pending:
            return ("partial" if source else "coming_soon"), ["README: " + pending.group(0), f"Detected {len(source)} source files"]
        if not source:
            if any(item["type"] == "commit" for item in tree["tree"]):
                return "unknown", ["Repository uses submodules; source contents not inspected"]
            return "empty", ["No implementation files detected (documentation/assets only); review required"]
        return "available", [f"Detected {len(source)} source files; examples: {', '.join(source[:5])}",
                             "Completeness, dependencies, training assets and reproducibility have not been verified"]
    except (requests.RequestException, ValueError, KeyError, TypeError) as exc:
        status = getattr(getattr(exc, "response", None), "status_code", None)
        if status in {403, 429}:
            _API_UNAVAILABLE = True
        try:
            return inspect_repository_page(url)
        except (requests.RequestException, ValueError, KeyError, TypeError):
            return "unknown", [f"Repository inspection failed ({status or type(exc).__name__}); API and public page unavailable"]


def audit_paper(paper, config):
    paper.open_source = False
    paper.code_status = "unknown"
    paper.code_evidence = []
    paper.code_checked_at = datetime.now(timezone.utc).isoformat()
    if paper.project_url:
        cleaned = extract_urls(paper.project_url)
        if cleaned:
            paper.project_url = cleaned[0]
    text = paper.abstract + "\n" + paper.comments
    candidates = project_candidates(paper.abstract) + project_candidates(paper.comments, comments=True)
    # Also inspect old records and Comments omitted from imported/API metadata.
    discovery_failed = False
    if paper.arxiv_id not in config.get("arxiv_metadata_ids", set()) and (not paper.comments or not candidates):
        html = fetch_arxiv_abstract_page(paper.arxiv_id)
        if html:
            page = PageParser(scoped=True)
            page.feed(html)
            comments_page = PageParser(scoped=True, comments_only=True)
            comments_page.feed(html)
            paper.comments = " ".join(comments_page.text).strip()
            candidates += project_candidates(paper.comments, comments=True)
            if not page.text:
                discovery_failed = True
            text += "\n" + " ".join(page.text)
            candidates += project_candidates(text)
            candidates += [urljoin(paper.paper_url, u) for u, _ in page.links
                           if urlparse(urljoin(paper.paper_url, u)).scheme in {"http", "https"}]
        else:
            discovery_failed = True
    candidates = list(dict.fromkeys(candidates))
    if paper.project_url:
        candidates.insert(0, paper.project_url)
    project = next((u for u in candidates if not repository_url(u) and not is_generic_platform_url(u)), None)
    repos = list(dict.fromkeys(repository_url(u) for u in candidates if repository_url(u)))
    if paper.repository_url and paper.repository_url not in repos:
        repos.append(paper.repository_url)
    direct_repos = list({u.lower(): u for u in repos if urlparse(u).hostname == "github.com"}.values())
    if project:
        paper.project_url = project
        try:
            response = fetch_project_page(project)
            paper.project_url = response.url
            page = PageParser()
            page.feed(response.text)
            if len(" ".join(page.text).strip()) < 40 and not page.links:
                discovery_failed = True
                paper.code_evidence.append("Project page has insufficient readable content; may require JavaScript")
            text += "\n" + " ".join(page.text)
            for href, label in page.links:
                repo = repository_url(urljoin(response.url, href))
                if not label.strip() and repo:
                    label = "Code"
                # Ignore template/credit and unrelated publication links.
                if repo and re.search(r"\b(code|github|source|repository)\b", label, re.I) and not re.search(r"template|credit|website", label, re.I):
                    repos.append(repo)
        except requests.RequestException as exc:
            paper.code_evidence.append(f"Project page inspection failed: {type(exc).__name__}")
            discovery_failed = True
    repos = list({u.lower(): u for u in repos}.values())
    github_repos = [u for u in repos if urlparse(u).hostname == "github.com"]
    if github_repos:
        repos = github_repos
    if len(direct_repos) == 1 and len(repos) > 1:
        paper.code_evidence.append("Selected repository explicitly linked in paper metadata; other project-page links may be related work: " + direct_repos[0])
        repos = direct_repos
    if len(repos) == 1:
        paper.repository_url = repos[0]
        if paper.project_url and repository_url(paper.project_url):
            paper.project_url = None
        paper.code_status, evidence = inspect_repository(repos[0])
        paper.code_evidence.extend(evidence)
        if paper.code_status == "empty" and PENDING.search(text):
            paper.code_status = "coming_soon"
            paper.code_evidence.append("Publication/project page: " + PENDING.search(text).group(0))
    elif len(repos) > 1:
        paper.code_evidence.append("Multiple repository candidates require review: " + ", ".join(repos))
    elif PENDING.search(text):
        paper.code_status = "coming_soon"
        paper.code_evidence.append("Publication/project page: " + PENDING.search(text).group(0))
    elif not discovery_failed:
        paper.code_status = "no_repository" if project else "not_found"
        paper.code_evidence.append("No repository link found in inspected publication/project content")
    else:
        paper.code_evidence.append("Link discovery incomplete; absence of code cannot be confirmed")
    paper.open_source = paper.code_status == "available"
    return paper


def detect_project_links(papers: list[Paper], config: Optional[dict] = None):
    config = config or load_config()
    for paper in papers:
        audit_paper(paper, config)
        logger.info("%s: %s", paper.arxiv_id, paper.code_status)
    return papers


if __name__ == "__main__":
    import argparse
    from fetch_arxiv import load_existing_papers, save_papers
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=0, help="Audit at most N records (oldest check first)")
    parser.add_argument("--arxiv-id", action="append", help="Audit selected paper IDs")
    parser.add_argument("--save", action="store_true", help="Save results, report and regenerate Markdown")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    papers = list(load_existing_papers().values())
    selected = [p for p in papers if not args.arxiv_id or p.arxiv_id in args.arxiv_id]
    selected.sort(key=lambda p: p.code_checked_at or "")
    detect_project_links(selected[:args.limit] if args.limit else selected)
    if args.save:
        from generate_markdown import generate_all
        save_papers(papers)
        generate_all(papers)
