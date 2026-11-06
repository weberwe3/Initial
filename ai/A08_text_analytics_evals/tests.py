import random as _random

GOLD = ["price", "delivery", "other", "delivery", "quality", "delivery"]
PRED = ["price", "other", "other", "delivery", "delivery", "delivery"]


def test_accuracy(ex):
    assert ex.accuracy(PRED, GOLD) == 0.667
    try:
        ex.accuracy(["a"], ["a", "b"])
    except ValueError:
        pass
    else:
        raise AssertionError("different lengths should raise ValueError")


def test_confusion_matrix(ex):
    got = ex.confusion_matrix(PRED, GOLD)
    assert got == {("price", "price"): 1, ("delivery", "other"): 1, ("other", "other"): 1,
                   ("delivery", "delivery"): 2, ("quality", "delivery"): 1}, f"got {got!r}"


def test_precision_recall(ex):
    assert ex.precision_recall(PRED, GOLD, "delivery") == (0.667, 0.667), "3 predicted delivery, 2 right; 3 real delivery, 2 caught"
    assert ex.precision_recall(PRED, GOLD, "quality") == (0.0, 0.0)
    assert ex.precision_recall(PRED, GOLD, "other") == (0.5, 1.0)


def test_label_distribution(ex):
    got = ex.label_distribution(GOLD)
    assert got == {"delivery": 50.0, "price": 16.7, "other": 16.7, "quality": 16.7}, f"got {got!r}"
    assert list(got)[0] == "delivery"


def test_disagreements(ex):
    rows = [{"id": i, "pred": p, "gold": g} for i, (p, g) in enumerate(zip(PRED, GOLD))]
    assert [r["id"] for r in ex.disagreements(rows)] == [1, 4]


def test_keyword_baseline(ex):
    rules = [("delivery", ["late", "shipping", "arrived"]), ("price", ["expensive", "price", "cost"])]
    assert ex.keyword_baseline("Arrived LATE again", rules) == "delivery"
    assert ex.keyword_baseline("Too expensive for what it is", rules) == "price"
    assert ex.keyword_baseline("Shipping cost was high", rules) == "delivery", "rules are checked in order"
    assert ex.keyword_baseline("Love it", rules) == "other"


def test_sample_for_gold(ex):
    rows = list(range(100))
    a = ex.sample_for_gold(rows, 5, seed=7)
    assert a == _random.Random(7).sample(rows, 5)
    assert ex.sample_for_gold(rows, 5, seed=7) == a, "same seed, same sample"
    assert ex.sample_for_gold([1, 2], 10) == [1, 2]
