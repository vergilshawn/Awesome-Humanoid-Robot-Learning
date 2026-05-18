# Awesome-Humanoid-Robot-Learning

A modern static academic navigation website for humanoid robot learning research. Automatically collects, organizes, classifies, and presents newly released humanoid robotics papers from arXiv.

**Live site:** [https://<username>.github.io/Awesome-Humanoid-Robot-Learning/](https://<username>.github.io/Awesome-Humanoid-Robot-Learning/)

## Features

- Daily automatic paper fetching from arXiv
- Multi-label classification across 11 humanoid robotics categories
- Full-text search via VitePress
- Real robot experiment detection
- Open-source code detection
- Tag-based filtering
- Month-based paper organization
- Clean, modern academic UI with dark mode

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt
npm install

# Run the full pipeline
python scripts/update_repo.py

# Update only the current month (lighter on arXiv API limits)
python scripts/update_current_month.py

# Preview the website
npm run docs:dev
```

## How It Works

1. **fetch_arxiv.py** — Fetches new papers from arXiv (cs.RO, cs.AI, cs.LG, cs.CV, eess.SY)
2. **semantic_filter.py** — Filters papers by relevance to humanoid robotics
3. **classify_papers.py** — Multi-label classification into research categories
4. **detect_project_links.py** — Detects GitHub/HuggingFace project pages
5. **detect_real_robot.py** — Detects papers with real robot experiments
6. **generate_markdown.py** — Generates structured markdown pages
7. **generate_vitepress.py** — Generates VitePress config, sidebar, and navbar
8. **update_repo.py** — Orchestrates the full pipeline
9. **update_current_month.py** — Fetches only the current month and replaces only that month in the generated dataset

## Updating Without Hitting arXiv Limits

Prefer the monthly updater for routine runs:

```bash
python scripts/update_current_month.py
```

It queries arXiv with a `submittedDate` range for the current month, waits longer between category requests, and aborts without writing files if any configured category fails. To refresh a specific month:

```bash
python scripts/update_current_month.py --month 2026-05
```

## Categories

- Loco-Manipulation and Whole-Body Control
- Manipulation
- Teleoperation
- Locomotion
- Navigation
- State Estimation
- Sim-to-Real
- Hardware Design
- Simulation Benchmark
- Physics-Based Character Animation
- Human Motion Analysis and Synthesis

## License

MIT
