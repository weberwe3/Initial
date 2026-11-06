"""
Checks for Module 13. This uses "mutation testing": it plants bugs in
pricing.py and re-runs YOUR tests to see whether they notice.
"""

import importlib.util
import itertools
import sys
import types
from pathlib import Path

HERE = Path(__file__).parent


def _load_pricing():
    spec = importlib.util.spec_from_file_location("pricing", HERE / "pricing.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _expand(fn):
    """Yield argument-dicts for a test function, honouring @pytest.mark.parametrize."""
    marks = [m for m in getattr(fn, "pytestmark", []) if m.name == "parametrize"]
    if not marks:
        yield {}
        return
    groups = []
    for m in marks:
        names = m.args[0]
        names = [n.strip() for n in names.split(",")] if isinstance(names, str) else list(names)
        rows = []
        for values in m.args[1]:
            values = getattr(values, "values", values)  # pytest.param(...)
            if len(names) == 1:
                values = (values,)
            rows.append(dict(zip(names, values)))
        groups.append(rows)
    for combo in itertools.product(*groups):
        merged = {}
        for d in combo:
            merged.update(d)
        yield merged


def _run_student_tests(ex_path, pricing_module):
    """Run the student's tests against pricing_module. Return list of failures."""
    old = sys.modules.get("pricing")
    sys.modules["pricing"] = pricing_module
    sys.path.insert(0, str(HERE))
    try:
        spec = importlib.util.spec_from_file_location("student_tests_13", ex_path)
        student = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(student)
        tests = [(n, f) for n, f in vars(student).items() if n.startswith("test_") and callable(f)]
        if not tests:
            raise NotImplementedError
        failures = []
        for name, fn in tests:
            for kwargs in _expand(fn):
                try:
                    fn(**kwargs)
                except NotImplementedError:
                    raise
                except (Exception, BaseException) as e:  # pytest's Failed is a BaseException
                    if isinstance(e, KeyboardInterrupt):
                        raise
                    failures.append((name, e))
        return failures
    finally:
        sys.path.pop(0)
        if old is None:
            sys.modules.pop("pricing", None)
        else:
            sys.modules["pricing"] = old


def _mutant(**replacements):
    real = _load_pricing()
    m = types.ModuleType("pricing")
    m.__dict__.update({k: v for k, v in vars(real).items() if not k.startswith("__")})
    m.__dict__.update(replacements)
    return m


def _must_catch(ex, mutant, hint):
    failures = _run_student_tests(ex.__file__, mutant)
    assert failures, f"your tests didn't notice this planted bug: {hint}"


# --------------------------------------------------------------------------


def test_your_tests_pass_on_the_real_code(ex):
    failures = _run_student_tests(ex.__file__, _load_pricing())
    assert not failures, (
        f"{failures[0][0]} failed against the CORRECT pricing.py: "
        f"{type(failures[0][1]).__name__}: {failures[0][1]}"
    )


def test_catches_wrong_discount_maths(ex):
    def apply_discount(price, percent):
        if not 0 <= percent <= 100:
            raise ValueError
        return round(price * (1 - percent / 1000), 2)
    _must_catch(ex, _mutant(apply_discount=apply_discount), "discount divided by 1000 instead of 100")


def test_catches_missing_validation(ex):
    def apply_discount(price, percent):
        return round(price * (1 - percent / 100), 2)
    _must_catch(ex, _mutant(apply_discount=apply_discount), "apply_discount accepts percent=150")


def test_catches_off_by_one_upper_limit(ex):
    def apply_discount(price, percent):
        if not 0 <= percent < 100:
            raise ValueError
        return round(price * (1 - percent / 100), 2)
    _must_catch(ex, _mutant(apply_discount=apply_discount), "a 100% discount is wrongly rejected")


def test_catches_shipping_boundary_bug(ex):
    def shipping(order_total):
        return 0 if order_total > 50 else 4.99
    _must_catch(ex, _mutant(shipping=shipping), "shipping isn't free at exactly $50")


def test_catches_shipping_always_free(ex):
    def shipping(order_total):
        return 0
    _must_catch(ex, _mutant(shipping=shipping), "shipping is always free")


def test_catches_parse_price_ignoring_commas(ex):
    def parse_price(text):
        return float(text.strip().replace("$", ""))
    _must_catch(ex, _mutant(parse_price=parse_price), "parse_price crashes on '1,234.50'")


def test_catches_parse_price_ignoring_dollar(ex):
    def parse_price(text):
        return float(text.strip().replace(",", ""))
    _must_catch(ex, _mutant(parse_price=parse_price), "parse_price crashes on '$5'")


def test_catches_parse_price_swallowing_errors(ex):
    def parse_price(text):
        try:
            return float(text.strip().replace("$", "").replace(",", ""))
        except ValueError:
            return 0.0
    _must_catch(ex, _mutant(parse_price=parse_price), "parse_price returns 0.0 for garbage instead of raising")
