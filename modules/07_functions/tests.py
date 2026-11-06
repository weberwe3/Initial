def _need(ex, name):
    if not hasattr(ex, name):
        raise NotImplementedError
    return getattr(ex, name)


def test_greet(ex):
    assert ex.greet("Ada") == "Hello, Ada!"
    assert ex.greet("Ada", "Welcome") == "Welcome, Ada!"
    assert ex.greet(greeting="Hi", name="Bo") == "Hi, Bo!"


def test_compound_interest(ex):
    assert ex.compound_interest(1000, 0.05) == 1050.0
    assert ex.compound_interest(1000, 0.05, 10) == 1628.89


def test_total(ex):
    total = _need(ex, "total")
    assert total(1, 2, 3) == 6
    assert total() == 0
    assert total(5) == 5


def test_parse_expense(ex):
    parse_expense = _need(ex, "parse_expense")
    assert parse_expense("rent, 1200") == ("rent", 1200.0)
    assert parse_expense("  coffee ,3.5 ") == ("coffee", 3.5)


def test_parse_expenses(ex):
    parse_expenses = _need(ex, "parse_expenses")
    got = parse_expenses("rent, 1200\nfood, 350\n")
    assert got == [("rent", 1200.0), ("food", 350.0)], f"got {got!r} (skip empty lines!)"


def test_apply_to_all(ex):
    apply_to_all = _need(ex, "apply_to_all")
    assert apply_to_all(len, ["hi", "bye"]) == [2, 3]
    assert apply_to_all(str.upper, ["a", "b"]) == ["A", "B"]


def test_make_multiplier(ex):
    double = ex.make_multiplier(2)
    assert callable(double), "make_multiplier should return a function"
    assert double(5) == 10
    assert ex.make_multiplier(3)(4) == 12


def test_add_item(ex):
    assert ex.add_item("a") == ["a"]
    assert ex.add_item("b") == ["b"], "the default list is being reused between calls - see the ⚠️ in section 3"
    assert ex.add_item("c", ["x"]) == ["x", "c"]
