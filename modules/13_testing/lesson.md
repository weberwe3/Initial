# Module 13: Testing

**Goal:** write automated tests with `pytest` so you *know* your code works,
and can change it without fear.
**Time:** 3–4 hours.

You've been using tests this whole course: `check.py` runs tests against your
exercises. Now you'll write your own.

---

## 1. Why test?

Without tests, every change means manually re-checking everything, or more
likely, not checking and hoping. With tests:

- You find bugs in seconds, not when a user (or you, three weeks later) trips over them.
- You can **refactor**, rewriting code to be cleaner, and know you didn't break it.
- Tests document what your code is supposed to do.

---

## 2. Set up pytest

In your project's virtual environment (Module 10):

```bash
pip install pytest
```

---

## 3. Your first test

`pricing.py`:
```python
def apply_discount(price, percent):
    return round(price * (1 - percent / 100), 2)
```

`test_pricing.py`:
```python
from pricing import apply_discount

def test_ten_percent_off():
    assert apply_discount(100, 10) == 90

def test_zero_discount_changes_nothing():
    assert apply_discount(59.99, 0) == 59.99
```

Run:
```bash
pytest            # finds every test_*.py file and every test_* function
pytest -v         # verbose: lists each test
pytest -x         # stop at the first failure
pytest -k discount  # only tests whose name contains "discount"
```

A test is just a function whose name starts with `test_` and that uses
`assert`. If the assert is false, pytest shows you exactly what the values were.

---

## 4. What to test

For each function, think of:

1. **The normal case:** typical inputs.
2. **Edge cases:** zero, empty list, one item, exactly-on-the-boundary values.
3. **Error cases:** bad input that should raise an error.

**Boundaries are where bugs live.** If shipping is free "at $50 or more",
test $49.99, $50.00 and $50.01.

---

## 5. Testing that errors are raised

```python
import pytest
from pricing import apply_discount

def test_discount_over_100_is_rejected():
    with pytest.raises(ValueError):
        apply_discount(100, 150)
```

The test passes only if a `ValueError` is raised inside the `with` block.

---

## 6. Comparing floats

```python
assert 0.1 + 0.2 == 0.3          # FAILS! (0.30000000000000004)
assert 0.1 + 0.2 == pytest.approx(0.3)   # passes
```

Computers store decimals in binary, so tiny rounding errors happen. Use
`pytest.approx` for float results, or store money as whole cents.

---

## 7. Many cases at once: `parametrize`

```python
import pytest
from pricing import shipping

@pytest.mark.parametrize("total, expected", [
    (10, 4.99),
    (49.99, 4.99),
    (50, 0),
    (200, 0),
])
def test_shipping(total, expected):
    assert shipping(total) == expected
```

One function, four tests. Each runs and reports separately.

---

## 8. Fixtures: shared setup

```python
import pytest
from budget import Budget, Expense

@pytest.fixture
def budget():
    b = Budget(limit=100)
    b.add(Expense("Lunch", 20, "food"))
    return b

def test_total(budget):           # pytest passes the fixture in by name
    assert budget.total() == 20

def test_remaining(budget):       # each test gets a FRESH budget
    assert budget.remaining() == 80
```

`tmp_path` is a built-in fixture that gives each test a fresh empty folder,
which is perfect for testing file code:

```python
def test_save_and_load(tmp_path):
    path = tmp_path / "data.json"
    save_json(path, {"a": 1})
    assert load_json(path) == {"a": 1}
```

---

## 9. Writing code that's easy to test

You've already been doing this:

- **Return values instead of printing.** You can't easily assert on a print.
- **Pass things in as parameters** (file paths, today's date, prices) instead
  of hard-coding or reading `input()` inside the logic.
- **Keep functions small** with one job each.

If something is hard to test, that's usually a sign the design could be simpler.

### Test-driven development (TDD), briefly
1. Write a failing test for the behaviour you want.
2. Write the simplest code that makes it pass.
3. Clean up the code, with the test keeping you safe.

Try it on Project 2.

---

## 10. This module's exercise: test the tests

`pricing.py` in this folder has three working functions. Your job is to write
tests for them in `exercises.py`.

The checker then does something sneaky: it **plants bugs** in `pricing.py`
(off-by-one boundaries, missing validation, wrong maths) and checks whether
your tests catch each one. This is called *mutation testing*, and it measures
whether your tests are actually any good.

```bash
pip install pytest
pytest modules/13_testing/exercises.py -v   # run your tests normally
python check.py 13                          # see which planted bugs you catch
```

---

## Key takeaways
- A test is a `test_` function with `assert`. Run them with `pytest`.
- Test normal cases, **boundaries**, and errors (`pytest.raises`).
- `pytest.approx` for floats; `parametrize` for many cases; fixtures for setup.
- Testable code returns values and takes its inputs as parameters.

**Continue reading:** [Get Started](https://docs.pytest.org/en/stable/getting-started.html) (the pytest documentation). Install pytest, write your first tests, and learn fixtures from the source.

**Next:** [Module 14: Working with the web](../14_web_apis/lesson.md)
