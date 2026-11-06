"""
Module 13 exercises: Write tests for pricing.py.

Run your tests:              pytest modules/13_testing/exercises.py -v
See which bugs you'd catch:  python check.py 13

Replace each `raise NotImplementedError` with real asserts. Add as many extra
test_ functions as you like. Think about BOUNDARIES and ERRORS.
"""

import pytest

from pricing import apply_discount, parse_price, shipping


def test_apply_discount_normal_cases():
    # TODO: e.g. assert apply_discount(100, 10) == 90
    raise NotImplementedError


def test_apply_discount_rejects_bad_percent():
    # TODO: use `with pytest.raises(ValueError):` for percents below 0 and above 100
    raise NotImplementedError


def test_shipping():
    # TODO: test below, AT, and above the $50 threshold
    raise NotImplementedError


def test_parse_price():
    # TODO: plain numbers, "$" signs, thousands commas, surrounding spaces...
    raise NotImplementedError


def test_parse_price_rejects_garbage():
    # TODO: something that isn't a price should raise ValueError
    raise NotImplementedError
