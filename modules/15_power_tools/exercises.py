"""
Module 15 exercises: Power tools.   Run:  python check.py 15
"""

import functools
import time
from contextlib import contextmanager


# ---------------------------------------------------------------- Generators

def countdown(n):
    # TODO: a GENERATOR that yields n, n-1, ..., 1. Use `yield`.
    raise NotImplementedError


def fibonacci():
    # TODO: an INFINITE generator: 0, 1, 1, 2, 3, 5, 8, ...
    # (The checker only takes the first few values.)
    raise NotImplementedError


def only_errors(lines):
    # TODO: a generator that yields each line containing "ERROR",
    # with surrounding whitespace stripped.
    raise NotImplementedError


def batched(items, size):
    # TODO: a generator yielding lists of up to `size` items at a time.
    # list(batched([1,2,3,4,5], 2)) -> [[1,2],[3,4],[5]]
    raise NotImplementedError


# ---------------------------------------------------------------- Decorators

def count_calls(func):
    # TODO: a decorator. The wrapped function should work as normal, but also
    # have an attribute `.calls` that counts how many times it was called.
    #   @count_calls
    #   def hi(): ...
    #   hi(); hi(); hi.calls -> 2
    # Use functools.wraps so the name is preserved.
    raise NotImplementedError


def uppercase_result(func):
    # TODO: a decorator that converts the wrapped function's return value
    # to uppercase.
    raise NotImplementedError


def retry(times):
    # TODO: a decorator WITH an argument. Call the function; if it raises an
    # exception, try again, up to `times` attempts in total. If the last attempt
    # also fails, let the exception propagate.
    raise NotImplementedError


# ---------------------------------------------------------- Context managers

@contextmanager
def recorder(log):
    # TODO: append "start" to the list `log` on entry, and "end" on exit -
    # even if the with-block raises an exception (use try/finally).
    raise NotImplementedError
    yield  # (leave this here until you write your own yield)


# ---------------------------------------------------------------- Type hints

def word_frequencies(words):
    # TODO: add type hints to this function's signature:
    #   words is a list of strings; it returns a dict mapping str -> int.
    # Then implement it.
    raise NotImplementedError
