"""JSON output helpers."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def write_json(payload: dict[str, Any], output_path: str) -> Path:
    """Persist payloads as formatted JSON."""

    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return destination
