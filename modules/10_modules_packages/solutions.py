"""Module 10 solutions."""

import math
import random
import statistics
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta


def days_until(start_iso, end_iso):
    return (date.fromisoformat(end_iso) - date.fromisoformat(start_iso)).days


def add_business_days(start_iso, n):
    d = date.fromisoformat(start_iso)
    added = 0
    while added < n:
        d += timedelta(days=1)
        if d.weekday() < 5:      # Monday-Friday
            added += 1
    return d.isoformat()


def reformat_date(text):
    d = datetime.strptime(text, "%d/%m/%Y")
    return f"{d.day} {d.strftime('%B %Y')}"


def top_n_words(text, n):
    return Counter(text.lower().split()).most_common(n)


def median_and_mean(numbers):
    return statistics.median(numbers), statistics.mean(numbers)


def roll_dice(n, seed):
    random.seed(seed)
    return [random.randint(1, 6) for _ in range(n)]


def group_words_by_length(words):
    groups = defaultdict(list)
    for w in words:
        groups[len(w)].append(w)
    return dict(groups)


def hypotenuse(a, b):
    return math.hypot(a, b)   # or math.sqrt(a**2 + b**2)
