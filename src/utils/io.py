import json
from pathlib import Path
from typing import Any, Iterator


def read_jsonl(path: str | Path) -> Iterator[dict[str, Any]]:
    with open(path) as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def write_jsonl(path: str | Path, data: Iterator[dict[str, Any]]) -> None:
    with open(path, "w") as f:
        for item in data:
            f.write(json.dumps(item) + "\n")


def append_jsonl(path: str | Path, item: dict[str, Any]) -> None:
    with open(path, "a") as f:
        f.write(json.dumps(item) + "\n")


def read_json(path: str | Path) -> dict[str, Any]:
    with open(path) as f:
        return json.load(f)


def write_json(path: str | Path, data: dict[str, Any], indent: int = 2) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=indent)


def ensure_dir(path: str | Path) -> Path:
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path
