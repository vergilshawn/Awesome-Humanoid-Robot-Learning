"""Generate VitePress configuration, sidebar, and navbar."""

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
VITEPRESS_DIR = PROJECT_ROOT / "docs" / ".vitepress"

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


def generate_sidebar(papers: list[Paper]) -> list[dict]:
    """Generate sidebar configuration based on available papers and months."""
    # Group papers by category, then by month
    cat_papers = defaultdict(list)
    for p in papers:
        for c in p.categories:
            cat_papers[c].append(p)

    sidebar = [
        {
            "text": "Overview",
            "items": [
                {"text": "Home", "link": "/"},
                {"text": "Latest Papers", "link": "/latest"},
                {"text": "Real Robot", "link": "/real-robot"},
                {"text": "Open Source", "link": "/open-source"},
                {"text": "Tags", "link": "/tags"},
            ],
        }
    ]

    for cat_name, cat_key in CATEGORY_KEY_MAP.items():
        cp_list = cat_papers.get(cat_name, [])
        months = defaultdict(list)
        for p in cp_list:
            if p.published:
                months[p.published].append(p)

        if not months:
            continue

        month_items = []
        for month in sorted(months.keys(), reverse=True):
            month_items.append({
                "text": month,
                "link": f"/{cat_key}/{month}",
            })

        sidebar.append({
            "text": f"{cat_name} ({len(cp_list)})",
            "collapsed": True,
            "items": [
                {"text": "Overview", "link": f"/{cat_key}/"},
            ] + month_items,
        })

    return sidebar


def generate_config(papers: Optional[list[Paper]] = None) -> str:
    """Generate VitePress config.mjs content."""
    if papers is None:
        papers = load_papers()

    sidebar = generate_sidebar(papers)

    sidebar_json = json.dumps(sidebar, indent=6)

    config = f'''import {{ defineConfig }} from "vitepress";

export default defineConfig({{
  title: "Awesome-Humanoid-Robot-Learning",
  description: "A curated collection of humanoid robot learning research papers",
  base: "/",
  lang: "en-US",
  cleanUrls: true,
  ignoreDeadLinks: true,

  head: [
    ["link", {{ rel: "icon", href: "/Awesome-Humanoid-Robot-Learning/favicon.ico" }}],
  ],

  themeConfig: {{
    nav: [
      {{ text: "Home", link: "/" }},
      {{ text: "Latest", link: "/latest" }},
      {{ text: "Real Robot", link: "/real-robot" }},
      {{ text: "Open Source", link: "/open-source" }},
      {{ text: "Tags", link: "/tags" }},
    ],

    sidebar: {sidebar_json},

    socialLinks: [
      {{ icon: "github", link: "https://github.com" }},
    ],

    search: {{
      provider: "local",
      options: {{
        miniSearch: {{
          options: {{
            boostDocument: (id, term, storedFields) => {{
              // Boost titles over content
              if (storedFields.titles?.some(t => t.toLowerCase().includes(term.toLowerCase()))) {{
                return 3;
              }}
              return 1;
            }},
          }},
        }},
      }},
    }},

    footer: {{
      message: "Automatically updated daily from arXiv",
      copyright: "MIT License",
    }},

    outline: {{
      level: [2, 3],
      label: "On this page",
    }},

    docFooter: {{
      prev: "Previous",
      next: "Next",
    }},
  }},

  markdown: {{
    theme: "github-light",
    lineNumbers: false,
  }},

  appearance: {{
    initialValue: "dark",
  }},
}});
'''

    out_path = VITEPRESS_DIR / "config.mjs"
    out_path.write_text(config, encoding="utf-8")
    logger.info(f"Generated {out_path}")
    return config


def generate_theme_css() -> None:
    """Generate custom theme CSS for academic styling."""
    css = '''/* Custom theme for Awesome-Humanoid-Robot-Learning */
:root {
  --vp-font-family-base: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --vp-font-family-mono: "JetBrains Mono", "Fira Code", monospace;
  --vp-c-brand-1: #2563eb;
  --vp-c-brand-2: #3b82f6;
  --vp-c-brand-3: #60a5fa;
  --vp-c-text-1: #1e293b;
  --vp-c-text-2: #475569;
  --vp-c-bg: #ffffff;
  --vp-c-bg-alt: #f8fafc;
  --vp-c-bg-elv: #ffffff;
  --vp-c-border: #e2e8f0;
}

.dark {
  --vp-c-brand-1: #60a5fa;
  --vp-c-brand-2: #3b82f6;
  --vp-c-brand-3: #2563eb;
  --vp-c-text-1: #f1f5f9;
  --vp-c-text-2: #94a3b8;
  --vp-c-bg: #0f172a;
  --vp-c-bg-alt: #1e293b;
  --vp-c-bg-elv: #1e293b;
  --vp-c-border: #334155;
}

/* Paper entry styling */
h2 {
  font-size: 1.25rem !important;
  font-weight: 600 !important;
  margin-top: 2rem !important;
  padding-top: 1rem !important;
  border-top: 1px solid var(--vp-c-border) !important;
}

h2:first-of-type {
  border-top: none !important;
}

.VPDoc h2 a {
  color: var(--vp-c-text-1);
}

/* Tag styling */
.tag {
  display: inline-block;
  padding: 0.1rem 0.5rem;
  margin: 0.15rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  background: var(--vp-c-bg-alt);
  border: 1px solid var(--vp-c-border);
  color: var(--vp-c-text-2);
}

/* Statistics cards */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0;
}

.stat-card {
  padding: 1rem;
  border-radius: 0.5rem;
  background: var(--vp-c-bg-alt);
  border: 1px solid var(--vp-c-border);
  text-align: center;
}

.stat-card .number {
  font-size: 2rem;
  font-weight: 700;
  color: var(--vp-c-brand-1);
}

.stat-card .label {
  font-size: 0.875rem;
  color: var(--vp-c-text-2);
}

/* Improve readability */
.VPDoc {
  max-width: 800px !important;
}

@media (min-width: 1440px) {
  .VPDoc {
    max-width: 900px !important;
  }
}
'''

    VITEPRESS_DIR.mkdir(parents=True, exist_ok=True)
    theme_dir = VITEPRESS_DIR / "theme"
    theme_dir.mkdir(parents=True, exist_ok=True)
    (theme_dir / "custom.css").write_text(css, encoding="utf-8")
    logger.info(f"Generated {theme_dir / 'custom.css'}")


def generate_theme_index() -> None:
    """Generate theme index to import custom CSS."""
    ts_content = '''import DefaultTheme from "vitepress/theme";
import "./custom.css";

export default DefaultTheme;
'''
    theme_dir = VITEPRESS_DIR / "theme"
    theme_dir.mkdir(parents=True, exist_ok=True)
    (theme_dir / "index.ts").write_text(ts_content, encoding="utf-8")
    logger.info(f"Generated {theme_dir / 'index.ts'}")


def generate_all(papers: Optional[list[Paper]] = None) -> None:
    """Generate all VitePress configuration files."""
    if papers is None:
        papers = load_papers()

    VITEPRESS_DIR.mkdir(parents=True, exist_ok=True)
    generate_config(papers)
    generate_theme_css()
    generate_theme_index()
    logger.info("All VitePress configuration files generated.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    generate_all()
