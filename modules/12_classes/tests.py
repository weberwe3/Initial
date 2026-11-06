import dataclasses


def _need(ex, name):
    obj = getattr(ex, name, None)
    if obj is None:
        raise NotImplementedError
    return obj


def _raises(fn, *args):
    try:
        fn(*args)
    except ValueError:
        return True
    return False


def test_bank_account(ex):
    BankAccount = _need(ex, "BankAccount")
    if not hasattr(BankAccount, "deposit"):
        raise NotImplementedError
    a = BankAccount("Ada", 100)
    a.deposit(50)
    a.withdraw(30)
    assert a.balance == 120
    assert str(a) == "Ada: $120.00", f"str() gave {str(a)!r}"
    assert BankAccount("Bo").balance == 0, "balance should default to 0"
    assert _raises(a.deposit, 0), "deposit(0) should raise ValueError"
    assert _raises(a.withdraw, 1000), "overdrawing should raise ValueError"
    assert a.history == [("deposit", 50), ("withdraw", 30)], f"history was {a.history!r}"
    b = BankAccount("Cy")
    assert b.history == [], "each account needs its own history list"


def test_money(ex):
    Money = _need(ex, "Money")
    if not hasattr(Money, "__init__") or Money.__init__ is object.__init__:
        raise NotImplementedError
    assert str(Money(1234)) == "$12.34"
    assert Money(100) + Money(50) == Money(150)
    assert Money(1) < Money(2)
    assert sorted([Money(3), Money(1), Money(2)]) == [Money(1), Money(2), Money(3)]


def test_expense_dataclass(ex):
    Expense = _need(ex, "Expense")
    assert dataclasses.is_dataclass(Expense), "use @dataclass"
    e = Expense("Concert", 110.0, "fun")
    assert e.is_large() is True
    assert e.is_large(200) is False
    assert Expense("Gum", 1.5).category == "other"
    assert Expense("A", 1) == Expense("A", 1), "dataclasses give you == for free"


def test_budget(ex):
    Expense = _need(ex, "Expense")
    Budget = _need(ex, "Budget")
    b = Budget(limit=100)
    b.add(Expense("Lunch", 12.5, "food"))
    b.add(Expense("Dinner", 30, "food"))
    b.add(Expense("Cinema", 20, "fun"))
    assert b.total() == 62.5
    assert b.remaining() == 37.5
    assert b.by_category() == {"food": 42.5, "fun": 20}
    assert b.over_budget() is False
    b.add(Expense("Shoes", 80, "shopping"))
    assert b.over_budget() is True
    assert Budget(limit=10).expenses == [], "each Budget needs its own list - use field(default_factory=list)"


def test_rectangle_and_square(ex):
    Rectangle = _need(ex, "Rectangle")
    Square = _need(ex, "Square")
    r = Rectangle(3, 4)
    assert r.area == 12, "area should be a @property (no parentheses)"
    assert r.perimeter() == 14
    s = Square(5)
    assert isinstance(s, Rectangle), "Square should inherit from Rectangle"
    assert s.area == 25 and s.perimeter() == 20
