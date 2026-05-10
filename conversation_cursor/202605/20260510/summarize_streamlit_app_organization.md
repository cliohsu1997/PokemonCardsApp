# Proposal: summarize_streamlit_app_organization

Technical summary of how **`streamlit_app.py`** is organized today, plus a **target modular layout** that preserves the same structure without changing behavior yet (for your review).

---

## How `streamlit_app.py` is structured today (top → bottom)

The file is a **single script** executed linearly by Streamlit. Sections are marked with `# ----------` comment banners.

### 1. Imports (~lines 1–18)

Grouped implicitly by concern: UI (`streamlit`, `plotly`), data (`pandas`), scraping (`requests`, `BeautifulSoup`, `time`), time (`datetime`, `zoneinfo`), LangChain/HF imports (**mostly unused** in this file unless wired later).

**Note:** No cloud SDK — history is **local CSV** under **`data/`**.

### 2. Domain constants

- **`sealed_keywords`** + **`pattern`** — exclude sealed products in scrape and history filtering.

### 3. Local data paths

- **`HISTORY_CSV_PATH = "data/pokemon_price_history.csv"`** — append-only style history used by refresh and analytics.

### 4. Global presentation

- **`st.markdown(..., unsafe_allow_html=True)`** CSS: dark theme, maroon sidebar, component styling.

### 5. Scraping

- **`scrape_pricecharting_data()`**: PriceCharting → DataFrame; sealed filter; **`Deal_Value`**; numeric columns.

### 6. Local CSV helpers

- **`@st.cache_data`** **`load_data()`**: **`data/latest_pokemon_prices.csv`** when schema matches.

### 7. App chrome

- Header columns + optional PNGs.

### 8. Refresh flow

- Button → scrape → **`Date`** column → merge with existing **`HISTORY_CSV_PATH`** (skip duplicate today) → write **`pokemon_price_history.csv`** and **`latest_pokemon_prices.csv`**.

### 9. Data bootstrap

- **`get_valid_data()`**: CSV or scrape fallback.

### 10. Normalize + caption

- **`Deal_Value`**, **`Set`**, numeric coercion, Eastern time caption.

### 11. History load + analytics pipeline

- Read **`HISTORY_CSV_PATH`** → **`history_df`** → sealed filter → rolling **3/7/14/30** day ungraded changes → **`latest_with_changes`** / **`session_state`**.

### 12. Sidebar filters → table → download → Plotly charts

(Same as prior proposal.)

---

## Replication blueprint (modular files)

```text
python/code/pokemon_cards_app/
├── constants.py          # sealed_keywords, pattern, HISTORY_CSV_PATH
├── theme.py              # inject_css()
├── scrape.py             # scrape_pricecharting_data()
├── io_local.py           # load_data(), history read/write helpers
├── history.py            # merge refresh, rolling windows
├── filters.py            # pure filter helpers (optional)
├── charts.py             # Plotly builders
├── export.py             # CSV download helpers
└── app.py                # Streamlit wiring

streamlit_app.py          # thin entry or import run_app()
```

**Execution order:** constants → theme → header → refresh → `get_valid_data` → history pipeline → filters → table → download → charts.

---

## Design observations

1. **Duplicate logic:** **`Deal_Value`** / **`Set`** cleanup appears in multiple places — candidate for **`normalize_card_df(df)`**.
2. **Single history source:** one CSV path; **Phase 2–4** of **`IMPLEMENTATION_PLAN.md`** replace with SQLite.
3. **Dead imports:** LangChain/HF — prune or implement later.

---

## Status

Documentation only — adjust before refactor as needed.
