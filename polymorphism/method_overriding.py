"""Demonstrates runtime polymorphism via overriding."""

from __future__ import annotations


class Notification:
    def send(self, message: str) -> str:
        raise NotImplementedError


class EmailNotification(Notification):
    def send(self, message: str) -> str:
        return f"Email: {message}"


class SmsNotification(Notification):
    def send(self, message: str) -> str:
        return f"SMS: {message}"


def dispatch(notification: Notification, message: str) -> str:
    return notification.send(message)


if __name__ == "__main__":
    print(dispatch(EmailNotification(), "Welcome"))
    print(dispatch(SmsNotification(), "OTP 1234"))
