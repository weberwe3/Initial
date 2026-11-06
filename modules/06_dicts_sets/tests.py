PEOPLE = [
    {"name": "Ada", "dept": "Eng", "salary": 90000},
    {"name": "Grace", "dept": "Eng", "salary": 110000},
    {"name": "Linus", "dept": "Support", "salary": 60000},
]


def test_word_counts(ex):
    assert ex.word_counts("The cat the") == {"the": 2, "cat": 1}
    assert ex.word_counts("") == {}


def test_most_common_word(ex):
    assert ex.most_common_word("the cat and the hat") == "the"
    assert ex.most_common_word("b a a b") == "a", "on a tie, the word that reached the top count first wins ('a' hits 2 before 'b' does)"


def test_totals_by_category(ex):
    got = ex.totals_by_category([("food", 12.5), ("rent", 1200), ("food", 30)])
    assert got == {"food": 42.5, "rent": 1200}, f"got {got!r}"


def test_invert(ex):
    assert ex.invert({"a": 1, "b": 2}) == {1: "a", 2: "b"}


def test_lookup_price(ex):
    assert ex.lookup_price({"milk": 1.1}, "milk") == 1.1
    assert ex.lookup_price({"milk": 1.1}, "caviar") == 0


def test_cart_total(ex):
    prices = {"apple": 0.5, "bread": 2.25}
    assert ex.cart_total(prices, {"apple": 4, "bread": 1}) == 4.25
    assert ex.cart_total(prices, {"apple": 1, "unicorn": 3}) == 0.5


def test_names_in_dept(ex):
    assert ex.names_in_dept(PEOPLE, "Eng") == ["Ada", "Grace"]
    assert ex.names_in_dept(PEOPLE, "Sales") == []


def test_average_salary_by_dept(ex):
    assert ex.average_salary_by_dept(PEOPLE) == {"Eng": 100000, "Support": 60000}


def test_unique_count(ex):
    assert ex.unique_count([1, 1, 2]) == 2
    assert ex.unique_count(["a", "b", "a", "c"]) == 3


def test_missing_skills(ex):
    got = ex.missing_skills(["python", "excel"], ["sql", "python", "aws"])
    assert got == ["aws", "sql"], f"got {got!r} (should be sorted)"


def test_group_by_first_letter(ex):
    got = ex.group_by_first_letter(["apple", "Avocado", "banana"])
    assert got == {"a": ["apple", "Avocado"], "b": ["banana"]}, f"got {got!r}"
