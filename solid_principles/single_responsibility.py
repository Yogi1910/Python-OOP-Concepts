"""Single Responsibility Principle example."""

from __future__ import annotations


class ReportGenerator:
    def generate(self) -> str:
        return "Quarterly report"


class ReportPrinter:
    def print(self, report: str) -> None:
        print(report)


if __name__ == "__main__":
    generator = ReportGenerator()
    printer = ReportPrinter()
    printer.print(generator.generate())
