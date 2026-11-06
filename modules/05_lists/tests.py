def test_average(ex):
    assert ex.average([2, 4, 6]) == 4
    assert ex.average([]) == 0, "an empty list should give 0, not a crash"


def test_only_passing(ex):
    scores = [55, 82, 47, 91, 68]
    assert ex.only_passing(scores) == [82, 91, 68]
    assert scores == [55, 82, 47, 91, 68], "don't change the original list!"
    assert ex.only_passing(scores, 90) == [91]


def test_add_tax_to_all(ex):
    assert ex.add_tax_to_all([10, 20], 0.2) == [12.0, 24.0]
    assert ex.add_tax_to_all([4.99], 0.2) == [5.99]


def test_second_largest(ex):
    assert ex.second_largest([4, 9, 2, 9, 7]) == 7
    assert ex.second_largest([1, 2]) == 1


def test_remove_duplicates(ex):
    assert ex.remove_duplicates([3, 1, 3, 2, 1]) == [3, 1, 2], "order must be kept"
    assert ex.remove_duplicates([]) == []


EXPENSES = [("rent", 1200), ("food", 350), ("transport", 90)]


def test_total_expenses(ex):
    assert ex.total_expenses(EXPENSES) == 1640


def test_biggest_expense(ex):
    assert ex.biggest_expense(EXPENSES) == "rent"
    assert ex.biggest_expense([("a", 1), ("b", 5), ("c", 3)]) == "b"


def test_numbered_list(ex):
    assert ex.numbered_list(["milk", "eggs"]) == ["1. milk", "2. eggs"]


def test_chunk(ex):
    assert ex.chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert ex.chunk([1, 2, 3], 3) == [[1, 2, 3]]


def test_column(ex):
    assert ex.column([[1, 2, 3], [4, 5, 6]], 1) == [2, 5]
    assert ex.column([[1, 2, 3], [4, 5, 6]], 0) == [1, 4]
