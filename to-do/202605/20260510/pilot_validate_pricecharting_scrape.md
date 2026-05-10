# To-do: pilot_validate_pricecharting_scrape

- [x] Add `python/test/conftest.py` path bootstrap for `scrape`.
- [x] Add `python/test/test_pilot_pricecharting_scrape.py` (constants + live limited `scrape_pricecharting_data`, no mocks).
- [x] Extend `scrape_pricecharting_data` with `max_sets`, `sleep_seconds`, `quiet` for pilots outside Streamlit.
- [x] Run `poetry run pytest test/test_pilot_pricecharting_scrape.py -v` from `python/`.
- [x] Update `structure/latest.md`, `IMPLEMENTATION_PLAN.md`, and proposal/summary for paths and behavior.
