---
name: python
description: >-
  Python layout and Poetry conventions for this repository (in-project .venv,
  pyproject.toml, poetry.toml). Use when writing Python, running poetry run,
  or when the user asks about python/, virtualenv, or test/.
---

# Python skill

Follow these rules for **`python/`**. Applies **only to this repository**.

## Always run Python through Poetry

**Mandatory:** Use Poetry for installs and runs:

- **`poetry run python …`**, **`poetry run streamlit …`**, **`poetry run pytest …`**
- **`poetry add`** / **`poetry update`** — not bare **`pip install`** for project deps.

**`cd` into `python/`** first. Prefer **`poetry run`** over **`poetry shell`** in docs and automation.

## Convention: in-project `.venv`

- **`python/poetry.toml`** sets **`[virtualenvs] in-project = true`** so Poetry creates **`python/.venv/`** next to **`pyproject.toml`** (not under Poetry’s global cache).
- **`python/.venv/`** is **gitignored**; it holds **`Scripts/`**, **`Lib/`**, etc. Only Poetry manages its contents.
- **`pyproject.toml`**, **`poetry.lock`**, **`poetry.toml`**, **`README.md`** live **in `python/`**, never inside **`.venv/`**.
- Do **not** use a tracked **`python/venv/`** folder — this repo uses **`.venv`** only.

## Layout under `python/`

```
python/
├── .venv/           → created by Poetry on poetry install (gitignored)
├── code/
├── test/
├── poetry.toml      → in-project virtualenv setting (committed)
├── pyproject.toml
├── poetry.lock
└── README.md
```

## Code style

- Long calls: one argument per line where helpful; trailing comma when breaking lines.
- Imports: stdlib → third party → local.

## Running commands

From **`python/`**:

| Goal | Command |
|------|---------|
| Install deps | `poetry install` |
| Streamlit | `poetry run streamlit run ..\streamlit_app.py` |
| Script in `code/` | `poetry run python code\your_script.py` |
| Tests | `poetry run pytest test\ -v` |

## Output paths

Use **`output/`**, **`data/`**, etc., per **`structure/latest.md`**.
