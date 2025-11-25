"""Demonstrates class definitions, constructors, and object usage."""

from __future__ import annotations


class Book:
    """Simple domain object that tracks title and author."""

    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def describe(self) -> str:
        return f"{self.title} by {self.author}"


if __name__ == "__main__":
    book = Book(title="Clean Code", author="Robert C. Martin")
    print(book.describe())
