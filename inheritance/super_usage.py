"""Highlights super() for cooperative multiple inheritance."""

from __future__ import annotations


class Notifier:
    def __init__(self, channel: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.channel = channel


class Timestamped:
    def __init__(self, created_at: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.created_at = created_at


class Alert(Notifier, Timestamped):
    def __init__(self, message: str, channel: str, created_at: str) -> None:
        super().__init__(channel=channel, created_at=created_at)
        self.message = message


if __name__ == "__main__":
    alert = Alert("Threshold crossed", "email", "2025-11-25T10:00:00Z")
    print(alert.channel, alert.created_at, alert.message)
