"""Interface Segregation Principle via granular protocols."""

from __future__ import annotations

from typing import Protocol


class Printable(Protocol):
    def print(self) -> str:
        ...


class Scannable(Protocol):
    def scan(self) -> str:
        ...


class Printer:
    def print(self) -> str:
        return "Printing document"


class Scanner:
    def scan(self) -> str:
        return "Scanning document"


if __name__ == "__main__":
    printer: Printable = Printer()
    scanner: Scannable = Scanner()
    print(printer.print())
    print(scanner.scan())
