"""Module A05 solutions."""


def select(rows, fields, rename=None):
    rename = rename or {}
    return [{rename.get(f, f): row[f] for f in fields} for row in rows]


def filter_rows(rows, condition):
    true_rows = [{**r} for r in rows if condition(r)]
    false_rows = [{**r} for r in rows if not condition(r)]
    return true_rows, false_rows


def formula(rows, field, expression):
    return [{**r, field: expression(r)} for r in rows]


def unique(rows, keys):
    seen = set()
    uniq, dupes = [], []
    for r in rows:
        k = tuple(r[f] for f in keys)
        (dupes if k in seen else uniq).append({**r})
        seen.add(k)
    return uniq, dupes


def join(left, right, key):
    index = {}
    for r in right:
        index.setdefault(r[key], []).append(r)
    joined, left_only, matched_keys = [], [], set()
    for l in left:
        matches = index.get(l[key])
        if not matches:
            left_only.append({**l})
            continue
        matched_keys.add(l[key])
        for r in matches:
            merged = {**l}
            for k, v in r.items():
                if k == key:
                    continue
                merged[f"Right_{k}" if k in l else k] = v
            joined.append(merged)
    right_only = [{**r} for r in right if r[key] not in matched_keys]
    return joined, left_only, right_only


def union(*tables):
    return [{**r} for table in tables for r in table]


def summarize(rows, group_by, field, action):
    groups = {}
    for r in rows:
        groups.setdefault(r[group_by], []).append(r[field])
    funcs = {"sum": sum, "count": len, "avg": lambda v: round(sum(v) / len(v), 2), "min": min, "max": max}
    name = f"{action.capitalize()}_{field}"
    return [{group_by: g, name: funcs[action](values)} for g, values in groups.items()]


def multi_row(rows, field, expression):
    out, prev = [], None
    for r in rows:
        new = {**r}
        new[field] = expression(prev, r)
        out.append(new)
        prev = new
    return out


def cross_tab(rows, group_field, header_field, value_field):
    headers, table = [], {}
    for r in rows:
        if r[header_field] not in headers:
            headers.append(r[header_field])
        cell = table.setdefault(r[group_field], {})
        cell[r[header_field]] = cell.get(r[header_field], 0) + r[value_field]
    return [{group_field: g, **{h: cells.get(h, 0) for h in headers}} for g, cells in table.items()]
