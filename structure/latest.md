# Project structure (latest)

High-level layout only. Update when folders or primary files change.

## Root

| Path | Purpose |
|------|---------|
| `streamlit_app.py` | Streamlit UI: scraping, filters, charts (starting point for SQL integration). |
| `IMPLEMENTATION_PLAN.md` | Phase plan and status (authoritative). |
| `.cursor/` | **Rules:** `project-workflow.mdc`, `agent-permissions.mdc`. **Skills:** `task-management-workflow`, `agent-permissions`, `python` (Poetry-only runs). See `skills/README.md`. |
| `data/` | Empty placeholder for datasets and imports (tracked via `.gitkeep`). |
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
| `python/test/` | `pytest` (`poetry run pytest test\ -v`). |

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
