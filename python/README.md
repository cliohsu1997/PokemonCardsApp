# Pokémon Cards App — Python (Poetry)

Same layout idea as `sports-card-automation/python`: dependencies and virtualenv are managed **only via Poetry** from this directory.

## Setup

```powershell
Set-Location "c:\Users\birdy\Desktop\SQL\PokemonCardsApp\python"
poetry install
```

## Run Streamlit (app lives at repo root)

```powershell
Set-Location "c:\Users\birdy\Desktop\SQL\PokemonCardsApp\python"
poetry run streamlit run ..\streamlit_app.py
```

## Tests

When you add tests under `python/tests/`:

```powershell
poetry run pytest tests\ -v
```

## Notes

- Google Cloud and Hugging Face features in `streamlit_app.py` expect credentials or env vars as in the upstream project.
- For a reproducible lockfile, this folder includes `poetry.lock` after the first successful `poetry lock`.
