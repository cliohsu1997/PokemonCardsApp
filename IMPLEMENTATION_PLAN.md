
# Implementation plan — Pokémon card app + SQL (+ AWS later)

Single source of truth for phases and status. Update this file first when phases change, then sync `progress/latest.md` and task files.

---

## Phase 1 — Project skeleton and workflow

**Status:** Complete

- Align repo with `.cursor/rules/project-workflow.mdc` (folders, tracking docs).
- Keep `streamlit_app.py` as the starting UI reference; Poetry layout under `python/` (`pyproject.toml`, `poetry.toml`, in-project `.venv`, `code/`, `test/`).
- **Scrape pilot tests:** `python/test/scrape/test_pilot_pricecharting_scrape.py` — real `scrape_pricecharting_data()` against PriceCharting with `max_sets` capped (`poetry run pytest test/scrape/test_pilot_pricecharting_scrape.py -v` from `python/`).

---

## Phase 2 — Local SQL schema (SQLite)

**Status:** Not started

**Goal:** Practice **DDL** and lock down a relational model before changing the app.

- Choose **SQLite** as the local engine (single file, e.g. under **`data/`** — path documented in `structure/latest.md`).
- Design tables that mirror today’s concepts: **sets**, **cards** (or card identity per set), **price snapshots** (dated rows: ungraded, grade 9, PSA 10, optional image URL, derived fields if stored vs computed).
- Add indexes / constraints appropriate for lookups (`JOIN`, filter by set, date ranges).
- Check in **schema SQL** (e.g. `data/schema.sql` or `python/code/sql/schema.sql`) and optional seed scripts.
- **Practice:** `CREATE TABLE`, `PRIMARY KEY`, `FOREIGN KEY`, basic `INSERT` / `SELECT` from CLI or small scripts (`poetry run python …`).

---

## Phase 3 — Replicate upstream process → SQL (ingest)

**Status:** Not started

**Goal:** Same **logical pipeline** as `streamlit_app.py` (scrape PriceCharting → normalize → sealed-product filter → numeric prices → deal metrics), but **persist into SQLite** instead of local CSV history (`data/pokemon_price_history.csv` today).

- Implement ingest in **`python/code/`** (functions reused later by Streamlit): scrape or import bridge → **transactions** / bulk insert → idempotent rules for “same day refresh” (align with current “don’t duplicate today” behavior).
- Optionally keep a **one-shot CSV → SQL loader** to replay data without scraping.
- **Practice:** `INSERT`, `UPDATE`, `DELETE`, dedupe patterns, simple migrations when schema evolves.

---

## Phase 4 — Streamlit backed by local SQLite

**Status:** Not started

**Goal:** Run the app against **local DB** for testing; defer AWS until Phase 6.

- Introduce a thin **data access layer** (functions or small module) used by Streamlit: load latest snapshot, append refresh, read history for charts.
- Route **refresh**, **filters**, and **downloads** through SQL (or SQL → pandas only at the edge — whichever matches learning goals).
- **No Google Cloud** in this repo; cloud storage is **Phase 6** (e.g. S3 / RDS) only.
- **Practice:** parameterized queries, avoiding string-built SQL where unsafe.

---

## Phase 5 — SQL analytics parity

**Status:** Not started

**Goal:** Match current analytics (rolling **3 / 7 / 14 / 30** day ungraded changes, aggregates for charts) using **SQL** where instructive.

- Implement rolling / comparison logic with **`JOIN`s**, **aggregates**, **window functions** (SQLite 3.25+), or staged tables — document tradeoffs in task notes.
- Sidebar filters reflected as **`WHERE`** / **`HAVING`** patterns; chart data from **`GROUP BY`** queries.
- **Practice:** multi-step queries, views or CTEs, explaining execution order in comments or small docs.

---

## Phase 6 — AWS storage (later)

**Status:** Not started

**Goal:** Move off **local-only** persistence while keeping the same **relational** shape.

- **Database:** e.g. **Amazon RDS** (PostgreSQL or MySQL) — migrate schema with compatible SQL or Alembic/`sqlite3` export → RDS load.
- **Object storage (optional):** **Amazon S3** for CSV exports, backups, or cold archives — align with any existing “download history” behavior.
- Configuration via **environment variables / secrets** (no keys in repo); document deploy/runbook in `structure/latest.md` or README when started.
- Keep **SQLite** as local dev fallback where useful.

---

## Phase 7 — Polish

**Status:** Not started

- Remove unused imports / dead code paths (e.g. LangChain/HF if still unused).
- Root **`README.md`** for learners: how to run SQLite, sample queries, Streamlit + Poetry.
- Optional: **`requirements.txt`** snapshot for non-Poetry users.

---

## Dependency note

Phases **2 → 5** are intentionally **local SQLite** so you can practice SQL without AWS cost or networking. **Phase 6** introduces AWS when you are ready.
