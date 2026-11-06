# Module 08: Errors & Debugging

**Goal:** read error messages calmly, find bugs systematically, and handle
errors so your programs don't crash.
**Time:** 3–4 hours.

Professional programmers aren't people who don't make mistakes. They're people
who are **fast at finding** their mistakes. This module teaches that skill.

---

## 1. Reading a traceback

```
Traceback (most recent call last):
  File "budget.py", line 12, in <module>
    print(average(expenses))
  File "budget.py", line 4, in average
    return total / len(items)
ZeroDivisionError: division by zero
```

**Read from the bottom up:**
1. **Last line** = what went wrong: `ZeroDivisionError: division by zero`.
2. **Line above it** = exactly where: `budget.py`, line 4, inside `average`.
3. **Further up** = how the program got there: line 12 called `average`.

So: `items` was empty when `average` was called. Now you know what to look at.

---

## 2. The errors you'll meet most

| Error | Usually means | Example |
|-------|---------------|---------|
| `SyntaxError` | Python can't parse it: missing `:`, bracket, or quote | `if x > 3` |
| `IndentationError` | Inconsistent spaces | mixing tabs and spaces |
| `NameError` | Using a name that doesn't exist (often a typo) | `pritn("hi")` |
| `TypeError` | Wrong type for the operation | `"Age: " + 36` |
| `ValueError` | Right type, bad value | `int("hello")` |
| `IndexError` | List position doesn't exist | `[1, 2][5]` |
| `KeyError` | Dict key doesn't exist | `{"a": 1}["b"]` |
| `AttributeError` | That type doesn't have that method | `[1, 2].upper()` |
| `ZeroDivisionError` | Dividing by zero | `10 / 0` |
| `FileNotFoundError` | Wrong path or file name | `open("nope.txt")` |

> Tip: paste the **last line** of an error into a search engine. Someone has
> had it before.

---

## 3. A debugging method that always works

1. **Reproduce it.** Find the exact input that causes the bug.
2. **Read the error** (bottom up).
3. **Form a guess:** "I think `total` is a string, not a number."
4. **Test the guess:** add a `print` right before the failing line:
   ```python
   print(f"DEBUG total={total!r} type={type(total)}")
   ```
   `!r` shows the *exact* value. `'5'` with quotes means it's a string!
5. **Fix one thing**, run again.
6. **Remove the debug prints.**

### Rubber-duck debugging
Explain your code line by line, out loud, to a rubber duck (or a patient
friend). You'll often find the bug halfway through the explanation. It works
because explaining forces you to check each assumption.

### Using the VS Code debugger
1. Click in the margin left of a line number to set a red **breakpoint**.
2. Press **F5** → "Python File".
3. The program pauses at the breakpoint. Hover over variables to see their values.
4. **F10** runs the next line; **F11** steps into a function call.

Learn this. It's a superpower.

### `breakpoint()`
Put `breakpoint()` in your code and run it in the terminal. You get a prompt
(`(Pdb)`) where you can type variable names to see them, `n` for next line,
`c` to continue, `q` to quit.

---

## 4. Logic bugs: no error, wrong answer

The hardest bugs don't crash. Common ones:

```python
# Off-by-one: range stops BEFORE the end
for i in range(1, 10):     # 1..9, not 1..10!

# = vs ==
if x = 5:                  # SyntaxError (luckily)

# Forgetting to store a string method's result
name.strip()               # does nothing on its own

# Return inside the loop: returns after the first item!
def total(nums):
    t = 0
    for n in nums:
        t += n
        return t           # ← should be un-indented one level

# Integer vs string comparison
"10" > "9"                 # False! strings compare character by character
```

---

## 5. Handling errors: `try` / `except`

Some errors aren't bugs. They're things that *can* go wrong: users typing
nonsense, missing files, network failures. Handle them:

```python
try:
    age = int(input("Age: "))
except ValueError:
    print("That's not a number!")
    age = None
```

Python runs the `try` block. If a `ValueError` happens, it jumps to the
`except` block instead of crashing.

### The full form
```python
try:
    f = open("data.txt")
    data = f.read()
except FileNotFoundError:
    print("No data file yet; starting fresh.")
    data = ""
except PermissionError as e:
    print(f"Can't read the file: {e}")
    data = ""
else:
    print("Loaded successfully")   # runs only if no exception happened
finally:
    print("Done trying")           # ALWAYS runs
```

### Keep asking until valid
```python
def ask_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
```

### ⚠️ Don't swallow everything
```python
try:
    do_something()
except:            # ❌ catches EVERYTHING, even typos and Ctrl+C
    pass
```
Catch the **specific** error you expect. Hiding errors hides bugs.

---

## 6. Raising your own errors

When a function gets input it can't sensibly handle, **raise** an error
rather than returning something wrong:

```python
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError(f"Insufficient funds: balance is {balance}")
    return balance - amount
```

Whoever calls it can decide what to do:

```python
try:
    balance = withdraw(balance, 500)
except ValueError as e:
    print(f"Sorry: {e}")
```

This is a key design principle: **functions that detect problems raise;
code that talks to the user catches and explains.**

---

## Key takeaways
- Read tracebacks **bottom up**: what, where, how we got there.
- Debug by guessing and testing with `print(f"{x!r}")` or the debugger.
- `try` / `except SpecificError` handles expected problems.
- `raise ValueError("why")` when a function gets bad input.

**Continue reading:** [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) (the official Python tutorial). The complete picture of try/except/else/finally, raising, and custom exceptions.

**Next:** [Module 09: Files & data](../09_files_data/lesson.md)
