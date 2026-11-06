"""Module 12 solutions."""

from dataclasses import dataclass, field


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []          # created in __init__, so each account gets its own

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.history.append(("withdraw", amount))

    def __str__(self):
        return f"{self.owner}: ${self.balance:,.2f}"


class Money:
    def __init__(self, cents):
        self.cents = cents

    def __str__(self):
        return f"${self.cents / 100:,.2f}"

    def __repr__(self):
        return f"Money({self.cents})"

    def __add__(self, other):
        return Money(self.cents + other.cents)

    def __eq__(self, other):
        return isinstance(other, Money) and self.cents == other.cents

    def __lt__(self, other):
        return self.cents < other.cents


@dataclass
class Expense:
    description: str
    amount: float
    category: str = "other"

    def is_large(self, threshold=100):
        return self.amount >= threshold


@dataclass
class Budget:
    limit: float
    expenses: list = field(default_factory=list)

    def add(self, expense):
        self.expenses.append(expense)

    def total(self):
        return sum(e.amount for e in self.expenses)

    def remaining(self):
        return self.limit - self.total()

    def by_category(self):
        totals = {}
        for e in self.expenses:
            totals[e.category] = totals.get(e.category, 0) + e.amount
        return totals

    def over_budget(self):
        return self.total() > self.limit


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
