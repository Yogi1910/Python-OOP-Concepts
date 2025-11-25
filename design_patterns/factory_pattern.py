"""Simple factory pattern for creating transports."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Transport:
    mode: str


class TransportFactory:
    @staticmethod
    def create(mode: str) -> Transport:
        return Transport(mode=mode)


if __name__ == "__main__":
    print(TransportFactory.create("car"))
