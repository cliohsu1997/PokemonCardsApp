"""PriceCharting scrape pilots: constants + live site (limited set count, no mocks)."""

from __future__ import annotations

import pandas as pd

from scrape.constants import SEALED_KEYWORDS, SEALED_NAME_PATTERN
from scrape.pricecharting import scrape_pricecharting_data


def test_sealed_name_pattern_covers_keywords() -> None:
    assert "|" in SEALED_NAME_PATTERN
    for kw in SEALED_KEYWORDS:
        assert kw.lower() in SEALED_NAME_PATTERN.lower()


def test_scrape_pricecharting_real_site_limited_sets() -> None:
    """Hit PriceCharting with real HTTP; scrape a few sets only (no fake HTML)."""
    result = scrape_pricecharting_data(
        max_sets=3,
        sleep_seconds=0.25,
        quiet=True,
    )
    assert not result.ok_for_history
    df = result.df
    assert isinstance(df, pd.DataFrame)
    assert not df.empty, "Expected at least one card row from a few live sets"
    expected_cols = {
        "Set",
        "Card_Name",
        "Product_URL",
        "Ungraded_Price",
        "Grade_9_Price",
        "PSA_10_Price",
        "Image_URL",
        "Deal_Value",
    }
    assert expected_cols.issubset(set(df.columns))
    assert df["Card_Name"].notna().any()
