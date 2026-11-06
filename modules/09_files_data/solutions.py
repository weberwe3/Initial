"""Module 09 solutions."""

import csv
import json
from pathlib import Path


def count_lines(path):
    with open(path, encoding="utf-8") as f:
        return sum(1 for _ in f)


def longest_line(path):
    longest = ""
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if len(line) > len(longest):
                longest = line
    return longest


def write_lines(path, lines):
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


def append_log(path, message):
    with open(path, "a", encoding="utf-8") as f:
        f.write(message + "\n")


def load_expenses(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            row["amount"] = float(row["amount"])
            rows.append(row)
    return rows


def category_totals_from_csv(path):
    totals = {}
    for e in load_expenses(path):
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    return {cat: round(total, 2) for cat, total in totals.items()}


def write_summary_csv(path, totals):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["category", "total"])
        for category, total in totals.items():
            writer.writerow([category, total])


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_json(path, default=None):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return default


def files_by_extension(folder):
    counts = {}
    for p in Path(folder).iterdir():
        if p.is_file():
            ext = p.suffix.lower().lstrip(".")
            counts[ext] = counts.get(ext, 0) + 1
    return counts
