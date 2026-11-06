"""
Module 09 exercises: Files & data.   Run:  python check.py 9

Every function receives paths as arguments. The checker creates temporary
files to test with, so don't hard-code file names.
"""

import csv
import json
from pathlib import Path


def count_lines(path):
    # TODO: return the number of lines in the text file at `path`.
    raise NotImplementedError


def longest_line(path):
    # TODO: return the longest line in the file, without its trailing newline.
    raise NotImplementedError


def write_lines(path, lines):
    # TODO: write each string in `lines` to the file, one per line
    # (each followed by "\n"). Overwrite the file if it exists.
    raise NotImplementedError


def append_log(path, message):
    # TODO: add `message` followed by "\n" to the END of the file,
    # creating it if it doesn't exist.
    raise NotImplementedError


def load_expenses(path):
    # TODO: read a CSV with columns date,category,description,amount.
    # Return a list of dicts, with "amount" converted to a float.
    raise NotImplementedError


def category_totals_from_csv(path):
    # TODO: return {category: total amount} for the CSV at path,
    # each total rounded to 2 decimals. (Reuse load_expenses!)
    raise NotImplementedError


def write_summary_csv(path, totals):
    # TODO: totals is {category: amount}. Write a CSV with header
    # "category,total" and one row per category.
    raise NotImplementedError


def save_json(path, data):
    # TODO: save `data` (dicts/lists) to path as JSON with indent=2.
    raise NotImplementedError


def load_json(path, default=None):
    # TODO: return the data from the JSON file, or `default` if the file
    # doesn't exist.
    raise NotImplementedError


def files_by_extension(folder):
    # TODO: return {extension: count} for every FILE (not sub-folder) directly
    # inside `folder`. Extensions lowercase without the dot; files with no
    # extension use "".   e.g. {"txt": 2, "csv": 1}
    raise NotImplementedError
