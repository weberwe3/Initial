# Module 02: Strings (Working with Text)

**Goal:** slice, search, clean and format text.
**Time:** 3 hours.

Text is everywhere: names, emails, file names, spreadsheet cells, web pages.
Being good with strings makes you useful fast.

---

## 1. Making strings

```python
a = "double quotes"
b = 'single quotes'
c = "It's easy to include an apostrophe this way"
d = """Triple quotes
let a string span
several lines."""
```

Special characters use a backslash: `"\n"` is a new line, `"\t"` is a tab.

---

## 2. Joining and repeating

```python
first = "Ada"
last = "Lovelace"
full = first + " " + last     # "Ada Lovelace"
line = "-" * 20               # "--------------------"
len(full)                     # 12  (number of characters)
```

---

## 3. f-strings: the best way to build text

Put an `f` before the quotes and drop any variable or expression inside `{}`:

```python
name = "Ada"
age = 36
print(f"{name} is {age} years old")
print(f"Next year she'll be {age + 1}")
```

### Formatting numbers
```python
price = 1234.5678
f"{price:.2f}"      # '1234.57'    2 decimal places
f"{price:,.2f}"     # '1,234.57'   with thousands separator
f"{0.256:.1%}"      # '25.6%'      as a percentage
f"{42:>6}"          # '    42'     right-aligned in 6 spaces
f"{'hi':<6}|"       # 'hi    |'    left-aligned
```

You'll use `:.2f` constantly for money.

---

## 4. Indexing and slicing

Each character has a position (an **index**), **starting from 0**.

```
 P  y  t  h  o  n
 0  1  2  3  4  5
-6 -5 -4 -3 -2 -1
```

```python
word = "Python"
word[0]      # 'P'   first character
word[-1]     # 'n'   last character
word[0:3]    # 'Pyt' from index 0 up to (NOT including) 3
word[2:]     # 'thon' from 2 to the end
word[:2]     # 'Py'  from the start up to 2
word[::-1]   # 'nohtyP' reversed (step of -1)
```

The rule "up to but not including the end" feels odd at first, but it means
`word[:3] + word[3:]` always gives back the whole word.

---

## 5. String methods

A **method** is a function attached to a value. Call it with a dot:

```python
s = "  Hello, World!  "
s.strip()          # 'Hello, World!'      remove surrounding spaces
s.lower()          # '  hello, world!  '
s.upper()          # '  HELLO, WORLD!  '
s.replace("World", "Python")
"hello world".title()       # 'Hello World'
"report.pdf".endswith(".pdf")   # True
"report.pdf".startswith("rep")  # True
"banana".count("a")         # 3
"banana".find("n")          # 2  (index of first match, -1 if none)
```

**Strings never change in place.** Methods return a *new* string:

```python
name = "  sam "
name.strip()          # this alone does nothing useful!
name = name.strip()   # store the result
```

### Checking content
```python
"123".isdigit()     # True
"abc".isalpha()     # True
"ell" in "hello"    # True    the `in` operator checks for a substring
```

---

## 6. Splitting and joining: the power pair

```python
"a,b,c".split(",")            # ['a', 'b', 'c']
"the quick  brown fox".split()  # ['the', 'quick', 'brown', 'fox'] splits on any whitespace
"-".join(["2026", "11", "06"])  # '2026-11-06'
```

`split` turns text into a list (Module 05); `join` turns a list back into text.
Together they solve a huge number of real problems, like cleaning up
CSV lines, reformatting names, or building file names.

```python
full_name = "ada lovelace"
parts = full_name.split()                # ['ada', 'lovelace']
initials = parts[0][0] + parts[1][0]     # 'al'
print(initials.upper())                  # 'AL'
```

---

## 7. Real-world example: cleaning messy input

```python
raw = "   JOHN.smith@Example.COM  "
email = raw.strip().lower()
username, domain = email.split("@")
print(f"User: {username}, Domain: {domain}")
# User: john.smith, Domain: example.com
```

Chaining methods (`.strip().lower()`) works because each method returns a new
string you can call the next method on.

---

## Key takeaways
- f-strings (`f"...{x}..."`) are how you build text. `:.2f` for money.
- Indexes start at 0. Slices go *up to but not including* the end.
- Strings are immutable: store the result of `.strip()`, `.lower()`, etc.
- `split()` and `join()` convert between text and lists.

**Next:** [Module 03: Decisions](../03_decisions/lesson.md)
