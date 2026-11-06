def test_estimate_tokens(ex):
    assert ex.estimate_tokens("abcdefghij") == 3, "10 characters / 4 = 2.5, rounded UP is 3 (math.ceil)"
    assert ex.estimate_tokens("") == 0
    assert ex.estimate_tokens("abcd") == 1


def test_words_to_tokens(ex):
    assert ex.words_to_tokens(750) == 1000
    assert ex.words_to_tokens(1) == 2, "1 / 0.75 = 1.33, rounded up is 2"


def test_fits_in_context(ex):
    doc = "x" * 4000          # ~1000 tokens
    assert ex.fits_in_context([doc, doc], 3000) is True, "2000 + 1000 reserve = 3000 fits exactly"
    assert ex.fits_in_context([doc, doc, doc], 3000) is False
    assert ex.fits_in_context([doc], 1500, reserve_for_answer=600) is False


def test_request_cost(ex):
    assert ex.request_cost(1000, 500, 3.0, 15.0) == 0.0105
    assert ex.request_cost(1_000_000, 0, 2.0, 10.0) == 2.0


def test_monthly_cost(ex):
    got = ex.monthly_cost(200, 1500, 400, 3.0, 15.0)
    assert got == 46.2, f"200/day x 22 days x $0.0105 = $46.20, got {got!r}"
    assert ex.monthly_cost(10, 1000, 500, 3.0, 15.0, working_days=30) == 3.15


def test_cheapest_option(ex):
    options = {"large": (4.0, 20.0), "medium": (2.0, 10.0), "small": (0.1, 0.5)}
    assert ex.cheapest_option(options, 2000, 500) == "small"
    assert ex.cheapest_option({"a": (1.0, 50.0), "b": (5.0, 5.0)}, 100, 1000) == "b", "output tokens can dominate the cost"
