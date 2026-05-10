"""Pilot checks for PriceCharting scrape: live category probe + mocked full path."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pandas as pd
import pytest
import requests
from bs4 import BeautifulSoup

from scrape.constants import SEALED_KEYWORDS, SEALED_NAME_PATTERN
from scrape.pricecharting import scrape_pricecharting_data


def test_sealed_name_pattern_covers_keywords() -> None:
    assert "|" in SEALED_NAME_PATTERN
    for kw in SEALED_KEYWORDS:
        assert kw.lower() in SEALED_NAME_PATTERN.lower()


def test_pricecharting_pokemon_category_reachable_and_has_sets() -> None:
    """Live pilot: category page must load and expose console set links."""
    url = "https://www.pricecharting.com/category/pokemon-cards"
    res = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=60,
    )
    assert res.status_code == 200
    soup = BeautifulSoup(res.text, "html.parser")
    links = soup.select('a[href^="/console/pokemon"]')
    assert len(links) >= 3, "Expected multiple Pokémon set links on category page"


def test_scrape_pricecharting_data_mocked_one_set() -> None:
    """Pilot without network: one category link → one set table → expected columns."""
    category_html = """
    <html><body>
    <a href="/console/pokemon-test-set">Test Set</a>
    </body></html>
    """
    set_html = """
    <html><body>
    <table>
    <tr>
      <td><img src="https://example.com/card.png" /></td>
      <td>Charizard Holo</td>
      <td>$100</td>
      <td>$200</td>
      <td>$300</td>
    </tr>
    </table>
    </body></html>
    """

    class FakeResp:
        def __init__(self, text: str) -> None:
            self.text = text

    def fake_get(url: str, headers=None, timeout=None) -> FakeResp:
        if "category/pokemon-cards" in url:
            return FakeResp(category_html)
        return FakeResp(set_html)

    mock_progress = MagicMock()
    with (
        patch("scrape.pricecharting.requests.get", side_effect=fake_get),
        patch("scrape.pricecharting.time.sleep"),
        patch("scrape.pricecharting.st.progress", return_value=mock_progress),
        patch("scrape.pricecharting.st.error"),
        patch("scrape.pricecharting.st.warning"),
    ):
        df = scrape_pricecharting_data()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    expected_cols = {
        "Set",
        "Card_Name",
        "Ungraded_Price",
        "Grade_9_Price",
        "PSA_10_Price",
        "Image_URL",
        "Deal_Value",
    }
    assert expected_cols.issubset(set(df.columns))
    row = df.iloc[0]
    assert row["Card_Name"] == "Charizard Holo"
    assert row["Ungraded_Price"] == 100.0
    assert row["Grade_9_Price"] == 200.0
    assert row["PSA_10_Price"] == 300.0
    assert row["Set"] == "test-set"
