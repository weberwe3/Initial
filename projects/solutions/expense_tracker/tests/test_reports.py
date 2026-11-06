import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from expenses import reports  # noqa: E402
from expenses.models import Expense  # noqa: E402


@pytest.fixture
def expenses():
    return [
        Expense(1200, "rent", "November rent", "2026-11-01"),
        Expense(12.5, "Food", "Lunch", "2026-11-03"),
        Expense(30, "food", "Dinner", "2026-11-10"),
        Expense(20, "fun", "Cinema", "2026-10-28"),
    ]


def test_category_is_normalised():
    assert Expense(5, "  Food ", "", "2026-01-01").category == "food"


def test_rejects_non_positive_amount():
    with pytest.raises(ValueError):
        Expense(0, "food", "", "2026-01-01")


def test_rejects_bad_date():
    with pytest.raises(ValueError):
        Expense(5, "food", "", "2026-13-01")


def test_filter_by_month(expenses):
    nov = reports.filter_expenses(expenses, month="2026-11")
    assert [e.description for e in nov] == ["November rent", "Lunch", "Dinner"]


def test_filter_by_category_ignores_case(expenses):
    assert len(reports.filter_expenses(expenses, category="FOOD")) == 2


def test_totals_by_category_biggest_first(expenses):
    totals = reports.totals_by_category(expenses)
    assert totals == {"rent": 1200, "food": 42.5, "fun": 20}
    assert list(totals) == ["rent", "food", "fun"]


def test_total_and_biggest(expenses):
    assert reports.total(expenses) == 1262.5
    assert reports.biggest(expenses).description == "November rent"
    assert reports.biggest([]) is None


def test_over_budget():
    assert reports.over_budget({"food": 412.3, "fun": 50}, {"food": 300, "fun": 100}) == {"food": 300}


def test_month_label():
    assert reports.month_label("2026-11") == "November 2026"
