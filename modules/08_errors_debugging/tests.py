def _raises(fn, *args):
    try:
        fn(*args)
    except ValueError:
        return True
    except NotImplementedError:
        raise
    return False


def test_safe_int(ex):
    assert ex.safe_int("42") == 42
    assert ex.safe_int("hello") == 0
    assert ex.safe_int("3.5", -1) == -1


def test_safe_divide(ex):
    assert ex.safe_divide(10, 4) == 2.5
    assert ex.safe_divide(1, 0) is None


def test_get_setting(ex):
    s = {"theme": "dark"}
    assert ex.get_setting(s, "theme") == "dark"
    assert ex.get_setting(s, "font") is None
    assert ex.get_setting(s, "font", "Arial") == "Arial"


def test_withdraw(ex):
    assert ex.withdraw(100, 30) == 70
    assert _raises(ex.withdraw, 100, 0), "withdrawing 0 should raise ValueError"
    assert _raises(ex.withdraw, 100, -5), "withdrawing a negative should raise ValueError"
    assert _raises(ex.withdraw, 100, 500), "overdrawing should raise ValueError"


def test_parse_age(ex):
    assert ex.parse_age("36") == 36
    assert _raises(ex.parse_age, "old"), "'old' should raise ValueError"
    assert _raises(ex.parse_age, "200"), "200 is out of range - raise ValueError"
    assert _raises(ex.parse_age, "-1"), "-1 is out of range - raise ValueError"


def test_sum_valid_numbers(ex):
    assert ex.sum_valid_numbers(["1", "two", "2.5", ""]) == 3.5


def test_buggy_total(ex):
    assert ex.buggy_total([1, 2, 3]) == 6, "look at the indentation of the return"


def test_buggy_count_to(ex):
    assert ex.buggy_count_to(3) == [1, 2, 3], "classic off-by-one: where does range stop?"


def test_buggy_shout(ex):
    assert ex.buggy_shout("  hi  ") == "HI", "strings are immutable - store the result"


def test_buggy_largest(ex):
    assert ex.buggy_largest([3, 7, 2]) == 7
    assert ex.buggy_largest([-5, -2, -9]) == -2, "what's wrong with starting at 0?"


def test_buggy_describe(ex):
    assert ex.buggy_describe("Ada", 36) == "Ada is 36 years old", "TypeError: you can't + a str and an int"
