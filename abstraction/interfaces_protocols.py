"""Structural typing via typing.Protocol."""

from __future__ import annotations

from typing import Protocol


class SupportsExport(Protocol):
    def export(self) -> str:  # pragma: no cover - simple demo
        ...


class CsvExporter:
    def export(self) -> str:
        return "id,name\n1,Python"


def run_exporter(exporter: SupportsExport) -> None:
    print(exporter.export())


if __name__ == "__main__":
    run_exporter(CsvExporter())
