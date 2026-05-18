"""High-level collection workflows."""

from __future__ import annotations

import time
from typing import Any

from leddit_scrap.config import Settings
from leddit_scrap.scraper.parsers import parse_listing_posts
from leddit_scrap.scraper.reddit_client import fetch_listing


def collect_subreddit_posts(
    subreddit: str,
    sort: str,
    limit: int,
    settings: Settings,
) -> dict[str, Any]:
    """Collect a normalized subreddit payload."""

    raw_listing = fetch_listing(subreddit=subreddit, sort=sort, limit=limit, settings=settings)
    posts = parse_listing_posts(raw_listing)

    # Keep a single, explicit delay point so rate limiting stays centralized.
    time.sleep(settings.request_delay)

    return {
        "subreddit": subreddit,
        "sort": sort,
        "limit": limit,
        "posts": posts,
    }
