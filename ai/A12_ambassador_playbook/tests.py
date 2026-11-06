UCS = [
    {"name": "Meeting notes", "value": 3, "feasibility": 5, "risk": 1},
    {"name": "Auto-approve refunds", "value": 5, "feasibility": 3, "risk": 5},
    {"name": "Survey comment tagging", "value": 4, "feasibility": 4, "risk": 2},
    {"name": "Forecast rewrite", "value": 4, "feasibility": 2, "risk": 2},
    {"name": "Slide fonts", "value": 1, "feasibility": 2, "risk": 1},
]


def test_score_use_case(ex):
    assert ex.score_use_case(UCS[0]) == 3.0, "3*0.5 + 5*0.3 - 0 = 3.0"
    assert ex.score_use_case(UCS[2]) == 3.0, "4*0.5 + 4*0.3 - 1*0.2 = 3.0"
    assert ex.score_use_case(UCS[1]) == 2.6


def test_quadrant(ex):
    assert [ex.quadrant(u) for u in UCS] == ["Quick win", "Avoid", "Quick win", "Strategic bet", "Avoid"]
    assert ex.quadrant({"value": 2, "feasibility": 4, "risk": 1}) == "Fill-in"


def test_prioritise(ex):
    got = ex.prioritise(UCS)
    assert [u["name"] for u in got] == ["Meeting notes", "Survey comment tagging", "Auto-approve refunds",
                                        "Forecast rewrite", "Slide fonts"], [u["name"] for u in got]
    assert got[0]["quadrant"] == "Quick win" and got[0]["score"] == 3.0
    assert "score" not in UCS[0], "don't modify the input"


def test_annual_value(ex):
    assert ex.annual_value(2, 10, 50) == 46000
    assert ex.annual_value(2, 10, 50, tool_cost_per_month=300) == 42400
    assert isinstance(ex.annual_value(1.5, 3, 40.5), int)


def test_payback_months(ex):
    assert ex.payback_months(10000, 3000) == 4
    assert ex.payback_months(9000, 3000) == 3
    assert ex.payback_months(5000, 0) is None


def test_adoption_rate(ex):
    assert ex.adoption_rate([5, 9, 14], 20) == 70.0


def test_confidence_shift(ex):
    assert ex.confidence_shift([2, 3, 2, 1], [4, 4, 3, 4]) == {"before": 2.0, "after": 3.75, "change": 1.75}
