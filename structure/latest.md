# Project structure (latest)

High-level layout only. Update when folders or primary files change.

## Root

| Path | Purpose |
|------|---------|
| `streamlit_app.py` | Streamlit UI: scraping, filters, charts (starting point for SQL integration). |
| `IMPLEMENTATION_PLAN.md` | Phase plan and status (authoritative). |
| `.cursor/` | **Rules** (`rules/*.mdc`): `project-workflow.mdc`, `agent-permissions.mdc`. **Skills** (`skills/`): optional `SKILL.md` subfolders only; LaTeX/CV skills were removed; see `skills/README.md`. |
| `data/` | Empty placeholder for datasets and imports (tracked via `.gitkeep`). |
| `debug/` | Empty placeholder for debug logs or scratch outputs (`.gitkeep`). |
| `output/` | Empty placeholder for exports, reports, and generated files (`.gitkeep`). |

## Python (Poetry)

Same pattern as `sports-card-automation/python`: dependency lock and venv are managed from **`python/`** only.

| Path | Purpose |
|------|---------|
| `python/pyproject.toml` | Poetry project metadata and runtime + dev dependencies. |
| `python/poetry.lock` | Locked versions (commit this file). |
| `python/README.md` | `poetry install` and `poetry run streamlit run ..\streamlit_app.py`. |
| `python/tests/` | Placeholder for `pytest` (see `python/README.md`). |

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
