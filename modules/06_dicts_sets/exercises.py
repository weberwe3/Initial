"""
Module 06 exercises: Dictionaries & sets.   Run:  python check.py 6
"""


def word_counts(text):
    # TODO: return a dict of how many times each word appears. Ignore case.
    # word_counts("The cat the") -> {"the": 2, "cat": 1}
    raise NotImplementedError


def most_common_word(text):
    # TODO: return the word that appears most often (ignore case).
    # If there's a tie, return whichever reached that count first in the text.
    raise NotImplementedError


def totals_by_category(transactions):
    # TODO: transactions is a list of (category, amount) tuples.
    # Return a dict of category -> total amount.
    raise NotImplementedError


def invert(d):
    # TODO: swap keys and values.  invert({"a": 1, "b": 2}) -> {1: "a", 2: "b"}
    raise NotImplementedError


def lookup_price(prices, item):
    # TODO: return the price of `item`, or 0 if it isn't in the prices dict.
    raise NotImplementedError


def cart_total(prices, cart):
    # TODO: prices is {item: price}; cart is {item: quantity}.
    # Return the total cost, rounded to 2 decimals. Ignore items with no price.
    raise NotImplementedError


def names_in_dept(people, dept):
    # TODO: people is a list of dicts with "name" and "dept" keys.
    # Return a list of names in the given department, in original order.
    raise NotImplementedError


def average_salary_by_dept(people):
    # TODO: people have "dept" and "salary" keys.
    # Return {dept: average salary}.
    raise NotImplementedError


def unique_count(items):
    # TODO: return how many DIFFERENT items there are.  unique_count([1,1,2]) -> 2
    raise NotImplementedError


def missing_skills(my_skills, job_skills):
    # TODO: both are lists. Return a SORTED list of skills the job needs that
    # you don't have.
    raise NotImplementedError


def group_by_first_letter(words):
    # TODO: return {letter: [words starting with it]} (lowercase letters,
    # words kept in original order).
    # group_by_first_letter(["apple", "Avocado", "banana"])
    #   -> {"a": ["apple", "Avocado"], "b": ["banana"]}
    raise NotImplementedError
