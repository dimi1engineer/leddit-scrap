"""Command-line entrypoint for the scraper workflow."""

from __future__ import annotations

import argparse

from leddit_scrap.config import get_settings
from leddit_scrap.scraper.collectors import collect_subreddit_posts
from leddit_scrap.storage.writer_json import write_json


def build_parser() -> argparse.ArgumentParser:
    """Create the CLI parser used by the operational script."""

    parser = argparse.ArgumentParser(description="Collect public Reddit subreddit data.")
    parser.add_argument("subreddit", help="Subreddit name without the r/ prefix.")
    parser.add_argument(
        "--sort",
        default="hot",
        choices=["hot", "new", "top", "rising"],
        help="Reddit listing sort order.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Number of posts to request from the listing.",
    )
    parser.add_argument(
        "--output",
        help="Optional JSON output path. When omitted, prints a summary only.",
    )
    return parser


def main() -> int:
    """Execute the CLI workflow."""

    parser = build_parser()
    args = parser.parse_args()
    settings = get_settings()

    payload = collect_subreddit_posts(
        subreddit=args.subreddit,
        sort=args.sort,
        limit=args.limit,
        settings=settings,
    )

    if args.output:
        write_json(payload, args.output)
        print(f"Saved subreddit payload to {args.output}")
    else:
        print(
            f"Prepared scraper payload for r/{args.subreddit} "
            f"with {len(payload['posts'])} posts."
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
