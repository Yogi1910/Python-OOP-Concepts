"""Observer pattern using callback subscribers."""

from __future__ import annotations

from collections.abc import Callable

Observer = Callable[[str], None]


class EventBus:
    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self._observers.append(observer)

    def publish(self, message: str) -> None:
        for observer in self._observers:
            observer(message)


if __name__ == "__main__":
    bus = EventBus()
    bus.subscribe(lambda msg: print(f"Listener A received: {msg}"))
    bus.publish("Build completed")
