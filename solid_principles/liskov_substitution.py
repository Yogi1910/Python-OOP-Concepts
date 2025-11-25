"""Liskov Substitution Principle demonstration."""

from __future__ import annotations


class Bird:
    def fly(self) -> str:
        return "Bird flying"


class Sparrow(Bird):
    def fly(self) -> str:
        return "Sparrow flying"


def take_off(bird: Bird) -> str:
    return bird.fly()


if __name__ == "__main__":
    print(take_off(Sparrow()))
