ORDERS = [
    {"order_id": 1, "region": "North", "amount": 120.0, "product_id": "P1"},
    {"order_id": 2, "region": "South", "amount": 80.0, "product_id": "P2"},
    {"order_id": 3, "region": "North", "amount": 45.5, "product_id": "P9"},
]
PRODUCTS = [
    {"product_id": "P1", "name": "Widget", "region": "Global"},
    {"product_id": "P2", "name": "Gadget", "region": "Global"},
    {"product_id": "P3", "name": "Doohickey", "region": "Global"},
]


def _snapshot(rows):
    return [dict(r) for r in rows]


def test_select(ex):
    got = ex.select([{"a": 1, "b": 2, "c": 3}], ["c", "a"], {"a": "A"})
    assert got == [{"c": 3, "A": 1}] and list(got[0]) == ["c", "A"], f"got {got!r}"
    assert ex.select([{"a": 1, "b": 2}], ["b"]) == [{"b": 2}]


def test_filter_rows(ex):
    before = _snapshot(ORDERS)
    t, f = ex.filter_rows(ORDERS, lambda r: r["amount"] > 100)
    assert [r["order_id"] for r in t] == [1] and [r["order_id"] for r in f] == [2, 3]
    assert ORDERS == before


def test_formula(ex):
    before = _snapshot(ORDERS)
    got = ex.formula(ORDERS, "with_tax", lambda r: round(r["amount"] * 1.2, 2))
    assert [r["with_tax"] for r in got] == [144.0, 96.0, 54.6]
    assert ORDERS == before, "Formula must not modify its input rows"


def test_unique(ex):
    rows = [{"c": "A", "d": 1}, {"c": "B", "d": 1}, {"c": "A", "d": 1}, {"c": "A", "d": 2}]
    u, d = ex.unique(rows, ["c", "d"])
    assert u == [{"c": "A", "d": 1}, {"c": "B", "d": 1}, {"c": "A", "d": 2}]
    assert d == [{"c": "A", "d": 1}]


def test_join(ex):
    before = _snapshot(ORDERS)
    j, l, r = ex.join(ORDERS, PRODUCTS, "product_id")
    assert [x["order_id"] for x in j] == [1, 2]
    assert j[0] == {"order_id": 1, "region": "North", "amount": 120.0, "product_id": "P1",
                    "name": "Widget", "Right_region": "Global"}, f"J row was {j[0]!r}"
    assert [x["order_id"] for x in l] == [3], "order 3 has no product: L anchor"
    assert [x["product_id"] for x in r] == ["P3"], "P3 was never ordered: R anchor"
    assert ORDERS == before


def test_join_many_matches(ex):
    j, l, r = ex.join([{"k": 1}], [{"k": 1, "v": "a"}, {"k": 1, "v": "b"}], "k")
    assert j == [{"k": 1, "v": "a"}, {"k": 1, "v": "b"}] and l == [] and r == []


def test_union(ex):
    got = ex.union([{"a": 1}], [{"a": 2}], [{"a": 3}])
    assert got == [{"a": 1}, {"a": 2}, {"a": 3}]


def test_summarize(ex):
    assert ex.summarize(ORDERS, "region", "amount", "sum") == [
        {"region": "North", "Sum_amount": 165.5}, {"region": "South", "Sum_amount": 80.0}]
    assert ex.summarize(ORDERS, "region", "amount", "count") == [
        {"region": "North", "Count_amount": 2}, {"region": "South", "Count_amount": 1}]
    assert ex.summarize(ORDERS, "region", "amount", "avg")[0] == {"region": "North", "Avg_amount": 82.75}
    assert ex.summarize(ORDERS, "region", "amount", "max")[0]["Max_amount"] == 120.0


def test_multi_row(ex):
    rows = [{"m": 1, "x": 10}, {"m": 2, "x": 5}, {"m": 3, "x": 7}]
    got = ex.multi_row(rows, "rt", lambda prev, r: r["x"] + (prev["rt"] if prev else 0))
    assert [r["rt"] for r in got] == [10, 15, 22]
    chg = ex.multi_row(rows, "chg", lambda prev, r: None if prev is None else r["x"] - prev["x"])
    assert [r["chg"] for r in chg] == [None, -5, 2]
    assert "rt" not in rows[0], "don't modify the input rows"


def test_cross_tab(ex):
    sales = [
        {"region": "North", "quarter": "Q1", "amount": 60},
        {"region": "North", "quarter": "Q2", "amount": 50},
        {"region": "South", "quarter": "Q2", "amount": 70},
        {"region": "North", "quarter": "Q1", "amount": 40},
    ]
    got = ex.cross_tab(sales, "region", "quarter", "amount")
    assert got == [{"region": "North", "Q1": 100, "Q2": 50}, {"region": "South", "Q1": 0, "Q2": 70}], f"got {got!r}"
