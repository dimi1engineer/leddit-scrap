"""HTTP client helpers for public Reddit endpoints."""

from __future__ import annotations

from typing import Any

import requests

from leddit_scrap.config import Settings


def fetch_listing(
    subreddit: str,
    sort: str,
    limit: int,
    settings: Settings,
) -> dict[str, Any]:
    """Fetch a subreddit listing using Reddit's public JSON feed."""

    response = requests.get(
        f"{settings.reddit_base_url}/r/{subreddit}/{sort}.json",
        headers={"User-Agent": settings.reddit_user_agent},
        params={"limit": limit},
        timeout=settings.request_timeout,
    )
    response.raise_for_status()
    return response.json()
