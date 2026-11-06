"""
Module 12 exercises: Classes & objects.   Run:  python check.py 12

Write each class from the description. The checker looks for these exact
class and method names. Delete the `pass` lines as you go.
"""

from dataclasses import dataclass, field


# ---------------------------------------------------------------------------
# 1. BankAccount
#   BankAccount(owner, balance=0)
#   .deposit(amount)   -> raise ValueError if amount <= 0, else add it
#   .withdraw(amount)  -> raise ValueError if amount <= 0 or > balance
#   .history           -> a list of ("deposit"|"withdraw", amount) tuples,
#                         one appended per successful transaction.
#                         Each account must have ITS OWN list.
#   str(account)       -> "Ada: $120.00"
# ---------------------------------------------------------------------------
class BankAccount:
    pass


# ---------------------------------------------------------------------------
# 2. Money (stores whole cents to avoid float rounding problems)
#   Money(cents)
#   str(Money(1234))           -> "$12.34"
#   Money(100) + Money(50)     -> Money(150)
#   Money(100) == Money(100)   -> True
#   Money(1) < Money(2)        -> True   (so sorted() works)
# ---------------------------------------------------------------------------
class Money:
    pass


# ---------------------------------------------------------------------------
# 3. Expense - a DATACLASS with fields:
#     description: str, amount: float, category: str = "other"
#   and a method is_large(threshold=100) -> True if amount >= threshold
# ---------------------------------------------------------------------------
# TODO: write @dataclass class Expense here


# ---------------------------------------------------------------------------
# 4. Budget - a DATACLASS with fields:
#     limit: float, expenses: list (default: a new empty list per budget)
#   methods:
#     add(expense)      -> append an Expense
#     total()           -> sum of all amounts
#     remaining()       -> limit - total
#     by_category()     -> {category: total}
#     over_budget()     -> True if total > limit
# ---------------------------------------------------------------------------
# TODO: write @dataclass class Budget here


# ---------------------------------------------------------------------------
# 5. Rectangle and Square
#   Rectangle(width, height) with a PROPERTY `area` and a method perimeter()
#   Square(side) inherits from Rectangle (use super().__init__)
# ---------------------------------------------------------------------------
# TODO: write class Rectangle and class Square here
