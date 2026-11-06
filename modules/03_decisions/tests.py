def test_grade(ex):
    cases = {95: "A", 90: "A", 89: "B", 80: "B", 75: "C", 60: "D", 59: "F", 0: "F"}
    for score, expected in cases.items():
        got = ex.grade(score)
        assert got == expected, f"grade({score}) should be {expected!r}, got {got!r}"


def test_fizzbuzz_word(ex):
    cases = {15: "FizzBuzz", 30: "FizzBuzz", 9: "Fizz", 10: "Buzz", 7: "7"}
    for n, expected in cases.items():
        got = ex.fizzbuzz_word(n)
        assert got == expected, f"fizzbuzz_word({n}) should be {expected!r}, got {got!r} (check the order of your ifs)"


def test_can_vote(ex):
    assert ex.can_vote(18, True) is True
    assert ex.can_vote(17, True) is False
    assert ex.can_vote(30, False) is False


def test_is_weekend(ex):
    assert ex.is_weekend("Sunday") is True
    assert ex.is_weekend("SATURDAY") is True
    assert ex.is_weekend("monday") is False


def test_shipping_cost(ex):
    assert ex.shipping_cost(50, "US") == 0
    assert ex.shipping_cost(49.99, "US") == 5.99
    assert ex.shipping_cost(10, "CA") == 12.0
    assert ex.shipping_cost(10, "MX") == 12.0
    assert ex.shipping_cost(1000, "FR") == 25.0


def test_bmi_category(ex):
    assert ex.bmi_category(50, 1.8) == "underweight"
    assert ex.bmi_category(70, 1.75) == "normal"
    assert ex.bmi_category(85, 1.75) == "overweight"
    assert ex.bmi_category(110, 1.75) == "obese"


def test_is_leap_year(ex):
    for year, expected in {2024: True, 1900: False, 2000: True, 2023: False}.items():
        got = ex.is_leap_year(year)
        assert got == expected, f"is_leap_year({year}) should be {expected}, got {got!r}"


def test_password_strength(ex):
    assert ex.password_strength("abc") == "weak"
    assert ex.password_strength("abcdefgh") == "medium"
    assert ex.password_strength("12345678") == "medium"
    assert ex.password_strength("abc12345") == "strong"
