"""Module 13 solutions: one good set of tests for pricing.py."""

import pytest

from pricing import apply_discount, parse_price, shipping


@pytest.mark.parametrize("price, percent, expected", [
    (100, 10, 90),
    (100, 0, 100),
    (100, 100, 0),
    (59.99, 25, 44.99),
])
def test_apply_discount_normal_cases(price, percent, expected):
    assert apply_discount(price, percent) == expected


def test_apply_discount_boundaries():
    assert apply_discount(80, 0) == 80
    assert apply_discount(80, 100) == 0
    assert apply_discount(80, 50) == 40


def test_apply_discount_rejects_bad_percent():
    with pytest.raises(ValueError):
        apply_discount(100, -1)
    with pytest.raises(ValueError):
        apply_discount(100, 101)


def test_shipping():
    assert shipping(10) == 4.99
    assert shipping(49.99) == 4.99
    assert shipping(50) == 0          # the boundary: free AT exactly $50
    assert shipping(50.01) == 0


def test_parse_price():
    assert parse_price("12") == 12.0
    assert parse_price(" $5.50 ") == 5.5
    assert parse_price("$1,234.50") == 1234.5


def test_parse_price_rejects_garbage():
    with pytest.raises(ValueError):
        parse_price("twelve")
