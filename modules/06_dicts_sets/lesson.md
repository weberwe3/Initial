# Module 06: Dictionaries & Sets

**Goal:** look things up by name, count things, and remove duplicates.
**Time:** 3–4 hours.

---

## 1. Dictionaries: labelled values

A list finds things by **position**. A dictionary (`dict`) finds things by
**key**, like a real dictionary where you look up a word to get its meaning.

```python
person = {
    "name": "Ada",
    "age": 36,
    "city": "London",
}

person["name"]          # 'Ada'
person["age"] = 37      # change a value
person["email"] = "ada@example.com"   # add a new key
del person["city"]      # remove a key
len(person)             # 3
"name" in person        # True  (checks KEYS)
```

Keys are usually strings (they can be numbers or tuples too) and must be
unique. Values can be anything, including lists or other dicts.

---

## 2. Safe lookups with `.get()`

```python
person["phone"]              # KeyError! crashes if the key isn't there
person.get("phone")          # None, no crash
person.get("phone", "n/a")   # 'n/a', your chosen default
```

---

## 3. Looping over a dictionary

```python
prices = {"apple": 0.5, "bread": 2.25, "milk": 1.10}

for item in prices:                  # loops over KEYS
    print(item)

for price in prices.values():        # just the values
    print(price)

for item, price in prices.items():   # both: the one you'll use most
    print(f"{item}: ${price:.2f}")
```

Dictionaries remember the order you inserted keys.

---

## 4. The counting pattern ⭐

Counting how often things appear is one of the most common tasks in programming:

```python
words = "the cat and the hat and the bat".split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)
# {'the': 3, 'cat': 1, 'and': 2, 'hat': 1, 'bat': 1}
```

Read the key line as: "look up the current count (or 0 if new), add one,
store it back."

## 5. The grouping pattern ⭐

```python
transactions = [("food", 12.5), ("rent", 1200), ("food", 30), ("fun", 25)]
by_category = {}
for category, amount in transactions:
    if category not in by_category:
        by_category[category] = []
    by_category[category].append(amount)
# {'food': [12.5, 30], 'rent': [1200], 'fun': [25]}
```

Or totals instead of lists:

```python
totals = {}
for category, amount in transactions:
    totals[category] = totals.get(category, 0) + amount
```

---

## 6. Lists of dictionaries: how real data looks

Data from spreadsheets, databases, and web APIs almost always arrives as a
list of dicts, one dict per row/record:

```python
people = [
    {"name": "Ada", "dept": "Engineering", "salary": 95000},
    {"name": "Grace", "dept": "Engineering", "salary": 105000},
    {"name": "Linus", "dept": "Support", "salary": 60000},
]

for p in people:
    print(f"{p['name']} works in {p['dept']}")

# total salary per department
dept_totals = {}
for p in people:
    dept_totals[p["dept"]] = dept_totals.get(p["dept"], 0) + p["salary"]
```

> Note: inside an f-string with double quotes, use single quotes for keys:
> `f"{p['name']}"`.

---

## 7. Sets: unique values, fast membership

A set is an unordered collection with **no duplicates**:

```python
tags = {"python", "beginner", "python"}
print(tags)              # {'python', 'beginner'}  (order may vary)
tags.add("tutorial")
tags.discard("beginner")
"python" in tags         # True, and very fast even for huge sets

unique = set([3, 1, 3, 2, 1])   # {1, 2, 3}
empty = set()                    # NOT {} (that's an empty dict)
```

### Set maths
```python
mine = {"python", "sql", "excel"}
job = {"python", "sql", "aws"}

mine & job    # {'python', 'sql'}           in both (intersection)
mine | job    # all four skills             in either (union)
job - mine    # {'aws'}                     in job but not mine (difference)
```

---

## 8. Which collection should I use?

| Need | Use |
|------|-----|
| Ordered items, may change | `list` |
| Fixed group of related values | `tuple` |
| Look up a value by a name/ID | `dict` |
| Unique items / "have I seen this?" | `set` |

---

## Key takeaways
- `dict` maps keys → values. Use `.get(key, default)` for safe lookups.
- Loop with `.items()` to get keys and values together.
- Counting: `counts[k] = counts.get(k, 0) + 1`.
- Real data is usually a **list of dicts**.
- `set` removes duplicates and answers "is X in here?" fast.

**Checkpoint:** you've finished Part 1. Do
[Project 1](../../projects/01_first_programs.md) before moving on.

**Next:** [Module 07: Functions](../07_functions/lesson.md)
