"""
Module 05 exercises: Lists & tuples.   Run:  python check.py 5
"""


def average(numbers):
    # TODO: return the average of a list of numbers. Return 0 for an empty list.
    raise NotImplementedError


def only_passing(scores, pass_mark=60):
    # TODO: return a NEW list with only the scores >= pass_mark, same order.
    raise NotImplementedError


def add_tax_to_all(prices, rate):
    # TODO: return a new list where each price has tax added and is rounded
    # to 2 decimals.  add_tax_to_all([10, 20], 0.2) -> [12.0, 24.0]
    raise NotImplementedError


def second_largest(numbers):
    # TODO: return the second-largest DISTINCT value.
    # second_largest([4, 9, 2, 9, 7]) -> 7
    # You can assume there are at least two distinct values.
    raise NotImplementedError


def remove_duplicates(items):
    # TODO: return a new list without duplicates, KEEPING the original order.
    # remove_duplicates([3, 1, 3, 2, 1]) -> [3, 1, 2]
    raise NotImplementedError


def total_expenses(expenses):
    # TODO: expenses is a list of (category, amount) tuples.
    # Return the total of all amounts.
    # total_expenses([("rent", 1200), ("food", 350)]) -> 1550
    raise NotImplementedError


def biggest_expense(expenses):
    # TODO: same format as above. Return the CATEGORY name with the largest amount.
    raise NotImplementedError


def numbered_list(items):
    # TODO: return a list of strings numbered from 1.
    # numbered_list(["milk", "eggs"]) -> ["1. milk", "2. eggs"]
    # Hint: enumerate(items, start=1)
    raise NotImplementedError


def chunk(items, size):
    # TODO: split a list into smaller lists of length `size`. The last chunk
    # may be shorter.  chunk([1,2,3,4,5], 2) -> [[1,2],[3,4],[5]]
    # Hint: range(0, len(items), size) and slicing.
    raise NotImplementedError


def column(grid, index):
    # TODO: grid is a list of rows (lists). Return a list with the value at
    # position `index` from every row.
    # column([[1,2,3],[4,5,6]], 1) -> [2, 5]
    raise NotImplementedError
