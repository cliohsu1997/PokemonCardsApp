"""PriceCharting.com Pokémon card table scrape."""

from __future__ import annotations

import time
from dataclasses import dataclass

import pandas as pd
import requests
import streamlit as st
from bs4 import BeautifulSoup

from scrape.constants import SEALED_NAME_PATTERN


@dataclass(frozen=True)
class ScrapeResult:
    """Output of ``scrape_pricecharting_data``.

    ``ok_for_history`` is True only when this was a **full** run (all non-Japanese
    sets, no ``max_sets`` cap), the category page loaded, at least one set URL was
    found, the per-set loop finished, and the cleaned frame has at least one row.
    """

    df: pd.DataFrame
    ok_for_history: bool


class _QuietProgress:
    """No-op progress when ``quiet=True`` (e.g. pytest against real HTTP)."""

    def progress(self, _value: float) -> None:
        return None


def scrape_pricecharting_data(
    *,
    max_sets: int | None = None,
    sleep_seconds: float = 0.3,
    quiet: bool = False,
) -> ScrapeResult:
    """Scrape category → per-set tables; return cleaned data plus history eligibility flag.

    Parameters
    ----------
    max_sets
        If set, only scrape this many set URLs (after de-dup and Japanese filter).
        Such runs are never ``ok_for_history``. Use for pilots/tests.
    sleep_seconds
        Pause between set requests (politeness). Tests may pass ``0``.
    quiet
        If True, do not call Streamlit ``st.*`` (safe outside ``streamlit run``).
    """
    base_url = "https://www.pricecharting.com"
    category_url = f"{base_url}/category/pokemon-cards"
    headers = {"User-Agent": "Mozilla/5.0"}

    def _error(msg: str) -> None:
        if quiet:
            return
        st.error(msg)

    def _warn(msg: str) -> None:
        if quiet:
            return
        st.warning(msg)

    try:
        res = requests.get(category_url, headers=headers, timeout=60)
        soup = BeautifulSoup(res.text, "html.parser")
    except Exception:
        _error("Error fetching category page.")
        print("[scrape] Finished — category fetch failed.", flush=True)
        return ScrapeResult(pd.DataFrame(), False)

    set_links = soup.select('a[href^="/console/pokemon"]')
    set_urls = list({base_url + link["href"] for link in set_links})
    set_urls = [url for url in set_urls if "japanese" not in url.lower()]
    if max_sets is not None:
        set_urls = set_urls[:max_sets]

    n_planned = len(set_urls)
    if n_planned == 0:
        print("[scrape] Finished — no set URLs after category parse.", flush=True)
        return ScrapeResult(pd.DataFrame(), False)

    is_full_run = max_sets is None
    all_data: list[dict] = []
    progress = _QuietProgress() if quiet else st.progress(0)

    for i, url in enumerate(set_urls):
        try:
            sorted_url = f"{url}?sort=highest-price"
            res = requests.get(sorted_url, headers=headers, timeout=60)
            soup = BeautifulSoup(res.text, "html.parser")
            rows = soup.select("table tr")
            for row in rows:
                cols = row.find_all("td")
                if len(cols) >= 5:
                    img_tag = cols[0].find("img")
                    if img_tag and "src" in img_tag.attrs:
                        img_url = img_tag["src"]
                    else:
                        img_url = ""

                    name_td = cols[1]
                    name = name_td.get_text(strip=True)
                    link = name_td.find("a", href=True)
                    if link and link.get("href"):
                        href = str(link["href"]).strip()
                        if href.startswith("http://") or href.startswith("https://"):
                            product_url = href
                        elif href.startswith("/"):
                            product_url = f"{base_url}{href}"
                        else:
                            product_url = f"{base_url}/{href}"
                    else:
                        product_url = ""

                    ungraded = cols[2].text.strip().replace("$", "").replace(",", "")
                    grade9 = cols[3].text.strip().replace("$", "").replace(",", "")
                    psa10 = cols[4].text.strip().replace("$", "").replace(",", "")

                    all_data.append(
                        {
                            "Set": url.split("/")[-1],
                            "Card_Name": name,
                            "Product_URL": product_url,
                            "Ungraded_Price": ungraded,
                            "Grade_9_Price": grade9,
                            "PSA_10_Price": psa10,
                            "Image_URL": img_url,
                        }
                    )
                    n_raw = len(all_data)
                    if n_raw > 0 and n_raw % 1000 == 0:
                        print(
                            f"[scrape] {n_raw:,} raw card rows scraped (every 1,000)…",
                            flush=True,
                        )
        except Exception as e:
            _warn(f"Error scraping {url}: {e}")
            continue

        if set_urls:
            progress.progress((i + 1) / len(set_urls))
        if sleep_seconds > 0:
            time.sleep(sleep_seconds)

    n_raw_total = len(all_data)
    print(
        f"[scrape] Set pages finished ({n_planned} URLs). Raw card rows: {n_raw_total:,}.",
        flush=True,
    )

    df = pd.DataFrame(all_data)
    if df.empty:
        print("[scrape] Finished — no rows after parse (empty).", flush=True)
        return ScrapeResult(df, False)

    df["Card_Name_clean"] = df["Card_Name"].str.strip()
    df = df[
        ~df["Card_Name_clean"].str.contains(
            SEALED_NAME_PATTERN,
            case=False,
            na=False,
        )
    ]
    df = df.drop(columns=["Card_Name_clean"])

    if df.empty:
        print(
            "[scrape] Finished — 0 rows after sealed-product filter "
            f"(raw was {n_raw_total:,}).",
            flush=True,
        )
        return ScrapeResult(df, False)

    for col in ["Ungraded_Price", "Grade_9_Price", "PSA_10_Price"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["Deal_Value"] = df["Grade_9_Price"] - df["Ungraded_Price"]
    df["Set"] = df["Set"].str.replace("pokemon-", "", regex=False)

    ok_for_history = is_full_run and n_planned > 0 and not df.empty
    n_kept = len(df)
    print(
        "[scrape] Finished — "
        f"raw rows: {n_raw_total:,}; after sealed filter: {n_kept:,}. "
        f"ok_for_history={ok_for_history}",
        flush=True,
    )
    return ScrapeResult(df, ok_for_history)
