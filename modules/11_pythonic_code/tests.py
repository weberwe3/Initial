PEOPLE = [
    {"name": "Ada", "age": 36, "dept": "Eng", "salary": 90000},
    {"name": "Grace", "age": 45, "dept": "Eng", "salary": 110000},
    {"name": "Linus", "age": 28, "dept": "Support", "salary": 60000},
    {"name": "Barbara", "age": 50, "dept": "Admin", "salary": 70000},
]


def test_squares_of_odds(ex):
    assert ex.squares_of_odds([1, 2, 3, 4, 5]) == [1, 9, 25]


def test_pass_fail_labels(ex):
    assert ex.pass_fail_labels([70, 40, 50]) == ["pass", "fail", "pass"]


def test_word_lengths(ex):
    assert ex.word_lengths(["hi", "hello"]) == {"hi": 2, "hello": 5}


def test_unique_domains(ex):
    assert ex.unique_domains(["a@x.com", "b@x.com", "c@y.org"]) == {"x.com", "y.org"}


def test_food_total(ex):
    rows = [{"category": "food", "amount": 10}, {"category": "rent", "amount": 500},
            {"category": "food", "amount": 5.5}]
    assert ex.food_total(rows) == 15.5


def test_has_negative(ex):
    assert ex.has_negative([3, -1, 4]) is True
    assert ex.has_negative([3, 1, 4]) is False


def test_pair_up(ex):
    assert ex.pair_up(["Ada", "Bo"], [95, 80]) == {"Ada": 95, "Bo": 80}


def test_sort_case_insensitive(ex):
    assert ex.sort_case_insensitive(["banana", "Apple", "cherry"]) == ["Apple", "banana", "cherry"]


def test_oldest_person(ex):
    assert ex.oldest_person(PEOPLE) == "Barbara"


def test_sort_by_dept_then_salary(ex):
    got = ex.sort_by_dept_then_salary(PEOPLE)
    assert got == ["Barbara", "Grace", "Ada", "Linus"], f"got {got!r}"


def test_top_expenses(ex):
    exp = [("food", 350), ("rent", 1200), ("fun", 80), ("travel", 600)]
    assert ex.top_expenses(exp, 2) == [("rent", 1200), ("travel", 600)]


def test_flatten(ex):
    assert ex.flatten([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]


def test_merge_settings(ex):
    d = {"theme": "light", "size": 12}
    o = {"theme": "dark"}
    assert ex.merge_settings(d, o) == {"theme": "dark", "size": 12}
    assert d == {"theme": "light", "size": 12}, "don't modify the defaults"
