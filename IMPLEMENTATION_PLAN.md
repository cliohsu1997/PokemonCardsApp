
# Implementation plan — Pokémon card app + SQL

Single source of truth for phases and status. Update this file first when phases change, then sync `progress/latest.md` and task files.

## Phase 1 — Project skeleton and workflow

**Status:** Complete

- Align repo with `.cursor/rules/project-workflow.mdc` (folders, tracking docs).
- Keep `streamlit_app.py` as the starting UI; trim assets per repo cleanup.

## Phase 2 — Data model and SQLite

**Status:** Not started

- Define tables for sets, cards, and price snapshots (or equivalent).
- Load scraped or exported data into SQLite; document schema in `structure/latest.md`.

## Phase 3 — SQL-backed features

**Status:** Not started

- Replace or complement in-memory filters with SQL queries where it aids learning.
- Optional: historical snapshots and trend queries (`JOIN`, `GROUP BY`, window concepts).

## Phase 4 — Polish and dependencies

**Status:** In progress

- **`python/` Poetry environment** — `pyproject.toml` + `poetry.lock` aligned with upstream `requirements.txt` (including `langchain==0.0.234`). Use `poetry run` from `python/` (see `python/README.md`).
- Add root `.gitignore` for venv, caches, and local secrets (optional root `requirements.txt` for non-Poetry users).
