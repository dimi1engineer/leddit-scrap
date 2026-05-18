"""Parsers that normalize Reddit payloads."""

from __future__ import annotations

from typing import Any


def parse_listing_posts(payload: dict[str, Any]) -> list[dict[str, Any]]:
    """Extract a compact list of post dictionaries from a Reddit listing."""

    children = payload.get("data", {}).get("children", [])
    parsed_posts = []

    for child in children:
        data = child.get("data", {})
        parsed_posts.append(
            {
                "id": data.get("id"),
                "title": data.get("title"),
                "author": data.get("author"),
                "score": data.get("score"),
                "num_comments": data.get("num_comments"),
                "url": data.get("url"),
                "permalink": data.get("permalink"),
            }
        )

    return parsed_posts
