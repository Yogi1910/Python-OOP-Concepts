"""Uses abc.ABC to enforce required methods."""

from __future__ import annotations

from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, amount: float) -> str:
        raise NotImplementedError


class StripeGateway(PaymentGateway):
    def charge(self, amount: float) -> str:
        return f"Stripe charged {amount}" 


if __name__ == "__main__":
    gateway = StripeGateway()
    print(gateway.charge(49.0))
