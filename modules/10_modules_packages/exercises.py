"""
Module 10 exercises: The standard library.   Run:  python check.py 10

Use the standard library for each of these. Add the imports you need at the
top of this file. Part of the exercise is finding the right tool!
"""

# TODO: add your imports here, e.g.
# from datetime import date, timedelta


def days_until(start_iso, end_iso):
    # TODO: both are strings like "2026-11-06". Return the number of days
    # from start to end.  days_until("2026-11-06", "2026-12-25") -> 49
    # Hint: date.fromisoformat()
    raise NotImplementedError


def add_business_days(start_iso, n):
    # TODO: return the ISO date string that is n WORKING days (Mon-Fri) after
    # start. add_business_days("2026-11-06", 1) -> "2026-11-09" (Fri -> Mon)
    # Hint: date.weekday() is 0 for Monday ... 6 for Sunday.
    raise NotImplementedError


def reformat_date(text):
    # TODO: convert "06/11/2026" (day/month/year) to "6 November 2026".
    # Hint: datetime.strptime and strftime. "%B" is the full month name.
    # Watch out: "%d" gives "06" - you need "6".
    raise NotImplementedError


def top_n_words(text, n):
    # TODO: return a list of the n most common words (lowercase) as
    # (word, count) tuples, most common first.
    # Hint: collections.Counter has a method for exactly this.
    raise NotImplementedError


def median_and_mean(numbers):
    # TODO: return (median, mean) using the statistics module.
    raise NotImplementedError


def roll_dice(n, seed):
    # TODO: return a list of n dice rolls (1-6). Call random.seed(seed) first
    # so the results are repeatable, then use random.randint for each roll.
    raise NotImplementedError


def group_words_by_length(words):
    # TODO: return a dict {length: [words]} using collections.defaultdict(list).
    # Return it as a normal dict: dict(your_defaultdict).
    raise NotImplementedError


def hypotenuse(a, b):
    # TODO: length of the long side of a right-angled triangle, using math.
    # hypotenuse(3, 4) -> 5.0
    raise NotImplementedError
