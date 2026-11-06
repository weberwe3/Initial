# Module 05: Lists & Tuples

**Goal:** store many values together and process them.
**Time:** 3–4 hours.

---

## 1. Lists

A list is an ordered collection, written in square brackets:

```python
groceries = ["milk", "eggs", "bread"]
scores = [88, 92, 79]
mixed = ["Ada", 36, True]   # allowed, but usually a list holds one kind of thing
empty = []
```

Indexing and slicing work exactly like strings:

```python
groceries[0]      # 'milk'
groceries[-1]     # 'bread'
groceries[1:]     # ['eggs', 'bread']
len(groceries)    # 3
"eggs" in groceries   # True
```

---

## 2. Lists can change (they're *mutable*)

Unlike strings, you can change a list in place:

```python
groceries[0] = "oat milk"        # replace an item
groceries.append("apples")       # add to the end
groceries.insert(0, "coffee")    # add at a position
groceries.remove("eggs")         # remove the first matching value
last = groceries.pop()           # remove and return the last item
groceries.extend(["rice", "tea"])  # add several items
groceries.sort()                 # sort in place (alphabetical / numeric)
groceries.reverse()              # reverse in place
groceries.index("bread")         # position of a value
groceries.count("tea")           # how many times it appears
```

### `sorted()` vs `.sort()`
```python
nums = [3, 1, 2]
new = sorted(nums)   # returns a NEW sorted list; nums is unchanged
nums.sort()          # changes nums itself; returns None
```

> ⚠️ Classic bug: `nums = nums.sort()` sets `nums` to `None`. Use one or the other.

---

## 3. Looping over lists

```python
for item in groceries:
    print(f"- {item}")
```

### Need the position too? Use `enumerate`
```python
for i, item in enumerate(groceries, start=1):
    print(f"{i}. {item}")
```

### Building a new list (the accumulator pattern again)
```python
prices = [4.99, 12.50, 3.25]
with_tax = []
for p in prices:
    with_tax.append(round(p * 1.2, 2))
print(with_tax)    # [5.99, 15.0, 3.9]
```

### Filtering
```python
scores = [55, 82, 47, 91, 68]
passed = []
for s in scores:
    if s >= 60:
        passed.append(s)
```

---

## 4. Handy built-ins for lists of numbers

```python
nums = [4, 8, 15, 16, 23, 42]
sum(nums)          # 108
min(nums)          # 4
max(nums)          # 42
sum(nums) / len(nums)   # average: 18.0
```

---

## 5. Tuples: lists that can't change

```python
point = (3, 4)
rgb = (255, 128, 0)
point[0]    # 3
# point[0] = 5   ← error! tuples are immutable
```

Use a tuple for a fixed group of values that belong together (a coordinate, a
date, a row of data). Use a list for a collection that grows or changes.

### Unpacking
```python
x, y = point                 # x = 3, y = 4
name, age = ("Ada", 36)
a, b = b, a                  # swap two variables in one line!
first, *rest = [1, 2, 3, 4]  # first = 1, rest = [2, 3, 4]
```

You've already used this: returning `hours, minutes` in Module 01 returned a tuple.

---

## 6. Lists of lists

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
]
grid[1][2]    # 6   row 1, column 2

for row in grid:
    for value in row:
        print(value, end=" ")
```

A list of tuples is a great way to hold simple tabular data:

```python
expenses = [("rent", 1200), ("food", 350), ("transport", 90)]
for category, amount in expenses:
    print(f"{category:<10} ${amount:>7,.2f}")
```

---

## 7. ⚠️ The aliasing trap

```python
a = [1, 2, 3]
b = a           # b is NOT a copy: it's another name for the SAME list
b.append(4)
print(a)        # [1, 2, 3, 4]  ← surprise!

c = a.copy()    # a real, separate copy (or a[:] or list(a))
```

Variables are *labels* stuck onto values, not boxes containing them. Two labels
can point at one list.

---

## Key takeaways
- Lists `[...]` are ordered and changeable; tuples `(...)` are ordered and fixed.
- `append`, `remove`, `pop`, `sort` change a list in place.
- Loop with `for item in items:`; use `enumerate` when you need positions.
- `sum`, `min`, `max`, `len`, `sorted` do most of your number crunching.
- `b = a` doesn't copy a list. Use `.copy()`.

**Continue reading:** [Data Structures](https://docs.python.org/3/tutorial/datastructures.html) (the official Python tutorial). Every list method, tuples, sets and dictionaries, plus looping techniques.

**Next:** [Module 06: Dictionaries & sets](../06_dicts_sets/lesson.md)
