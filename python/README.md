# Pokémon Cards App — Python (Poetry)

Use **`poetry run`** for every Python-related command after **`cd`** into **`python/`**. See **`.cursor/skills/python/SKILL.md`**.

## Convention: where Poetry puts the virtualenv

This repo follows Poetry’s **in-project** convention:

| Piece | Location | Committed to Git? |
|-------|----------|-------------------|
| Project definition | **`pyproject.toml`** | Yes |
| Locked dependency graph | **`poetry.lock`** | Yes |
| Local Poetry toggles | **`poetry.toml`** (`virtualenvs.in-project = true`) | Yes |
| Installed interpreter + packages | **`python/.venv/`** | **No** (see repo `.gitignore`) |
| Your code | **`code/`**, **`test/`** | Yes |

When you run **`poetry install`** from **`python/`**, Poetry **creates `python/.venv/`** (next to `pyproject.toml`) and installs packages there. You do **not** maintain a hand-made **`venv/`** folder.

**Default (without in-project):** Poetry keeps envs under its cache directory; harder to find. **`poetry.toml`** pins **in-project** so the env always sits beside your config files.

Do **not** put **`pyproject.toml`**, **`poetry.lock`**, **`poetry.toml`**, or **`README.md`** inside **`.venv/`** — only Poetry-managed binaries and libraries belong there.

## Layout

| Path | Role |
|------|------|
| **`.venv/`** | Auto-created virtualenv (gitignored). |
| **`code/`** | Application scripts. |
| **`test/`** | `pytest` tests. |

## Setup

```powershell
Set-Location "c:\Users\birdy\Desktop\SQL\PokemonCardsApp\python"
poetry install
```

After this, **`python/.venv/`** exists locally; delete it anytime with **Remove-Item -Recurse .venv** if you need a clean reinstall.

## Run Streamlit (app at repo root)

```powershell
Set-Location "c:\Users\birdy\Desktop\SQL\PokemonCardsApp\python"
poetry run streamlit run ..\streamlit_app.py
```

## Scripts in `code/`

```powershell
Set-Location "c:\Users\birdy\Desktop\SQL\PokemonCardsApp\python"
poetry run python code\your_script.py
```

## Tests

```powershell
Set-Location "c:\Users\birdy\Desktop\SQL\PokemonCardsApp\python"
poetry run pytest test\ -v
```

(`pyproject.toml` sets **`testpaths = ["test"]`**.)

## Notes

- Hugging Face–related imports in `streamlit_app.py` may expect **`HF_TOKEN`** (or similar) if you enable those features.
