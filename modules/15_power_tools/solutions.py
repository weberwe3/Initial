"""Module 15 solutions."""

import functools
from contextlib import contextmanager


def countdown(n):
    while n > 0:
        yield n
        n -= 1


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def only_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line.strip()


def batched(items, size):
    batch = []
    for item in items:
        batch.append(item)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch


def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


def uppercase_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == times:
                        raise
        return wrapper
    return decorator


@contextmanager
def recorder(log):
    log.append("start")
    try:
        yield
    finally:
        log.append("end")


def word_frequencies(words: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts
