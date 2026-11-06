import random as _random


def test_days_until(ex):
    assert ex.days_until("2026-11-06", "2026-12-25") == 49
    assert ex.days_until("2026-01-01", "2026-01-01") == 0


def test_add_business_days(ex):
    assert ex.add_business_days("2026-11-06", 1) == "2026-11-09", "Friday + 1 working day is Monday"
    assert ex.add_business_days("2026-11-02", 4) == "2026-11-06"
    assert ex.add_business_days("2026-11-02", 5) == "2026-11-09"


def test_reformat_date(ex):
    assert ex.reformat_date("06/11/2026") == "6 November 2026", f"got {ex.reformat_date('06/11/2026')!r}"
    assert ex.reformat_date("25/12/2026") == "25 December 2026"


def test_top_n_words(ex):
    got = ex.top_n_words("the cat and the hat and the bat", 2)
    assert got == [("the", 3), ("and", 2)], f"got {got!r}"


def test_median_and_mean(ex):
    assert tuple(ex.median_and_mean([1, 2, 3, 10])) == (2.5, 4)


def test_roll_dice(ex):
    rolls = ex.roll_dice(10, 42)
    _random.seed(42)
    expected = [_random.randint(1, 6) for _ in range(10)]
    assert rolls == expected, "seed first, then call random.randint(1, 6) once per roll"


def test_group_words_by_length(ex):
    got = ex.group_words_by_length(["hi", "yo", "cat"])
    assert got == {2: ["hi", "yo"], 3: ["cat"]}
    assert type(got) is dict, "convert to a plain dict before returning"


def test_hypotenuse(ex):
    assert ex.hypotenuse(3, 4) == 5.0
