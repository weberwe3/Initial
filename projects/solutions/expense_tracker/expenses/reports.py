"""Pure functions that analyse expenses. No printing, no input - easy to test."""

from collections import defaultdict
from datetime import date

from .models import Expense


def filter_expenses(expenses: list[Expense], month: str | None = None,
                    category: str | None = None) -> list[Expense]:
    result = expenses
    if month:
        result = [e for e in result if e.month == month]
    if category:
        result = [e for e in result if e.category == category.lower()]
    return sorted(result, key=lambda e: e.date)


def totals_by_category(expenses: list[Expense]) -> dict[str, float]:
    totals: dict[str, float] = defaultdict(float)
    for e in expenses:
        totals[e.category] += e.amount
    # biggest category first
    return {k: round(v, 2) for k, v in sorted(totals.items(), key=lambda kv: kv[1], reverse=True)}


def total(expenses: list[Expense]) -> float:
    return round(sum(e.amount for e in expenses), 2)


def biggest(expenses: list[Expense]) -> Expense | None:
    return max(expenses, key=lambda e: e.amount, default=None)


def over_budget(totals: dict[str, float], budgets: dict[str, float]) -> dict[str, float]:
    """Return {category: budget} for each category whose total exceeds its budget."""
    return {cat: budgets[cat] for cat, spent in totals.items() if cat in budgets and spent > budgets[cat]}


def month_label(month: str) -> str:
    """'2026-11' -> 'November 2026'"""
    return date.fromisoformat(month + "-01").strftime("%B %Y")
