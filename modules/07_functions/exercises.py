"""
Module 07 exercises: Functions.   Run:  python check.py 7

This time YOU write some of the function definitions (the `def` lines).
Read each TODO carefully; the checker expects the exact names given.
"""


def greet(name, greeting="Hello"):
    # TODO: return "<greeting>, <name>!"  greet("Ada") -> "Hello, Ada!"
    raise NotImplementedError


def compound_interest(principal, rate, years=1):
    # TODO: return principal * (1 + rate) ** years, rounded to 2 decimals.
    raise NotImplementedError


# TODO: write a function called `total` that accepts ANY number of numbers
# and returns their sum.  total(1, 2, 3) -> 6 ; total() -> 0
# Hint: def total(*numbers):


# TODO: write a function called `parse_expense` that takes a string like
# "rent, 1200" and returns a tuple ("rent", 1200.0): name stripped of
# spaces, amount as a float.


# TODO: write `parse_expenses(text)` that takes several lines like
# "rent, 1200\nfood, 350" and returns a list of tuples by CALLING
# parse_expense on each non-empty line.


# TODO: write `apply_to_all(func, items)` that returns a new list with func
# applied to each item.  apply_to_all(len, ["hi", "bye"]) -> [2, 3]


def make_multiplier(factor):
    # TODO (stretch): return a FUNCTION that multiplies its argument by factor.
    # double = make_multiplier(2); double(5) -> 10
    # Hint: define a function inside this one and return it (no parentheses).
    raise NotImplementedError


def add_item(item, items=None):
    # TODO: append item to the list `items` and return the list.
    # If items is not given, start with a NEW empty list every time.
    # add_item("a") -> ["a"] ; add_item("b") -> ["b"]  (not ["a", "b"]!)
    raise NotImplementedError
