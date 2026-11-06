def test_add_tax(ex):
    assert ex.add_tax(10) == 12.0, f"add_tax(10) should be 12.0, got {ex.add_tax(10)!r}"
    assert abs(ex.add_tax(2.5) - 3.0) < 1e-9, "add_tax(2.5) should be 3.0"


def test_celsius_to_fahrenheit(ex):
    assert ex.celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"
    assert ex.celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert ex.celsius_to_fahrenheit(-40) == -40, "-40°C should be -40°F"


def test_minutes_to_hours_and_minutes(ex):
    got = ex.minutes_to_hours_and_minutes(135)
    assert tuple(got) == (2, 15), f"135 minutes should give (2, 15), got {got!r}"
    assert tuple(ex.minutes_to_hours_and_minutes(59)) == (0, 59), "59 minutes should give (0, 59)"


def test_is_even(ex):
    assert ex.is_even(4) is True, "4 is even"
    assert ex.is_even(7) is False, "7 is odd"
    assert ex.is_even(0) is True, "0 is even"


def test_split_bill(ex):
    assert ex.split_bill(100, 3) == 33.33, f"split_bill(100, 3) should be 33.33, got {ex.split_bill(100, 3)!r}"
    assert ex.split_bill(50, 2) == 25, "split_bill(50, 2) should be 25"


def test_text_to_number_sum(ex):
    got = ex.text_to_number_sum("4", "5")
    assert got == 9, f"expected 9, got {got!r} - did you convert the strings with int()?"


def test_average_of_three(ex):
    assert ex.average_of_three(2, 4, 9) == 5, "average of 2, 4, 9 is 5"
    assert ex.average_of_three(1, 2, 2) == 5 / 3
