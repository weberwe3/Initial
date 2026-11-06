"""Loading and saving expenses (JSON) and importing/exporting CSV."""

import csv
import json
from pathlib import Path

from .models import Expense

# Bank exports use all sorts of column names. Map the ones we know.
COLUMN_ALIASES = {
    "amount": ["amount", "transaction amount", "debit", "value"],
    "category": ["category", "type"],
    "description": ["description", "details", "merchant", "memo", "name"],
    "date": ["date", "transaction date", "posted date"],
}


def load(path: Path) -> tuple[list[Expense], dict[str, float]]:
    """Return (expenses, budgets). A missing file means a fresh start."""
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return [], {}
    expenses = [Expense(**item) for item in data.get("expenses", [])]
    return expenses, data.get("budgets", {})


def save(path: Path, expenses: list[Expense], budgets: dict[str, float]) -> None:
    data = {"expenses": [e.to_dict() for e in expenses], "budgets": budgets}
    tmp = Path(path).with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    tmp.replace(path)  # write-then-rename so a crash can't leave a half-written file


def _find_column(fieldnames: list[str], wanted: str) -> str | None:
    lowered = {name.strip().lower(): name for name in fieldnames}
    for alias in COLUMN_ALIASES[wanted]:
        if alias in lowered:
            return lowered[alias]
    return None


def import_csv(path: Path, default_category: str = "uncategorised") -> tuple[list[Expense], list[str]]:
    """Read a bank-style CSV. Return (expenses, problems) - bad rows are reported, not fatal."""
    expenses, problems = [], []
    with open(path, newline="", encoding="utf-8-sig") as f:   # -sig strips Excel's BOM
        reader = csv.DictReader(f)
        cols = {key: _find_column(reader.fieldnames or [], key) for key in COLUMN_ALIASES}
        if cols["amount"] is None or cols["date"] is None:
            raise ValueError(f"{path} needs at least an amount and a date column")
        for line_no, row in enumerate(reader, start=2):
            try:
                raw_amount = row[cols["amount"]].replace("$", "").replace(",", "").strip()
                category = row.get(cols["category"] or "", "") or default_category
                description = row.get(cols["description"] or "", "")
                expenses.append(Expense(
                    amount=abs(float(raw_amount)),   # banks often show spending as negative
                    category=category,
                    description=description.strip(),
                    date=row[cols["date"]].strip(),
                ))
            except (ValueError, KeyError) as e:
                problems.append(f"line {line_no}: {e}")
    return expenses, problems


def export_csv(path: Path, expenses: list[Expense]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "category", "description", "amount"])
        writer.writeheader()
        for e in expenses:
            writer.writerow({"date": e.date, "category": e.category,
                             "description": e.description, "amount": f"{e.amount:.2f}"})
