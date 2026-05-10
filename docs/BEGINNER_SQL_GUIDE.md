# Beginner SQL guide — files, tools, and how they fit together

This note is for **this repository** (Pokémon cards + SQLite path in `IMPLEMENTATION_PLAN.md`). It is **not** every database system in the world—others add servers, users, clusters—but the **roles** (schema, data file, engine, client) stay similar.

---

## 1. Concept map (mental positions)

Think of four **layers**:

```
┌─────────────────────────────────────────────────────────────────┐
│  YOU write SQL *text* (language)                                │
│    • in .sql files, or in Python strings, or in a GUI           │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│  DATABASE ENGINE (software program)                             │
│    • reads/writes the .db file                                  │
│    • parses SQL, checks rules, runs queries                     │
│    • SQLite: often `sqlite3.exe` (CLI) OR Python `sqlite3`     │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│  DATABASE FILE(S) on disk                                      │
│    • SQLite: usually ONE file ending in .db                    │
│    • holds tables, indexes, actual rows                         │
└─────────────────────────────────────────────────────────────────┘

Around this:
  • CSV / Excel  → interchange formats (export/import), not the engine
  • schema.sql   → human-readable *instructions* to create structure
```

**Important correction:** SQLite is **not** a “compiler” in the C/Java sense. It is a **database engine** (also called a **DBMS**): it **understands SQL**, **stores** data in a `.db` file, and **returns** results. A **compiler** turns source code into another form (e.g. `.exe`). SQLite **executes** SQL against stored data.

---

## 2. The SQL **language** vs SQLite the **product**

| Term | What it is |
|------|------------|
| **SQL** | A **language** (Structured Query Language): keywords like `SELECT`, `INSERT`, `CREATE TABLE`. It is **text**. Same ideas across many databases; **small syntax differences** exist (SQLite vs PostgreSQL vs MySQL). |
| **SQLite** | A **specific software library + tools** that implements SQL for **embedded/local** databases (one `.db` file, no separate server process required for basic use). |

You **write SQL**; **SQLite runs it** (or PostgreSQL, etc., on other projects).

---

## 3. File types you will see

| Kind | Typical extension | Purpose |
|------|-------------------|---------|
| **Schema / script** | `.sql` | **Plain text** file containing SQL statements—often `CREATE TABLE`, `CREATE INDEX`, sometimes small `INSERT` seeds. **Blueprint + optional starter rows.** Nothing runs until something **executes** this file against an engine. |
| **SQLite database** | `.db` (or `.sqlite`) | **Binary file** managed only through SQLite (or compatible tools). Holds **real tables and data**. Do not edit with Notepad. |
| **CSV** | `.csv` | **Text table** export/import. Good for Excel and pipelines; **not** where the living app database usually stays long-term in our plan. |
| **Lock file** (Poetry) | `poetry.lock` | **Not SQL**—Python dependency lock for this repo. |

There is **no requirement** that schema live only in `.sql`; you can create tables from Python instead. **`.sql` files** are popular because they are easy to read, diff in Git, and re-run.

---

## 4. “EXE” and programs involved (SQLite on Windows)

For **SQLite**, common pieces:

| Piece | Role |
|-------|------|
| **`sqlite3.exe`** | **Command-line shell**: you type SQL interactively or run `sqlite3 my.db < script.sql`. Optional—many people never install it if they only use Python. |
| **Python `sqlite3` module** | Built into Python’s standard library: open `something.db`, call `.execute("SELECT ...")`. Your Streamlit app would use this style **without** needing `sqlite3.exe`. |
| **`sqlite3.dll` / SQLite inside other apps** | The **engine** embedded inside tools (Python, DB Browser for SQLite, etc.). |

So: **one conceptual “engine,”** several **doors** into it (CLI exe, Python, GUI apps).

---

## 5. Typical beginner workflow (matches our plan)

1. **Design tables** (on paper or in chat)—what columns, keys, dates.
2. **Write `schema.sql`** with `CREATE TABLE ...`.
3. **Create empty DB:** e.g. Python opens `data/pokemon.db` and runs `schema.sql`, or CLI `sqlite3 data/pokemon.db < data/schema.sql`.
4. **Load CSV:** script reads CSV → `INSERT` or bulk load → rows live **inside** `.db`.
5. **App reads DB:** Streamlit uses Python `sqlite3` (or SQLAlchemy later) with `SELECT ...`.

**CSV** stays useful for **backup** and **Excel**; **`.db`** is what the app **queries** efficiently.

---

## 6. Minimal SQL shape (structure of the language)

Rough buckets beginners hit first:

| Bucket | Examples | Role |
|--------|-----------|------|
| **DDL** (Data Definition Language) | `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, `CREATE INDEX` | Define **structure**. |
| **DML** (Data Manipulation Language) | `INSERT`, `UPDATE`, `DELETE` | Change **rows**. |
| **Query** | `SELECT ... FROM ... WHERE ... JOIN ... GROUP BY ...` | **Read** and summarize. |
| **Transactions** (later) | `BEGIN`, `COMMIT`, `ROLLBACK` | Group changes safely. |

You don’t need every keyword at once—**CREATE**, **INSERT**, **SELECT**, **WHERE**, **JOIN**, **GROUP BY** carry most learning projects.

---

## 7. How this maps to **this** Pokémon project

| Today | Phase 2+ (`IMPLEMENTATION_PLAN.md`) |
|-------|-------------------------------------|
| History in **`data/pokemon_price_history.csv`** | Same facts eventually in **`data/*.db`** tables |
| Pandas filters in Python | More logic moves into **`SELECT`** for practice |
| No `schema.sql` yet | Add **`data/schema.sql`** (or under `python/code/sql/`) when you start Phase 2 |

---

## 8. Optional GUI

**DB Browser for SQLite** is a free desktop app to open a `.db`, browse tables, run `SELECT`, without writing Python—good for learning alongside this repo.

---

## One-sentence summary

**SQL is what you write; the engine (SQLite) is what runs it; the `.db` file is where rows actually live; `.sql` files are reusable text scripts; CSV is a handy sidecar format—not the authority database once you commit to SQLite.**
