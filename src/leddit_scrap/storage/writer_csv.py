"""CSV output helpers."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable


def write_csv(rows: Iterable[dict], output_path: str) -> Path:
    """Write dictionaries to CSV using the keys from the first row."""

    materialized_rows = list(rows)
    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)

    if not materialized_rows:
        destination.write_text("", encoding="utf-8")
        return destination

    with destination.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=list(materialized_rows[0].keys()))
        writer.writeheader()
        writer.writerows(materialized_rows)

    return destination
