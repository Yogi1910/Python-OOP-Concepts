"""Dependency Inversion Principle using abstractions."""

from __future__ import annotations

from typing import Protocol


class MessageSender(Protocol):
    def send(self, message: str) -> None:
        ...


class EmailSender:
    def send(self, message: str) -> None:
        print(f"Email sent: {message}")


class NotificationService:
    def __init__(self, sender: MessageSender) -> None:
        self.sender = sender

    def notify(self, message: str) -> None:
        self.sender.send(message)


if __name__ == "__main__":
    service = NotificationService(EmailSender())
    service.notify("Deployment finished")
