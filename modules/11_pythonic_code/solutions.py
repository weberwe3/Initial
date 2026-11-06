"""Module 11 solutions."""


def squares_of_odds(numbers):
    return [n * n for n in numbers if n % 2 == 1]


def pass_fail_labels(scores):
    return ["pass" if s >= 50 else "fail" for s in scores]


def word_lengths(words):
    return {w: len(w) for w in words}


def unique_domains(emails):
    return {e.split("@")[1] for e in emails}


def food_total(rows):
    return sum(r["amount"] for r in rows if r["category"] == "food")


def has_negative(numbers):
    return any(n < 0 for n in numbers)


def pair_up(names, scores):
    return dict(zip(names, scores))


def sort_case_insensitive(words):
    return sorted(words, key=str.lower)


def oldest_person(people):
    return max(people, key=lambda p: p["age"])["name"]


def sort_by_dept_then_salary(people):
    ordered = sorted(people, key=lambda p: (p["dept"], -p["salary"]))
    return [p["name"] for p in ordered]


def top_expenses(expenses, n):
    return sorted(expenses, key=lambda e: e[1], reverse=True)[:n]


def flatten(list_of_lists):
    return [x for row in list_of_lists for x in row]


def merge_settings(defaults, overrides):
    return {**defaults, **overrides}
