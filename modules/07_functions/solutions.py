"""Module 07 solutions."""


def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


def compound_interest(principal, rate, years=1):
    return round(principal * (1 + rate) ** years, 2)


def total(*numbers):
    return sum(numbers)


def parse_expense(line):
    name, amount = line.split(",")
    return name.strip(), float(amount)


def parse_expenses(text):
    result = []
    for line in text.split("\n"):
        if line.strip():
            result.append(parse_expense(line))
    return result


def apply_to_all(func, items):
    result = []
    for item in items:
        result.append(func(item))
    return result


def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply


def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
