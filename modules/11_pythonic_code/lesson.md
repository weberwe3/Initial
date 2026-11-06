# Module 11: Pythonic Code

**Goal:** write shorter, clearer Python with comprehensions, smart sorting,
and the built-ins experienced Python programmers use every day.
**Time:** 3–4 hours.

"Pythonic" means using the language's features the way they're meant to be
used. Everything here does what you could already do with loops, just more
clearly.

---

## 1. List comprehensions

The loop-and-append pattern:

```python
squares = []
for n in range(10):
    squares.append(n * n)
```

as a **comprehension**:

```python
squares = [n * n for n in range(10)]
```

Read it as: "a list of `n * n` for each `n` in `range(10)`".

### With a filter
```python
evens = [n for n in range(20) if n % 2 == 0]
passed = [s for s in scores if s >= 60]
clean = [w.strip().lower() for w in raw_words if w.strip()]
```

### With if/else (transform every item)
```python
labels = ["pass" if s >= 60 else "fail" for s in scores]
```
(Note the position: a *filter* `if` goes at the end; an *if/else* choice goes at the front.)

### Dict and set comprehensions
```python
prices = {"apple": 0.5, "bread": 2.25}
with_tax = {item: round(p * 1.2, 2) for item, p in prices.items()}
lengths = {word: len(word) for word in ["hi", "hello"]}
unique_domains = {email.split("@")[1] for email in emails}
```

> **When not to:** if a comprehension needs nested loops *and* conditions, or
> doesn't fit comfortably on one or two lines, use a regular loop. Clarity wins.

---

## 2. Generator expressions

Drop the brackets inside a function call and you get a *generator*. It produces
values one at a time without building a whole list:

```python
total = sum(p * q for p, q in items)
any(s < 0 for s in balances)       # True if ANY is negative
all(f.endswith(".csv") for f in files)   # True if ALL match
```

---

## 3. `enumerate` and `zip`

```python
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")

names = ["Ada", "Grace", "Linus"]
scores = [95, 98, 80]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

lookup = dict(zip(names, scores))   # {'Ada': 95, 'Grace': 98, 'Linus': 80}
```

---

## 4. Sorting like a pro: `key=`

```python
words = ["banana", "Apple", "cherry"]
sorted(words)                       # ['Apple', 'banana', 'cherry'] (capitals first!)
sorted(words, key=str.lower)        # case-insensitive
sorted(words, key=len)              # by length
sorted(words, reverse=True)         # descending
```

`key` is a **function** that's called on each item; items are sorted by what it returns.

### `lambda`: tiny unnamed functions
```python
people = [
    {"name": "Ada", "age": 36},
    {"name": "Grace", "age": 45},
    {"name": "Linus", "age": 28},
]
sorted(people, key=lambda p: p["age"])             # youngest first
max(people, key=lambda p: p["age"])["name"]        # 'Grace'

expenses = [("rent", 1200), ("food", 350)]
sorted(expenses, key=lambda e: e[1], reverse=True) # biggest first
```

`lambda p: p["age"]` is shorthand for:
```python
def get_age(p):
    return p["age"]
```
Use lambdas only for short one-off functions like these.

### Sorting by several things
Return a tuple. Python compares tuples element by element:
```python
sorted(people, key=lambda p: (p["dept"], -p["salary"]))   # by dept, then highest salary
```

---

## 5. More useful built-ins

```python
min(prices.items(), key=lambda kv: kv[1])   # cheapest (item, price)
sum(row["amount"] for row in rows)
round(x, 2), abs(-5), divmod(17, 5)         # divmod → (3, 2)
reversed(items)                              # iterate backwards
isinstance(x, (int, float))                  # type check
```

### Unpacking tricks
```python
first, *middle, last = [1, 2, 3, 4, 5]
print(*names, sep=", ")        # Ada, Grace, Linus
merged = {**defaults, **user_settings}   # merge dicts (right side wins)
combined = [*list_a, *list_b]
```

### The walrus `:=` (assign inside an expression)
```python
while (line := input("> ")) != "quit":
    print("You said", line)
```

---

## 6. Before and after

```python
# Before
result = []
for row in rows:
    if row["category"] == "food":
        result.append(row["amount"])
total = 0
for a in result:
    total = total + a

# After
total = sum(row["amount"] for row in rows if row["category"] == "food")
```

---

## Key takeaways
- `[expr for x in items if cond]` replaces loop-and-append.
- `sum(...)`, `any(...)`, `all(...)` with generator expressions.
- `enumerate` for positions, `zip` to walk lists side-by-side.
- `sorted(items, key=lambda x: ...)` sorts by anything.
- Readability beats cleverness, every time.

**Continue reading:** [Python List Comprehension: Tutorial With Examples](https://realpython.com/list-comprehension-python/) (Real Python). When comprehensions help, when they hurt, and the set/dict/generator variants.

**Next:** [Module 12: Classes & objects](../12_classes/lesson.md)
