# Proposal: pilot_validate_pricecharting_scrape

## Goal

Validate the refactored `python/code/scrape` package without running the full multi-set Streamlit scrape.

## Approach

1. **Constants check** — Assert `SEALED_NAME_PATTERN` is built from every `SEALED_KEYWORDS` entry (cheap regression guard).
2. **Live category pilot** — Single `GET` to `https://www.pricecharting.com/category/pokemon-cards`, parse with the same CSS selector as production (`a[href^="/console/pokemon"]`), assert HTTP 200 and a minimum number of links. Confirms reachability and that the listing HTML shape has not obviously changed.
3. **Mocked scrape path** — Patch `requests.get`, `time.sleep`, and Streamlit UI hooks; feed minimal HTML for one category link and one set table row. Assert DataFrame columns, numeric coercion, `Deal_Value`, and `Set` cleanup (`pokemon-` prefix stripped).

## Rationale

- Full scrape is slow and brittle in CI; the mocked test exercises `scrape_pricecharting_data()` end-to-end for parsing and filtering.
- The live pilot is a thin canary for site availability and selector drift.

## Related files

- `python/test/conftest.py` — `sys.path` for `scrape` imports.
- `python/test/test_pilot_pricecharting_scrape.py` — pilot tests.
