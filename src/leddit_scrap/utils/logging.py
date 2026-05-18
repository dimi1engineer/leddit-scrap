"""Logging helpers for the project."""

from __future__ import annotations

import logging


def configure_logging(level: int = logging.INFO) -> None:
    """Apply a basic logging configuration for CLI usage."""

    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
