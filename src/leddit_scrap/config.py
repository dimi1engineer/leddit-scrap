"""Configuration helpers for the application."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Runtime settings loaded from environment variables."""

    reddit_base_url: str = os.getenv("REDDIT_BASE_URL", "https://www.reddit.com")
    reddit_user_agent: str = os.getenv(
        "REDDIT_USER_AGENT",
        "leddit-scrap/0.1 (+https://github.com/dimi1engineer/leddit-scrap)",
    )
    request_timeout: float = float(os.getenv("REQUEST_TIMEOUT", "15"))
    request_delay: float = float(os.getenv("REQUEST_DELAY", "1.0"))


def get_settings() -> Settings:
    """Return application settings."""

    return Settings()
