"""Build a static HTML table preview from a pilot CSV (first N rows)."""

from __future__ import annotations

import html
from pathlib import Path

import pandas as pd


def write_pilot_preview_html(
    csv_path: Path,
    html_path: Path,
    *,
    n_rows: int = 5,
) -> None:
    """Read ``csv_path`` and write ``html_path`` with the first ``n_rows`` data rows."""
    df = pd.read_csv(csv_path)
    sample = df.head(n_rows)
    columns = list(sample.columns)

    def td_for(col: str, val: object) -> str:
        if pd.isna(val) or (isinstance(val, str) and not val.strip()):
            return '<td class="empty">—</td>'
        s = str(val).strip()
        if col == "Image_URL" and s.lower().startswith("http"):
            esc = html.escape(s, quote=True)
            return (
                f'<td><img class="card" src="{esc}" alt="" loading="lazy" /></td>'
            )
        if col == "Product_URL" and s.lower().startswith("http"):
            esc = html.escape(s, quote=True)
            return (
                f'<td class="url"><a href="{esc}" target="_blank" rel="noopener">'
                "open product</a></td>"
            )
        return f"<td>{html.escape(s)}</td>"

    thead = "".join(f"<th>{html.escape(c)}</th>" for c in columns)
    tbody_rows = []
    for _, row in sample.iterrows():
        cells = "".join(td_for(c, row[c]) for c in columns)
        tbody_rows.append(f"<tr>{cells}</tr>")
    tbody = "\n".join(tbody_rows)

    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Pilot sample preview</title>
  <style>
    body {{ font-family: system-ui, sans-serif; margin: 1.5rem; background: #f6f7f9; color: #111; }}
    p.meta {{ color: #444; font-size: 0.9rem; }}
    table {{ border-collapse: collapse; width: 100%; max-width: 1400px; background: #fff;
      box-shadow: 0 1px 3px rgba(0,0,0,.08); }}
    th, td {{ border: 1px solid #ccc; padding: 0.45rem 0.55rem; text-align: left;
      vertical-align: top; font-size: 0.82rem; }}
    th {{ background: #e8eaf0; font-weight: 600; }}
    td.num {{ text-align: right; font-variant-numeric: tabular-nums; }}
    td.url a {{ word-break: break-all; }}
    img.card {{ max-width: 120px; height: auto; display: block; border-radius: 4px; }}
    .empty {{ color: #888; font-style: italic; }}
  </style>
</head>
<body>
  <h1>Pilot CSV preview (first {n_rows} rows)</h1>
  <p class="meta">Generated from <code>{html.escape(str(csv_path))}</code></p>
  <table>
    <thead><tr>{thead}</tr></thead>
    <tbody>
{tbody}
    </tbody>
  </table>
</body>
</html>
"""
    html_path.parent.mkdir(parents=True, exist_ok=True)
    html_path.write_text(doc, encoding="utf-8")
