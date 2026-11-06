# Module 07: Functions

**Goal:** break problems into named, reusable pieces.
**Time:** 4 hours.

You've been *writing* functions in every exercise. Now you'll learn properly
what they are and how to design good ones. This is the single most important
skill for writing programs bigger than 30 lines.

---

## 1. Defining and calling

```python
def greet(name):
    message = f"Hello, {name}!"
    return message

result = greet("Ada")    # call the function
print(result)            # Hello, Ada!
```

- `def` starts a function definition. `greet` is its name.
- `name` is a **parameter**, a variable that gets filled in when the function is called.
- `"Ada"` is the **argument**, the actual value passed in.
- `return` sends a value back to whoever called the function, and **ends the function**.

Defining a function doesn't run it. It only runs when called.

---

## 2. `return` vs `print`

This confuses almost everyone at first:

```python
def add_print(a, b):
    print(a + b)      # shows it on screen, gives nothing back

def add_return(a, b):
    return a + b      # gives the value back to use

x = add_print(2, 3)   # prints 5, but x is None
y = add_return(2, 3)  # prints nothing, but y is 5
total = add_return(2, 3) * 10   # 50: you can keep using a returned value
```

**Rule of thumb:** functions that *compute* things should `return`. Keep
`print` and `input` in a small number of functions that talk to the user.
This makes your code testable, which is exactly why every exercise asks for a return.

A function without `return` gives back `None`.

---

## 3. Parameters in depth

### Default values
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Ada")              # Hello, Ada!
greet("Ada", "Welcome")   # Welcome, Ada!
```

### Keyword arguments
```python
def make_profile(name, age, city):
    return f"{name} ({age}) from {city}"

make_profile(age=36, city="London", name="Ada")   # order doesn't matter with names
```

Keyword arguments make calls readable: `send_email(to=..., subject=..., urgent=True)`
beats `send_email(..., ..., True)`.

> ⚠️ Never use a mutable default like `def f(items=[])`: the same list is
> reused between calls. Use `items=None` then `if items is None: items = []`.

### Any number of arguments
```python
def total(*numbers):         # numbers is a tuple of all positional args
    return sum(numbers)

total(1, 2, 3)   # 6

def describe(**details):     # details is a dict of all keyword args
    for key, value in details.items():
        print(f"{key}: {value}")

describe(name="Ada", job="Engineer")
```

---

## 4. Scope: where variables live

Variables created inside a function exist only inside it:

```python
def calc():
    secret = 42
    return secret

calc()
print(secret)   # NameError: secret only existed inside calc()
```

Functions can *read* variables from outside, but you should pass in what a
function needs as parameters instead. Functions that only depend on their
inputs are easy to understand, test, and reuse.

---

## 5. Docstrings: documenting your functions

```python
def compound_interest(principal, rate, years):
    """Return the balance after `years` of annual compounding.

    rate is a decimal, e.g. 0.05 for 5%.
    """
    return principal * (1 + rate) ** years
```

The string right after `def` is the docstring. VS Code shows it when you hover
over the function, and `help(compound_interest)` prints it.

---

## 6. Functions calling functions: decomposition

Big problems become easy when you split them into small functions that each
do one thing:

```python
def parse_line(line):
    """'rent,1200' -> ('rent', 1200.0)"""
    name, amount = line.split(",")
    return name.strip(), float(amount)

def parse_all(text):
    return [parse_line(line) for line in text.strip().split("\n")]

def summarise(items):
    total = sum(amount for _, amount in items)
    return f"{len(items)} expenses totalling ${total:,.2f}"

data = """rent, 1200
food, 350
transport, 90"""
print(summarise(parse_all(data)))   # 3 expenses totalling $1,640.00
```

(The `[... for ...]` syntax is a *list comprehension*. You'll meet it
properly in Module 11. Read it as "make a list of parse_line(line) for each line".)

### Signs a function is well designed
- Its name is a verb that says what it does: `calculate_total`, `load_expenses`.
- It does **one** job. If you need "and" to describe it, split it.
- It's short: ideally under ~20 lines.
- Same inputs → same output, with no hidden surprises.

---

## 7. The `main()` pattern

Real scripts are organised like this:

```python
def get_number(prompt):
    return float(input(prompt))

def main():
    price = get_number("Price: ")
    qty = get_number("Quantity: ")
    print(f"Total: ${price * qty:.2f}")

if __name__ == "__main__":
    main()
```

The last two lines mean "only run `main()` if this file is run directly, not
when it's imported by another file". You'll see why in Module 10.

---

## 8. Functions are values

You can pass a function to another function, without calling it (no parentheses):

```python
def shout(text):
    return text.upper() + "!"

def apply_to_all(func, items):
    return [func(x) for x in items]

apply_to_all(shout, ["hi", "bye"])   # ['HI!', 'BYE!']
apply_to_all(len, ["hi", "bye"])     # [2, 3]
```

This idea powers `sorted(..., key=...)` in Module 11 and decorators in Module 15.

---

## Key takeaways
- `def name(params):` defines; `name(args)` calls.
- **Return** results; keep printing/asking separate.
- Defaults and keyword arguments make functions flexible and readable.
- Variables inside a function are local to it.
- Split big problems into small single-purpose functions.

**Continue reading:** [Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/) (Real Python). Arguments, defaults, *args/**kwargs, return values and docstrings in depth.

**Next:** [Module 08: Errors & debugging](../08_errors_debugging/lesson.md)
