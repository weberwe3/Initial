# Module 03: Decisions

**Goal:** make programs choose what to do with `if`, `elif`, `else`.
**Time:** 2–3 hours.

---

## 1. Booleans: `True` and `False`

Comparisons produce a **boolean**, either `True` or `False`:

```python
5 > 3        # True
5 < 3        # False
5 == 5       # True    ← two equals signs to COMPARE
5 != 4       # True    "not equal"
5 >= 5       # True
"a" == "A"   # False   case matters
```

> ⚠️ `=` stores a value. `==` asks "are these equal?". Mixing them up is the
> #1 beginner bug.

---

## 2. `if`, `elif`, `else`

```python
temperature = 28

if temperature > 30:
    print("It's hot!")
elif temperature > 20:
    print("It's warm.")
elif temperature > 10:
    print("It's mild.")
else:
    print("It's cold.")
```

How to read it:
- Python checks each condition **top to bottom** and runs the **first** block
  whose condition is `True`. Then it skips the rest.
- `elif` ("else if") and `else` are optional.
- The colon `:` at the end of the line is required.
- The **indented** lines (4 spaces) are the block that belongs to that branch.
  Indentation isn't decoration in Python; it's how Python knows what's inside.

```python
if score >= 50:
    print("You passed")     # inside the if
    print("Well done")      # inside the if
print("Thanks for playing")  # always runs: not indented
```

---

## 3. Combining conditions: `and`, `or`, `not`

```python
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("Come in")

if day == "Saturday" or day == "Sunday":
    print("Weekend!")

if not has_ticket:
    print("Please buy a ticket")
```

- `and`: both sides must be True.
- `or`: at least one side must be True.
- `not`: flips True ↔ False.

Python lets you chain comparisons, which reads nicely:

```python
if 18 <= age < 65:
    print("Working age")
```

### Checking membership with `in`
```python
if day in ("Saturday", "Sunday"):
    print("Weekend!")
```

---

## 4. "Truthiness"

Python treats some values as false-ish in an `if`:
`0`, `0.0`, `""` (empty string), `[]` (empty list), `None`. Everything else
counts as true.

```python
name = input("Name: ")
if name:
    print(f"Hi {name}")
else:
    print("You didn't type anything!")
```

---

## 5. Order matters

```python
# ❌ Bug: a score of 95 prints "C", because 95 >= 50 is checked first
if score >= 50:
    grade = "C"
elif score >= 70:
    grade = "B"
elif score >= 90:
    grade = "A"

# ✅ Check the most specific / highest case first
if score >= 90:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 50:
    grade = "C"
else:
    grade = "F"
```

---

## 6. Real-world example: a shipping calculator

```python
total = float(input("Order total: $"))
country = input("Country: ").strip().lower()

if country == "us":
    shipping = 0 if total >= 50 else 5.99
elif country in ("canada", "mexico"):
    shipping = 12.00
else:
    shipping = 25.00

print(f"Shipping: ${shipping:.2f}")
print(f"Total:    ${total + shipping:.2f}")
```

`x if condition else y` is a one-line `if` (a "conditional expression"). It's
handy for simple choices between two values.

---

## 7. A tip for the exercises

Inside an exercise function you can `return` from any branch. As soon as a
`return` runs, the function stops, so you often don't even need `elif`:

```python
def sign(n):
    if n > 0:
        return "positive"
    if n < 0:
        return "negative"
    return "zero"
```

---

## Key takeaways
- `==` compares, `=` assigns.
- `if` / `elif` / `else` runs the **first** matching branch only.
- Indentation defines blocks. Use 4 spaces.
- Combine conditions with `and`, `or`, `not`; check membership with `in`.

**Continue reading:** [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (the official Python tutorial). if, for, range, break and the newer match statement, all in one place.

**Next:** [Module 04: Loops](../04_loops/lesson.md)
