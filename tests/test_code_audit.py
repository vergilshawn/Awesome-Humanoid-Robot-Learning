import base64
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from paper_model import Paper
from detect_project_links import audit_paper, inspect_repository, PageParser, repository_url
from generate_markdown import format_paper_entry


def paper(**kwargs):
    return Paper(arxiv_id="2601.00001", title="Example", paper_url="https://arxiv.org/abs/2601.00001", **kwargs)


def response(data=None, text="", url="https://example.org/Project"):
    return Mock(json=Mock(return_value=data), text=text, url=url)


class CodeAuditTests(unittest.TestCase):
    def setUp(self):
        self.api_patch = patch("detect_project_links._API_UNAVAILABLE", False)
        self.api_patch.start()
        self.addCleanup(self.api_patch.stop)

    def test_blobless_git_fallback_preserves_partial_release_evidence(self):
        from detect_project_links import inspect_git_repository
        listing = "100644 blob abc\tREADME.md\n100644 blob def\teval.py\n"
        with patch("detect_project_links.subprocess.run", side_effect=[Mock(), Mock(stdout=listing), Mock(stdout="Training code is not included")]) as run:
            status, evidence = inspect_git_repository("https://github.com/lab/robot")
        self.assertEqual(status, "partial")
        self.assertIn("--no-checkout", run.call_args_list[0].args[0])
        self.assertIn("--filter=blob:none", run.call_args_list[0].args[0])
        self.assertIn("Training code is not included", str(evidence))

    def test_archive_checks_implementation_without_extracting_files(self):
        import io
        import tarfile
        from detect_project_links import archive_implementation
        buffer = io.BytesIO()
        with tarfile.open(fileobj=buffer, mode="w:gz") as archive:
            for name in ["robot-main/src/__init__.py", "robot-main/src/train.py"]:
                entry = tarfile.TarInfo(name)
                entry.size = 10
                archive.addfile(entry, io.BytesIO(b"print(123)"))
        fake = Mock()
        fake.raw = io.BytesIO(buffer.getvalue())
        context = Mock()
        context.__enter__ = Mock(return_value=fake)
        context.__exit__ = Mock(return_value=False)
        with patch("detect_project_links.requests.get", return_value=context):
            self.assertEqual(archive_implementation("https://github.com/lab/robot", "main"), ["src/train.py"])

    def test_metadata_refresh_keeps_comments(self):
        from audit_code import refresh_metadata
        p = paper()
        xml = '<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom"><entry><id>http://arxiv.org/abs/2601.00001v2</id><summary>Abstract</summary><arxiv:comment>Project https://example.org</arxiv:comment></entry></feed>'
        with patch("audit_code.fetch_text", return_value=response(text=xml)), patch("audit_code.time.sleep"), patch("builtins.print"):
            found = refresh_metadata([p])
        self.assertEqual(found, {p.arxiv_id})
        self.assertEqual(p.comments, "Project https://example.org")

    def test_html_project_redirect_is_followed(self):
        from detect_project_links import fetch_project_page
        moved = response(text='<meta http-equiv="refresh" content="0; url=/new/">', url="https://example.org/old/")
        destination = response(text="Real project content", url="https://example.org/new/")
        with patch("detect_project_links.fetch_text", side_effect=[moved, destination]) as fetch:
            self.assertIs(fetch_project_page("https://example.org/old/"), destination)
        self.assertEqual(fetch.call_args.args[0], "https://example.org/new/")

    def test_public_page_fallback_detects_implementation(self):
        import json
        from detect_project_links import inspect_repository_page
        route = {"tree": {"items": [{"path": "train.py", "contentType": "file"}], "totalCount": 1}, "refInfo": {"name": "main"}}
        html = '<script type="application/json">' + json.dumps({"payload": {"codeViewRepoRoute": route}}) + '</script><article>Training instructions</article>'
        with patch("detect_project_links.fetch_text", return_value=response(text=html, url="https://github.com/lab/Robot")):
            status, evidence = inspect_repository_page("https://github.com/lab/Robot")
        self.assertEqual(status, "available")
        self.assertIn("train.py", str(evidence))

    def test_public_page_missing_tree_is_unknown(self):
        from detect_project_links import inspect_repository_page
        with patch("detect_project_links.fetch_text", return_value=response(text="Sign in")):
            self.assertEqual(inspect_repository_page("https://github.com/lab/Robot")[0], "unknown")

    def test_boolean_html_attributes_do_not_break_discovery(self):
        parser = PageParser()
        parser.feed('<div class><a href="https://github.com/lab/Robot" title>Code</a></div>')
        self.assertEqual(parser.links[0][0], "https://github.com/lab/Robot")

    def test_public_readme_checkboxes_preserved(self):
        parser = PageParser()
        parser.feed('<li><input type="checkbox" disabled>Release training code</li>')
        self.assertIn("[ ]", parser.text)

    def test_bare_github_and_project_domains(self):
        from detect_project_links import extract_urls
        self.assertEqual(extract_urls("Project: Lab.github.io/Robot. Code: github.com/Lab/Robot"), ["https://Lab.github.io/Robot", "https://github.com/Lab/Robot"])

    def test_latex_urls_are_not_corrupted(self):
        from detect_project_links import extract_urls
        self.assertEqual(extract_urls(r"Project \href{https://example.org/Demo/}{project website}"), ["https://example.org/Demo/"])

    def test_huggingface_dataset_retains_owner_and_name(self):
        self.assertEqual(repository_url("https://huggingface.co/datasets/lab/data"), "https://huggingface.co/datasets/lab/data")

    def test_repository_case_and_dataset_do_not_create_ambiguity(self):
        p = paper(comments="Code https://github.com/Lab/Robot and https://github.com/lab/robot and https://huggingface.co/datasets/lab/data")
        with patch("detect_project_links.inspect_repository", return_value=("available", ["Source detected"])):
            audit_paper(p, {})
        self.assertEqual(p.code_status, "available")

    def test_navigation_icon_code_link(self):
        p = paper(comments="Project https://example.org/Robot")
        html = '<nav><a href="https://github.com/lab/Robot"><img alt="Code" src="code.svg"></a></nav>'
        with patch("detect_project_links.fetch_text", return_value=response(text=html)), patch("detect_project_links.inspect_repository", return_value=("available", ["Source detected"])):
            audit_paper(p, {})
        self.assertEqual(p.repository_url, "https://github.com/lab/Robot")

    def test_legacy_link_is_not_verified_release(self):
        self.assertFalse(paper(open_source=True, project_url="https://github.com/a/b").open_source)

    def test_comments_project_page_without_repo(self):
        p = paper(comments="Project: https://example.org/MixedCase")
        with patch("detect_project_links.fetch_text", return_value=response(text="<p>Robot project: research overview, experiment results and supplementary demonstration video.</p>")) as fetch:
            audit_paper(p, {})
        fetch.assert_called_once_with("https://example.org/MixedCase")
        self.assertEqual(p.code_status, "no_repository")
        self.assertFalse(p.open_source)

    def test_arxiv_scoped_comments_excludes_footer(self):
        p = paper()
        html = '<blockquote class="abstract">Abstract</blockquote><td class="tablecell comments">Project: <a href="https://example.org/Demo">this https URL</a></td><footer><a href="https://github.com/arxiv/template">GitHub</a></footer>'
        with patch("detect_project_links.fetch_arxiv_abstract_page", return_value=html), patch("detect_project_links.fetch_text", return_value=response(text="Code coming soon", url="https://example.org/Demo")):
            audit_paper(p, {})
        self.assertEqual(p.project_url, "https://example.org/Demo")
        self.assertEqual(p.code_status, "coming_soon")
        self.assertIsNone(p.repository_url)

    def test_project_relative_code_link_and_template(self):
        p = paper(comments="Project https://example.org/Demo")
        html = '<a href="https://github.com/lab/Robot/tree/main">Code</a><footer><a href="https://github.com/other/template">GitHub</a></footer>'
        with patch("detect_project_links.fetch_text", return_value=response(text=html)), patch("detect_project_links.inspect_repository", return_value=("partial", ["Training code coming soon"])):
            audit_paper(p, {})
        self.assertEqual(p.repository_url, "https://github.com/lab/Robot")
        self.assertEqual(p.code_status, "partial")
        self.assertFalse(p.open_source)

    def inspect(self, files, readme="", truncated=False):
        values = [response({"default_branch": "main", "size": 10}), response({"tree": [{"path": p, "type": "blob", "size": 100} for p in files], "truncated": truncated}), response({"content": base64.b64encode(readme.encode()).decode()})]
        with patch("detect_project_links.fetch_text", side_effect=values):
            return inspect_repository("https://github.com/lab/Robot")

    def test_repository_states(self):
        for files, readme, expected in [
            (["README.md"], "Code coming soon", "coming_soon"),
            (["README.md", "assets/main.js"], "", "empty"),
            (["eval.py"], "Training code will be released soon", "partial"),
            (["src/train.py", "README.md"], "", "available"),
            (["setup.py", "docs/conf.py"], "", "empty"),
        ]:
            with self.subTest(expected=expected):
                self.assertEqual(self.inspect(files, readme)[0], expected)

    def test_depending_does_not_mean_release_pending(self):
        self.assertEqual(self.inspect(["train.py"], "Implementation can change depending on the task")[0], "available")

    def test_truncated_tree_unknown(self):
        self.assertEqual(self.inspect(["train.py"], truncated=True)[0], "unknown")

    def test_network_error_clears_stale_flag(self):
        import requests
        p = paper(project_url="https://example.org/Demo", code_status="available")
        with patch("detect_project_links.fetch_arxiv_abstract_page", return_value=None), patch("detect_project_links.fetch_text", side_effect=requests.Timeout):
            audit_paper(p, {})
        self.assertEqual(p.code_status, "unknown")
        self.assertFalse(p.open_source)

    def test_rate_limit_unknown(self):
        import requests
        with patch("detect_project_links.fetch_text", side_effect=requests.HTTPError(response=Mock(status_code=403))):
            status, evidence = inspect_repository("https://github.com/lab/Robot")
        self.assertEqual(status, "unknown")
        self.assertIn("403", evidence[0])

    def test_bare_comments_url(self):
        p = paper(comments="https://example.org/Robot")
        with patch("detect_project_links.fetch_text", return_value=response(text="Project video and research overview with supplementary experiment results.", url="https://example.org/Robot")):
            audit_paper(p, {})
        self.assertEqual(p.project_url, "https://example.org/Robot")
        self.assertEqual(p.code_status, "no_repository")

    def test_ambiguous_repositories_require_review(self):
        p = paper(comments="Code: https://github.com/lab/one https://github.com/lab/two")
        audit_paper(p, {})
        self.assertEqual(p.code_status, "unknown")
        self.assertIn("Multiple", p.code_evidence[0])

    def test_project_coming_soon_with_placeholder_repo(self):
        p = paper(comments="Project https://example.org/Demo")
        html = '<p>Code coming soon</p><a href="https://github.com/lab/Robot">Code</a>'
        with patch("detect_project_links.fetch_text", return_value=response(text=html)), patch("detect_project_links.inspect_repository", return_value=("empty", ["Empty repository"])):
            audit_paper(p, {})
        self.assertEqual(p.code_status, "coming_soon")

    def test_empty_github_repository(self):
        with patch("detect_project_links.fetch_text", return_value=response({"size": 0})):
            self.assertEqual(inspect_repository("https://github.com/lab/empty")[0], "empty")

    def test_unchecked_release_checklist(self):
        self.assertEqual(self.inspect(["eval.py"], "- [ ] Release training code")[0], "partial")

    def test_unsupported_host_is_not_verified(self):
        self.assertEqual(inspect_repository("https://gitlab.com/lab/Robot")[0], "unknown")

    def test_daily_merge_refreshes_status_without_losing_classification(self):
        from update_daily import merge_papers
        old = paper(abstract="Original abstract", primary_category="Locomotion", code_status="coming_soon")
        new = paper(comments="Code released", code_status="available", code_checked_at="2026-11-13T00:00:00+00:00", repository_url="https://github.com/lab/Robot")
        result = merge_papers({old.arxiv_id: old}, [new])[0]
        self.assertEqual(result.primary_category, "Locomotion")
        self.assertEqual(result.code_status, "available")
        self.assertTrue(result.open_source)
        self.assertEqual(result.comments, "Code released")

    def test_host_validation_and_case(self):
        self.assertIsNone(repository_url("https://github.com.evil.test/lab/repo"))
        self.assertIsNone(repository_url("https://github.com/lab"))
        self.assertEqual(repository_url("https://github.com/Lab/Robot.git/tree/main"), "https://github.com/Lab/Robot")

    def test_render_separates_project_and_repository(self):
        output = format_paper_entry(paper(project_url="https://example.org", repository_url="https://github.com/lab/Robot", code_status="partial"))
        self.assertIn("Project page", output)
        self.assertIn("**Repository:**", output)
        self.assertIn("Partial release", output)
        self.assertNotIn("🌟", output)


if __name__ == "__main__":
    unittest.main()
