"""Shows mixin-style multiple inheritance and MRO."""

from __future__ import annotations


class Loggable:
    def log(self, message: str) -> None:
        print(f"[LOG] {message}")


class Serializable:
    def serialize(self) -> dict[str, str]:
        return self.__dict__


class AuditRecord(Loggable, Serializable):
    def __init__(self, actor: str, action: str) -> None:
        self.actor = actor
        self.action = action
        self.log("AuditRecord created")


if __name__ == "__main__":
    record = AuditRecord("system", "login")
    print(record.serialize())
