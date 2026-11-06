"""
Module A04 exercises: Analysis you can verify.   Run:  python check.py A4

Data arrives as a list of dicts (one dict per row), the plain-Python version
of a table. These helpers compute the numbers AI must never be trusted to
calculate in its head, and profile data so you can describe it instead of
sending it.
"""


def column(rows, name):
    # TODO: return a list of the values in column `name`, skipping None.
    raise NotImplementedError


def summarize(rows, name):
    # TODO: return {"count", "sum", "mean", "min", "max"} for the numeric column
    # (ignoring None). Round sum and mean to 2 decimals.
    # For an empty column return {"count": 0, "sum": 0, "mean": None, "min": None, "max": None}
    raise NotImplementedError


def group_sum(rows, by, value):
    # TODO: return {group: total of value}, rounded to 2 decimals, groups in
    # first-seen order. Skip rows where value is None.
    raise NotImplementedError


def percent_change(old, new):
    # TODO: return the % change from old to new, rounded to 1 decimal.
    # percent_change(80, 100) -> 25.0 ; return None if old is 0.
    raise NotImplementedError


def verify_claim(rows, value, claimed_total, tolerance_pct=0.5):
    # TODO: an AI says the total of `value` is claimed_total. Return True if
    # the real total is within tolerance_pct percent of the claim.
    # (If the real total is 0, the claim must be exactly 0.)
    raise NotImplementedError


def conversion_rate(rows, group, visits="visits", orders="orders"):
    # TODO: return {group: orders / visits * 100, rounded to 1 decimal},
    # computed from the SUMMED visits and orders of each group, NOT by averaging
    # each row's rate (the classic "average of averages" mistake).
    raise NotImplementedError


def profile(rows):
    # TODO: describe a dataset WITHOUT revealing it. Return one line per column,
    # in the order columns appear in the first row, joined with "\n":
    #   "<name> (<type>): <n_distinct> distinct, <n_missing> missing"
    # <type> is "number" if every non-None value is an int or float, else "text".
    # (bool counts as text here, keep it simple.)
    raise NotImplementedError
