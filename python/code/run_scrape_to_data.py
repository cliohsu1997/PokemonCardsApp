"""Run a capped pilot scrape and/or a full scrape from the repo root (no Streamlit).

Examples (from ``PokemonCardsApp/``)::

    poetry run python python/code/run_scrape_to_data.py pilot
    poetry run python python/code/run_scrape_to_data.py full
    poetry run python python/code/run_scrape_to_data.py both
"""

from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CODE_ROOT = REPO_ROOT / "python" / "code"


def main() -> None:
    parser = argparse.ArgumentParser(description="Pilot and/or full PriceCharting scrape to data/.")
    parser.add_argument(
        "mode",
        choices=["pilot", "full", "both"],
        help="pilot = sample CSV only; full = latest + maybe history; both = pilot then full",
    )
    parser.add_argument(
        "--pilot-sets",
        type=int,
        default=5,
        help="Number of set pages for pilot (default 5).",
    )
    parser.add_argument(
        "--pilot-out",
        default="data/pokemon_pilot_sample.csv",
        help="Pilot output path relative to repo root.",
    )
    args = parser.parse_args()

    os.chdir(REPO_ROOT)
    sys.path.insert(0, str(CODE_ROOT))

    from scrape.persist import (
        HISTORY_CSV_PATH,
        LATEST_CSV_PATH,
        persist_scrape_output,
    )
    from scrape.pricecharting import scrape_pricecharting_data

    today = datetime.now().strftime("%Y-%m-%d")

    if args.mode in ("pilot", "both"):
        print(f"Pilot scrape (max_sets={args.pilot_sets}) → {args.pilot_out} …")
        pilot = scrape_pricecharting_data(
            max_sets=args.pilot_sets,
            sleep_seconds=0.2,
            quiet=True,
        )
        persist_scrape_output(
            pilot,
            today,
            latest_csv=args.pilot_out,
            update_history=False,
        )
        print(
            "  done:",
            "rows",
            len(pilot.df),
            "ok_for_history",
            pilot.ok_for_history,
            "(pilot never updates history)",
        )
        pilot_csv = REPO_ROOT / args.pilot_out
        preview_html = pilot_csv.with_name(f"{pilot_csv.stem}_preview.html")
        from scrape.sample_preview import write_pilot_preview_html

        write_pilot_preview_html(pilot_csv, preview_html, n_rows=5)
        print("  preview:", preview_html.relative_to(REPO_ROOT))

    if args.mode in ("full", "both"):
        print("Full scrape (all sets) →", LATEST_CSV_PATH, "…")
        full = scrape_pricecharting_data(quiet=True)
        persist_scrape_output(full, today, update_history=True)
        print(
            "  done:",
            "rows",
            len(full.df),
            "ok_for_history",
            full.ok_for_history,
            "history",
            HISTORY_CSV_PATH,
        )


if __name__ == "__main__":
    main()
