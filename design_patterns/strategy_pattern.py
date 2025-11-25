"""Strategy pattern to swap pricing algorithms."""

from __future__ import annotations

from typing import Protocol


class PricingStrategy(Protocol):
    def __call__(self, base_price: float) -> float:
        ...


def regular_pricing(base_price: float) -> float:
    return base_price


def discount_pricing(base_price: float) -> float:
    return base_price * 0.9


def calculate_total(base_price: float, strategy: PricingStrategy) -> float:
    return strategy(base_price)


if __name__ == "__main__":
    print(calculate_total(100, regular_pricing))
    print(calculate_total(100, discount_pricing))
