"""
Module A05 exercises: Build the Alteryx toolbox in Python.   Run:  python check.py A5

Each function is one Alteryx tool. Tables are lists of dicts. Every tool must
return NEW rows and never modify its input (just like Alteryx never changes
the upstream data). Tip: {**row} copies a dict.
"""


def select(rows, fields, rename=None):
    # SELECT tool: keep only `fields` (in that order), optionally renaming some.
    # rename is a dict {old_name: new_name}.
    # select([{"a":1,"b":2,"c":3}], ["c","a"], {"a":"A"}) -> [{"c":3, "A":1}]
    raise NotImplementedError


def filter_rows(rows, condition):
    # FILTER tool: return (true_rows, false_rows) - the T and F anchors.
    # condition is a function: row -> bool
    raise NotImplementedError


def formula(rows, field, expression):
    # FORMULA tool: return new rows with `field` set to expression(row).
    raise NotImplementedError


def unique(rows, keys):
    # UNIQUE tool: return (unique_rows, duplicate_rows). A row is a duplicate if
    # the combination of values in `keys` (a list of field names) was already seen.
    # The first occurrence goes to unique_rows.
    raise NotImplementedError


def join(left, right, key):
    # JOIN tool: return (J, L, R)
    #   J: for each left row with a matching right row, a merged dict
    #      (right's fields are added; if a field name exists in both, prefix the
    #      right one with "Right_", except the key itself which appears once).
    #      If several right rows match, produce one J row per match.
    #   L: left rows with no match.   R: right rows with no match.
    raise NotImplementedError


def union(*tables):
    # UNION tool: stack all tables into one new list (copies of the rows).
    raise NotImplementedError


def summarize(rows, group_by, field, action):
    # SUMMARIZE tool: group by one field and aggregate `field`.
    # action is one of "sum", "count", "avg", "min", "max".
    # Return a list of dicts like {group_by: <group>, "<Action>_<field>": value}
    # e.g. {"region": "North", "Sum_amount": 165.5}. Action is capitalised.
    # Groups in first-seen order. Round avg to 2 decimals.
    raise NotImplementedError


def multi_row(rows, field, expression):
    # MULTI-ROW FORMULA tool: new rows with field = expression(previous_row, row),
    # where previous_row is the previous NEW row (already holding its computed
    # field), or None for the first row.
    # Running total: multi_row(rows, "rt", lambda prev, r: r["x"] + (prev["rt"] if prev else 0))
    raise NotImplementedError


def cross_tab(rows, group_field, header_field, value_field):
    # CROSS TAB tool (sum): one output row per group_field value, with one column
    # per distinct header_field value holding the summed value_field.
    # Missing combinations get 0. Groups and headers in first-seen order.
    # cross_tab(sales, "region", "quarter", "amount") ->
    #   [{"region": "North", "Q1": 100, "Q2": 50}, {"region": "South", "Q1": 0, "Q2": 70}]
    raise NotImplementedError
