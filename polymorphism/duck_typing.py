"""Duck typing: behavior defined by interface, not inheritance."""

from __future__ import annotations

from collections.abc import Iterable


def total_length(items: Iterable[str]) -> int:
    return sum(len(item) for item in items)


class TagList:
    def __init__(self, *tags: str) -> None:
        self.tags = list(tags)

    def __iter__(self):
        return iter(self.tags)


if __name__ == "__main__":
    print(total_length(["dev", "ops"]))
    print(total_length(TagList("python", "oop")))
