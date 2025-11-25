"""Lightweight tests to verify inheritance relationships."""

from inheritance.single_inheritance import Car


def test_car_has_four_wheels() -> None:
    car = Car("Test")
    assert car.wheels == 4
