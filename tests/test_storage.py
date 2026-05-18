import json

from leddit_scrap.storage.writer_json import write_json


def test_write_json_persists_payload(tmp_path) -> None:
    destination = tmp_path / "exports" / "payload.json"
    payload = {"subreddit": "python", "posts": [{"id": "abc123"}]}

    result = write_json(payload, str(destination))

    assert result == destination
    assert json.loads(destination.read_text(encoding="utf-8")) == payload
