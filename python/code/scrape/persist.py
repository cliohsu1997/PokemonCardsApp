"""Write scrape results to CSV: always latest snapshot; history only when eligible."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Union

import pandas as pd

from scrape.pricecharting import ScrapeResult

PathLike = Union[str, Path]

LATEST_CSV_PATH = "data/latest_pokemon_prices.csv"
HISTORY_CSV_PATH = "data/pokemon_price_history.csv"


def persist_scrape_output(
    result: ScrapeResult,
    today: str,
    *,
    latest_csv: PathLike | None = None,
    history_csv: PathLike | None = None,
    update_history: bool = True,
) -> None:
    """Write ``latest`` CSV. Optionally append to ``history`` (see ``update_history``).

    History is updated only when ``update_history`` is True, ``result.ok_for_history``,
    the frame is non-empty, and ``today`` is not already in the history file.
    """
    latest_path = Path(latest_csv or LATEST_CSV_PATH)
    history_path = Path(history_csv or HISTORY_CSV_PATH)

    os.makedirs(latest_path.parent, exist_ok=True)
    df = result.df
    if df.empty:
        latest_out = pd.DataFrame(
            columns=[
                "Set",
                "Card_Name",
                "Product_URL",
                "Ungraded_Price",
                "Grade_9_Price",
                "PSA_10_Price",
                "Image_URL",
                "Deal_Value",
                "Date",
            ]
        )
    else:
        latest_out = df.copy()
        latest_out["Date"] = today
    latest_out.to_csv(latest_path, index=False)

    if not update_history or not result.ok_for_history or result.df.empty:
        return

    try:
        old = (
            pd.read_csv(history_path)
            if history_path.is_file()
            else pd.DataFrame()
        )
    except Exception:
        old = pd.DataFrame()

    if old.empty:
        combined = latest_out
    elif "Date" in old.columns and today not in old["Date"].astype(str).values:
        combined = pd.concat([old, latest_out], ignore_index=True)
    else:
        return

    os.makedirs(history_path.parent, exist_ok=True)
    combined.to_csv(history_path, index=False)
