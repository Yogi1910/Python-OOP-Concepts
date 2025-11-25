"""Open/Closed Principle via strategy extension."""

from __future__ import annotations

from typing import Protocol


class ShippingCost(Protocol):
    def __call__(self, weight: float) -> float:
        ...


def standard_shipping(weight: float) -> float:
    return 5 + weight * 0.5


def express_shipping(weight: float) -> float:
    return 10 + weight * 0.8


def compute_shipping(weight: float, policy: ShippingCost) -> float:
    return policy(weight)


if __name__ == "__main__":
    print(compute_shipping(10, standard_shipping))
    print(compute_shipping(10, express_shipping))
