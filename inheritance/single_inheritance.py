"""Basic single inheritance example."""

from __future__ import annotations


class Vehicle:
    def __init__(self, wheels: int) -> None:
        self.wheels = wheels

    def describe(self) -> str:
        return f"Vehicle with {self.wheels} wheels"


class Car(Vehicle):
    def __init__(self, brand: str) -> None:
        super().__init__(4)
        self.brand = brand

    def describe(self) -> str:
        return f"{self.brand} car with {self.wheels} wheels"


if __name__ == "__main__":
    car = Car("Tesla")
    print(car.describe())
