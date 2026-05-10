# Project structure (latest)

High-level layout only. Update when folders or primary files change.

## Root

| Path | Purpose |
|------|---------|
| `streamlit_app.py` | Streamlit UI: scraping, filters, charts (starting point for SQL integration). |
| `IMPLEMENTATION_PLAN.md` | Phase plan and status (authoritative). |
| `docs/BEGINNER_SQL_GUIDE.md` | Concept map: SQL vs SQLite, `.sql` / `.db` / CSV, tools (`sqlite3.exe`, Python `sqlite3`). |
| `BEGINNER_SQL_GUIDE.html` | Same guide as static HTML — open in a browser from the repo root for easier reading. |
| `.cursor/` | **Rules:** `project-workflow.mdc`, `agent-permissions.mdc`. **Skills:** `task-management-workflow`, `agent-permissions`, `python` (Poetry-only runs). See `skills/README.md`. |
| `data/` | `.gitkeep` placeholder; Streamlit writes **`latest_pokemon_prices.csv`** and **`pokemon_price_history.csv`** here when scraping (local-only; not committed by default if ignored). Future SQLite schema file possible per **`IMPLEMENTATION_PLAN.md`**. |
| `debug/` | Empty placeholder for debug logs or scratch outputs (`.gitkeep`). |
| `output/` | Empty placeholder for exports, reports, and generated files (`.gitkeep`). |

## Python (Poetry)

All Python commands for this app use **`poetry run`** from **`python/`** (see `.cursor/skills/python/SKILL.md`).

| Path | Purpose |
|------|---------|
| `python/pyproject.toml` | Dependencies and project metadata. |
| `python/poetry.lock` | Locked versions (commit). |
| `python/poetry.toml` | **`virtualenvs.in-project = true`** → env at **`python/.venv/`** (gitignored). |
| `python/README.md` | Setup and `poetry run` commands. |
| `python/.venv/` | Poetry-created virtualenv (**not** committed). |
| `python/code/` | Application scripts. |
| `python/code/scrape/` | PriceCharting scrape (`constants`, `pricecharting`, `__init__`). |
| `python/test/` | `pytest` (`poetry run pytest test\ -v`); includes **`test_pilot_pricecharting_scrape.py`** for scrape pilots. |

## Workflow and tracking (per `project-workflow.mdc`)

| Path | Purpose |
|------|---------|
| `conversation_cursor/YYYYMM/YYYYMMDD/` | Task proposals and design notes. |
| `to-do/YYYYMM/YYYYMMDD/` | Active checklists per task. |
| `task_summary/YYYYMM/YYYYMMDD/` | Task objectives, results, and status. |
| `progress/latest.md` | Active and completed tasks at a glance. |
| `structure/latest.md` | This file: repo layout and file roles. |

## Remotes

| Remote | Target |
|--------|--------|
| `origin` | User GitHub repository (main push target). |
| `upstream` | Original Logan142414/PokemonCardsApp (optional pulls). |
