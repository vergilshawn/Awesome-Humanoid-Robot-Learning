# Awesome-Humanoid-Robot-Learning

A modern static academic navigation website for humanoid robot learning research. Automatically collects, organizes, classifies, and presents newly released humanoid robotics papers from arXiv.

**Live site:** [https://<username>.github.io/Awesome-Humanoid-Robot-Learning/](https://<username>.github.io/Awesome-Humanoid-Robot-Learning/)

## Features

- Daily automatic paper fetching from arXiv
- Wider arXiv search with category and humanoid-topic queries
- Multi-label tagging with single best-category directory placement
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

# Update recent papers with daily arXiv windows
python scripts/update_daily.py --days 7

# Preview the website
npm run docs:dev
```

## How It Works

1. **fetch_arxiv.py** — Fetches new papers from arXiv categories and configured humanoid-topic queries
2. **semantic_filter.py** — Filters papers by relevance to humanoid robotics
3. **classify_papers.py** — Multi-label classification into research categories
4. **detect_project_links.py** — Detects GitHub/HuggingFace project pages
5. **detect_real_robot.py** — Detects papers with real robot experiments
6. **generate_markdown.py** — Generates structured markdown pages
7. **generate_vitepress.py** — Generates VitePress config, sidebar, and navbar
8. **update_repo.py** — Orchestrates the full pipeline
9. **update_current_month.py** — Fetches only the current month and replaces only that month in the generated dataset
10. **update_daily.py** — Fetches one day or a day range with small arXiv windows, then replaces only those days

## Updating Without Hitting arXiv Limits

Prefer daily windows for high-recall routine updates:

```bash
python scripts/update_daily.py --days 7
```

This splits the update into one-day `submittedDate` windows. It reduces arXiv result truncation, makes each request smaller, and lets the project run more frequently without re-scanning the whole month.

Use the monthly updater when you want to refresh a complete month:

```bash
python scripts/update_current_month.py
```

It queries arXiv with a `submittedDate` range for the current month, waits longer between requests, and aborts without writing files if any configured query fails. To refresh a specific month:

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
