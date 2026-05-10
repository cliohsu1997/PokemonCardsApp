# Proposal: add_python_poetry_env

## Goal

Provide a `python/` directory with Poetry-managed dependencies, matching the pattern used in `sports-card-automation/python`, so installs and runs use `poetry install` and `poetry run` from `python/`.

## Approach

- `package-mode = false` because the Streamlit entrypoint remains at repo root (`streamlit_app.py`).
- Pin `langchain` to `0.0.234` to match the original upstream `requirements.txt` and existing imports.
- Include `pytest` under `[dependency-groups] dev` for future `python/tests/`.
- Generate `poetry.lock` with `poetry lock` and verify with `poetry install`.
