"""Module A04 solutions."""


def column(rows, name):
    return [r[name] for r in rows if r.get(name) is not None]


def summarize(rows, name):
    values = column(rows, name)
    if not values:
        return {"count": 0, "sum": 0, "mean": None, "min": None, "max": None}
    total = sum(values)
    return {"count": len(values), "sum": round(total, 2), "mean": round(total / len(values), 2),
            "min": min(values), "max": max(values)}


def group_sum(rows, by, value):
    totals = {}
    for r in rows:
        if r.get(value) is None:
            continue
        totals[r[by]] = totals.get(r[by], 0) + r[value]
    return {k: round(v, 2) for k, v in totals.items()}


def percent_change(old, new):
    if old == 0:
        return None
    return round((new - old) / old * 100, 1)


def verify_claim(rows, value, claimed_total, tolerance_pct=0.5):
    actual = sum(column(rows, value))
    if actual == 0:
        return claimed_total == 0
    return abs(claimed_total - actual) / abs(actual) * 100 <= tolerance_pct


def conversion_rate(rows, group, visits="visits", orders="orders"):
    v, o = {}, {}
    for r in rows:
        g = r[group]
        v[g] = v.get(g, 0) + r[visits]
        o[g] = o.get(g, 0) + r[orders]
    return {g: round(o[g] / v[g] * 100, 1) for g in v}


def profile(rows):
    lines = []
    for name in rows[0]:
        values = [r.get(name) for r in rows]
        present = [x for x in values if x is not None]
        is_number = bool(present) and all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in present)
        lines.append(f"{name} ({'number' if is_number else 'text'}): "
                     f"{len(set(present))} distinct, {len(values) - len(present)} missing")
    return "\n".join(lines)
