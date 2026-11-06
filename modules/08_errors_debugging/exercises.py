"""
Module 08 exercises: Errors & debugging.   Run:  python check.py 8

Part A: handle and raise errors.
Part B: each `buggy_` function has ONE bug. Find it and fix it.
         (The docstring says what it SHOULD do.)
"""

# ---------------------------------------------------------------- Part A


def safe_int(text, default=0):
    # TODO: return int(text), or `default` if text isn't a valid whole number.
    raise NotImplementedError


def safe_divide(a, b):
    # TODO: return a / b, or None if b is zero. Use try/except.
    raise NotImplementedError


def get_setting(settings, key, default=None):
    # TODO: return settings[key]; if the key is missing return default.
    # Use try/except KeyError (yes, .get() would also work - practise try!).
    raise NotImplementedError


def withdraw(balance, amount):
    # TODO: raise ValueError if amount <= 0, raise ValueError if amount > balance,
    # otherwise return the new balance.
    raise NotImplementedError


def parse_age(text):
    # TODO: convert text to an int age and return it.
    # Raise ValueError if it's not a number OR if it's outside 0-130.
    raise NotImplementedError


def sum_valid_numbers(items):
    # TODO: items is a list of strings. Add up the ones that are valid numbers
    # (they may be decimals like "2.5"), skip the rest.
    # sum_valid_numbers(["1", "two", "2.5", ""]) -> 3.5
    raise NotImplementedError


# ---------------------------------------------------------------- Part B


def buggy_total(numbers):
    """Return the sum of all numbers."""
    total = 0
    for n in numbers:
        total += n
        return total


def buggy_count_to(n):
    """Return a list [1, 2, ..., n]."""
    result = []
    for i in range(1, n):
        result.append(i)
    return result


def buggy_shout(text):
    """Return text in uppercase with surrounding spaces removed."""
    text.strip()
    return text.upper()


def buggy_largest(numbers):
    """Return the largest number. Numbers may all be negative."""
    largest = 0
    for n in numbers:
        if n > largest:
            largest = n
    return largest


def buggy_describe(name, age):
    """Return e.g. 'Ada is 36 years old'."""
    return name + " is " + age + " years old"
