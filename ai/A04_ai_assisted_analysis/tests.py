ROWS = [
    {"region": "North", "revenue": 120.0, "visits": 100, "orders": 10},
    {"region": "South", "revenue": 80.5, "visits": 50, "orders": 10},
    {"region": "North", "revenue": None, "visits": 300, "orders": 6},
    {"region": "East", "revenue": 50.0, "visits": 10, "orders": 5},
]


def test_column(ex):
    assert ex.column(ROWS, "revenue") == [120.0, 80.5, 50.0]
    assert ex.column(ROWS, "region") == ["North", "South", "North", "East"]


def test_summarize(ex):
    got = ex.summarize(ROWS, "revenue")
    assert got == {"count": 3, "sum": 250.5, "mean": 83.5, "min": 50.0, "max": 120.0}, f"got {got!r}"
    assert ex.summarize([], "revenue") == {"count": 0, "sum": 0, "mean": None, "min": None, "max": None}


def test_group_sum(ex):
    assert ex.group_sum(ROWS, "region", "revenue") == {"North": 120.0, "South": 80.5, "East": 50.0}
    assert list(ex.group_sum(ROWS, "region", "visits")) == ["North", "South", "East"], "keep first-seen order"


def test_percent_change(ex):
    assert ex.percent_change(80, 100) == 25.0
    assert ex.percent_change(200, 150) == -25.0
    assert ex.percent_change(0, 10) is None


def test_verify_claim(ex):
    assert ex.verify_claim(ROWS, "revenue", 250.5) is True
    assert ex.verify_claim(ROWS, "revenue", 251.0) is True, "0.2% off is inside the default 0.5% tolerance"
    assert ex.verify_claim(ROWS, "revenue", 260.0) is False, "an AI's 260 is ~3.8% off: reject it"
    assert ex.verify_claim([{"revenue": 0}], "revenue", 0) is True


def test_conversion_rate(ex):
    got = ex.conversion_rate(ROWS, "region")
    assert got == {"North": 4.0, "South": 20.0, "East": 50.0}, (
        f"got {got!r}. North is (10+6)/(100+300) = 4.0%, not the average of 10% and 2% (6%)")


def test_profile(ex):
    got = ex.profile(ROWS).split("\n")
    assert got[0] == "region (text): 3 distinct, 0 missing", got[0]
    assert got[1] == "revenue (number): 3 distinct, 1 missing", got[1]
    assert len(got) == 4
