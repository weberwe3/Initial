"""Module A11 solutions."""

import math


def score_use_case(uc):
    return round(uc["value"] * 0.5 + uc["feasibility"] * 0.3 - (uc["risk"] - 1) * 0.2, 2)


def quadrant(uc):
    if uc.get("risk", 1) >= 5:
        return "Avoid"
    high_value, feasible = uc["value"] >= 3, uc["feasibility"] >= 3
    if high_value and feasible:
        return "Quick win"
    if high_value:
        return "Strategic bet"
    if feasible:
        return "Fill-in"
    return "Avoid"


def prioritise(use_cases):
    scored = [{**uc, "score": score_use_case(uc), "quadrant": quadrant(uc)} for uc in use_cases]
    return sorted(scored, key=lambda uc: -uc["score"])


def annual_value(hours_saved_per_week, people, hourly_cost, weeks=46, tool_cost_per_month=0):
    return int(round(hours_saved_per_week * people * weeks * hourly_cost - 12 * tool_cost_per_month))


def payback_months(setup_cost, monthly_net_saving):
    if monthly_net_saving <= 0:
        return None
    return math.ceil(setup_cost / monthly_net_saving)


def adoption_rate(weekly_active, licensed):
    return round(weekly_active[-1] / licensed * 100, 1)


def confidence_shift(before, after):
    b, a = sum(before) / len(before), sum(after) / len(after)
    return {"before": round(b, 2), "after": round(a, 2), "change": round(a - b, 2)}
