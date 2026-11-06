# Module 01: First Steps

**Goal:** print things, store values in variables, do arithmetic, and get input.
**Time:** 2–3 hours.

---

## 1. `print()`: making the computer talk

```python
print("Hello")
print("My favourite number is", 7)
print()                      # an empty line
print("a", "b", "c", sep="-")  # a-b-c
```

`print` is a **function**: a named action. You call it by writing its name
followed by parentheses, and put what you want printed inside them.

Text goes inside quotes, either `"double"` or `'single'`; both work. Text in
quotes is called a **string**.

> **Try it:** Print your name, your city, and the year on three separate lines.

---

## 2. Comments

Anything after a `#` is ignored by Python. Comments are notes for humans.

```python
# This program greets the user
print("Hi!")  # comments can also go at the end of a line
```

Write comments that explain **why**, not **what**. The code already says what.

---

## 3. Variables: giving values a name

```python
name = "Sam"
age = 34
print(name, "is", age)
```

`=` means **"store the value on the right under the name on the left"**. It is
*not* "equals" like in maths. Read `age = 34` as "age gets 34".

Variables can be changed:

```python
score = 10
score = score + 5   # take the old score, add 5, store it back
print(score)        # 15
```

A shortcut for the same thing:

```python
score += 5    # same as score = score + 5
score -= 2    # subtract
score *= 3    # multiply
```

### Naming rules
- Letters, digits, and underscores only; can't start with a digit.
- Case matters: `Age` and `age` are different variables.
- Use `snake_case`: lowercase words joined with underscores: `monthly_rent`.
- Pick names that describe what's inside: `total_price` beats `tp` or `x`.

---

## 4. The basic types of value

| Type | Example | What it is |
|------|---------|------------|
| `int` | `42`, `-7` | Whole numbers |
| `float` | `3.14`, `0.5` | Numbers with a decimal point |
| `str` | `"hello"` | Text (a "string" of characters) |
| `bool` | `True`, `False` | Yes/no values (Module 03) |

Ask Python what type something is:

```python
type(42)        # <class 'int'>
type("42")      # <class 'str'>  ← quotes make it text, not a number!
```

---

## 5. Arithmetic

```python
7 + 2    # 9      addition
7 - 2    # 5      subtraction
7 * 2    # 14     multiplication
7 / 2    # 3.5    division (always gives a float)
7 // 2   # 3      floor division (whole part only)
7 % 2    # 1      remainder ("modulo")
7 ** 2   # 49     power
```

Normal maths order applies (powers, then `* /`, then `+ -`). Use parentheses
to be clear: `(price + tax) * quantity`.

**`%` is more useful than it looks:**
- `n % 2 == 0` tells you if `n` is even.
- `minutes % 60` gives leftover minutes after taking out whole hours.

### Rounding
```python
round(3.14159, 2)   # 3.14
round(2.5)          # 2  (Python rounds .5 to the nearest even number)
```

---

## 6. Converting between types

```python
int("42")       # 42     text → whole number
float("3.5")    # 3.5    text → decimal
str(42)         # "42"   number → text
int(3.9)        # 3      chops off the decimal (doesn't round)
```

This matters because `"2" + "3"` is `"23"` (text gets glued together), but
`2 + 3` is `5`.

---

## 7. `input()`: asking the user

```python
name = input("What's your name? ")
print("Nice to meet you,", name)
```

**`input()` always gives you a string**, even if the user types a number. Convert it:

```python
age = int(input("How old are you? "))
print("Next year you'll be", age + 1)
```

---

## 8. Your first real program

Save this as `minutes.py` and run it:

```python
# Convert a number of minutes into hours and minutes
total = int(input("How many minutes? "))
hours = total // 60
minutes = total % 60
print(total, "minutes is", hours, "hours and", minutes, "minutes")
```

> **Try it:** Change it to convert seconds into hours, minutes and seconds.

---

## 9. How exercises work in this course

Open `exercises.py`. Each exercise looks like this:

```python
def add_tax(price):
    # TODO: return the price with 20% tax added
    raise NotImplementedError
```

You'll learn exactly what `def` and `return` mean in Module 07. For now:

- `price` is a variable that's **already filled in for you** by the checker.
- Replace `raise NotImplementedError` with your code.
- Finish with `return <your answer>`, which hands the answer back to be checked.

Example answer:

```python
def add_tax(price):
    return price * 1.2
```

Keep the 4 spaces of indentation at the start of each line inside the `def`.
Then run `python check.py 1`.

---

## Key takeaways
- `print()` shows things; `input()` asks for things (always as text).
- `=` stores a value under a name.
- `int`, `float`, `str`, `bool` are the basic types; convert with `int()`, `float()`, `str()`.
- `//` and `%` give the whole part and the remainder of a division.

**Continue reading:** [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html) (the official Python tutorial). Numbers, text and your first program, in the words of the people who make Python.

**Next:** [Module 02: Strings](../02_strings/lesson.md)
