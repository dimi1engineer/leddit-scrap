from leddit_scrap.scraper.parsers import parse_listing_posts


def test_parse_listing_posts_extracts_expected_fields() -> None:
    payload = {
        "data": {
            "children": [
                {
                    "data": {
                        "id": "abc123",
                        "title": "Example post",
                        "author": "alice",
                        "score": 42,
                        "num_comments": 7,
                        "url": "https://example.com",
                        "permalink": "/r/python/comments/abc123/example_post/",
                    }
                }
            ]
        }
    }

    posts = parse_listing_posts(payload)

    assert posts == [
        {
            "id": "abc123",
            "title": "Example post",
            "author": "alice",
            "score": 42,
            "num_comments": 7,
            "url": "https://example.com",
            "permalink": "/r/python/comments/abc123/example_post/",
        }
    ]
