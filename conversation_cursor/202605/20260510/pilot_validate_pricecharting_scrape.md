# Proposal: pilot_validate_pricecharting_scrape

## Goal

Validate the refactored `python/code/scrape` package without running the full multi-set Streamlit scrape.

## Approach

1. **Constants check** — Assert `SEALED_NAME_PATTERN` is built from every `SEALED_KEYWORDS` entry (cheap regression guard).
2. **Live scrape pilot** — Call `scrape_pricecharting_data(max_sets=…, quiet=True, sleep_seconds=…)` so pytest hits the real site for a small number of sets (no mocked HTML). `quiet` avoids Streamlit UI calls outside `streamlit run`.

## Rationale

- Full scrape over every set is too slow for routine tests; `max_sets` caps work while still using real HTML and table parsing.
- Tests live under **`python/test/`** (Poetry project root), not inside `code/scrape/`.

## Related files

- `python/test/conftest.py` — adds **`python/code/`** to `sys.path` for imports.
- `python/test/test_pilot_pricecharting_scrape.py` — scrape pilot tests.
- `python/code/scrape/pricecharting.py` — optional `max_sets`, `sleep_seconds`, `quiet` on `scrape_pricecharting_data`.
