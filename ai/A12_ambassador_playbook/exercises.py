"""
Module A12 exercises: The ambassador's toolkit.   Run:  python check.py A12

Prioritise use cases, estimate value conservatively, and report adoption,
the numbers that turn AI enthusiasm into leadership decisions.
"""

import math


def score_use_case(uc):
    # TODO: uc is a dict with "value", "feasibility" (1-5 each) and "risk" (1-5,
    # 5 = riskiest). Return value * 0.5 + feasibility * 0.3 - (risk - 1) * 0.2,
    # rounded to 2 decimals.
    raise NotImplementedError


def quadrant(uc):
    # TODO: place a use case on the 2x2:
    #   value >= 3 and feasibility >= 3 -> "Quick win"
    #   value >= 3 and feasibility < 3  -> "Strategic bet"
    #   value < 3 and feasibility >= 3  -> "Fill-in"
    #   otherwise                       -> "Avoid"
    # A use case with risk 5 is always "Avoid" until controls lower the risk.
    raise NotImplementedError


def prioritise(use_cases):
    # TODO: return a NEW list of new dicts, each with added "score" and "quadrant"
    # fields, sorted by score (highest first; ties keep the original order).
    raise NotImplementedError


def annual_value(hours_saved_per_week, people, hourly_cost, weeks=46, tool_cost_per_month=0):
    # TODO: (hours x people x weeks x hourly_cost) - 12 x tool_cost_per_month,
    # rounded to 0 decimals (return an int).
    raise NotImplementedError


def payback_months(setup_cost, monthly_net_saving):
    # TODO: months until savings repay the setup cost, rounded UP to a whole month.
    # Return None if monthly_net_saving <= 0 (it never pays back).
    raise NotImplementedError


def adoption_rate(weekly_active, licensed):
    # TODO: weekly_active is a list of active-user counts per week. Return the
    # latest week's adoption as a percentage of licensed seats, rounded to 1 decimal.
    raise NotImplementedError


def confidence_shift(before, after):
    # TODO: before/after are lists of 1-5 survey scores. Return
    # {"before": avg, "after": avg, "change": after - before}, each rounded to 2 decimals.
    raise NotImplementedError
