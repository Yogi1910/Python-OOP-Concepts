"""Demonstrates encapsulation via name mangling and properties."""

from __future__ import annotations


class Account:
    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.__balance = balance  # private via name mangling

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount


if __name__ == "__main__":
    account = Account("Yogesh", 1000.0)
    account.deposit(150.0)
    print(account.balance)
