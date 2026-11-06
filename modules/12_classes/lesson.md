# Module 12: Classes & Objects

**Goal:** model real things with classes, and know when a class is (and isn't)
the right tool.
**Time:** 4–5 hours.

---

## 1. Why classes?

So far, data (dicts, lists) and behaviour (functions) have been separate.
A **class** bundles them together. It's a blueprint for making **objects** that
have their own data (**attributes**) and actions (**methods**).

You've used objects all along: `"hello".upper()` calls the `upper` method on a
`str` object. `[1, 2].append(3)` calls `append` on a `list` object. Now you'll
make your own types.

---

## 2. Your first class

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def __str__(self):
        return f"{self.owner}: ${self.balance:,.2f}"


acct = BankAccount("Ada", 100)    # create an object (an "instance")
acct.deposit(50)
acct.withdraw(30)
print(acct.balance)               # 120
print(acct)                       # Ada: $120.00

other = BankAccount("Grace")      # a separate object with its own balance
```

### The pieces
- `class BankAccount:` defines the blueprint. Class names use `CapitalWords`.
- `__init__` is the **constructor**. It runs automatically when you create an
  object and sets up its starting attributes.
- `self` is **the specific object** the method is working on. When you write
  `acct.deposit(50)`, Python calls `BankAccount.deposit(acct, 50)`, so `self`
  *is* `acct`.
- `self.balance = ...` stores data **on that object**.
- Every method takes `self` as its first parameter.

---

## 3. Special ("dunder") methods

Methods with double underscores let your objects work with Python's built-in syntax:

```python
class Money:
    def __init__(self, cents):
        self.cents = cents

    def __str__(self):              # print(m), str(m), f"{m}"
        return f"${self.cents / 100:,.2f}"

    def __repr__(self):             # what you see in the REPL / debugger
        return f"Money({self.cents})"

    def __add__(self, other):       # m1 + m2
        return Money(self.cents + other.cents)

    def __eq__(self, other):        # m1 == m2
        return self.cents == other.cents

    def __lt__(self, other):        # m1 < m2 (and makes sorted() work)
        return self.cents < other.cents

print(Money(150) + Money(275))   # $4.25
```

Others you'll see: `__len__` (`len(x)`), `__contains__` (`in`), `__iter__`
(`for item in x`).

---

## 4. Dataclasses: classes without the boilerplate

Most classes you write mainly *hold data*. `dataclass` writes `__init__`,
`__repr__` and `__eq__` for you:

```python
from dataclasses import dataclass, field
from datetime import date

@dataclass
class Expense:
    description: str
    amount: float
    category: str = "other"
    when: date = field(default_factory=date.today)

    def is_large(self, threshold=100):
        return self.amount >= threshold


e = Expense("Concert", 110.0, "fun")
print(e)          # Expense(description='Concert', amount=110.0, category='fun', when=...)
e.is_large()      # True
```

The `: str`, `: float` parts are **type hints** (Module 15). Dataclasses need them.

> **Default to dataclasses** for "a thing with some fields". Upgrade to a
> hand-written class when you need custom setup logic.

---

## 5. Objects working together

```python
from dataclasses import dataclass, field

@dataclass
class Expense:
    description: str
    amount: float
    category: str

@dataclass
class Budget:
    limit: float
    expenses: list = field(default_factory=list)   # a NEW list per budget

    def add(self, expense):
        self.expenses.append(expense)

    def total(self):
        return sum(e.amount for e in self.expenses)

    def remaining(self):
        return self.limit - self.total()

    def by_category(self):
        totals = {}
        for e in self.expenses:
            totals[e.category] = totals.get(e.category, 0) + e.amount
        return totals


b = Budget(limit=2000)
b.add(Expense("Rent", 1200, "housing"))
b.add(Expense("Groceries", 84.2, "food"))
print(f"Remaining: ${b.remaining():,.2f}")
```

This is **composition**: a `Budget` *has* expenses. It's the most common and
useful way to combine classes.

---

## 6. Inheritance (use sparingly)

A class can extend another, reusing its code and changing parts:

```python
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def monthly_fee(self):
        return 5

class PremiumAccount(Account):           # PremiumAccount IS an Account
    def __init__(self, owner, balance=0, cashback=0.01):
        super().__init__(owner, balance) # run the parent's __init__
        self.cashback = cashback

    def monthly_fee(self):               # override
        return 0
```

Use inheritance when one thing truly **is a kind of** another. If you're
unsure, prefer composition. Deep inheritance trees are hard to follow.

---

## 7. Properties and class attributes

```python
class Rectangle:
    sides = 4                          # class attribute: shared by all rectangles

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):                    # accessed like an attribute: r.area
        return self.width * self.height

r = Rectangle(3, 4)
r.area      # 12  (no parentheses)
```

---

## 8. When should I write a class?

✅ Good reasons:
- You keep passing the same group of values to several functions.
- A thing has state that changes over time (an account balance, a game character).
- You want your own type that works with `+`, `==`, `sorted`, `print`, etc.

❌ Not needed:
- A class with only one method besides `__init__`: that's just a function.
- Pure calculations: functions are simpler.

Python is happy to mix both. Most good programs are mostly functions plus a
few well-chosen classes.

---

## Key takeaways
- A class is a blueprint; objects (instances) are made from it.
- `__init__` sets up attributes; `self` is the current object.
- Dunder methods (`__str__`, `__eq__`, `__add__`...) plug into Python syntax.
- `@dataclass` is the quickest way to make a data-holding class.
- Prefer composition ("has a") over inheritance ("is a").

**Continue reading:** [Classes](https://docs.python.org/3/tutorial/classes.html) (the official Python tutorial). Scopes, instances, inheritance and iterators: how Python's object model really works.

**Next:** [Module 13: Testing](../13_testing/lesson.md)
