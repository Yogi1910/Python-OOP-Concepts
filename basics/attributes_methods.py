"""Illustrates instance vs class attributes and methods."""

from __future__ import annotations


class Warehouse:
    location: str = "GLOBAL"  # class attribute shared across instances
    inventory_count: int = 0

    def __init__(self, name: str) -> None:
        self.name = name

    @classmethod
    def set_location(cls, location: str) -> None:
        cls.location = location

    @classmethod
    def increment_inventory(cls, amount: int) -> None:
        cls.inventory_count += amount

    def describe(self) -> str:
        return f"{self.name} warehouse located in {self.location} holds {self.inventory_count} items"


if __name__ == "__main__":
    regional = Warehouse("EMEA")
    Warehouse.set_location("Berlin")
    Warehouse.increment_inventory(120)
    print(regional.describe())
