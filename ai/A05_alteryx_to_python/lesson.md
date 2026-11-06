# Module A05: From Alteryx to Python

**Goal:** translate the Alteryx tools you use every day into Python, so you can read, write and AI-generate Python with confidence, and combine both in one workflow.
**Time:** 4 hours.

You already think like a programmer. Every Alteryx workflow is a program:
data flows through tools that select, filter, compute, join and summarise.
Python does the same things with text instead of icons. This module is the
translation dictionary.

---

## 1. Why a BA who knows Alteryx should learn Python

- **AI writes Python fluently.** Ask an assistant for an Alteryx workflow and
  it can only describe one. Ask for Python and you get something you can run.
- **The Python tool** inside Alteryx Designer lets you drop Python into an
  existing workflow, so you don't have to choose.
- **Calling AI APIs** (A07), text analytics (A08) and document search (A09) are
  natural in Python.
- **Career range:** "Alteryx + Python + AI" is a much rarer and more valuable
  combination than any one alone.

Alteryx stays great for visual, auditable, shareable workflows. Python adds
reach. The best analysts use both.

---

## 2. The mental model: rows and fields

In Alteryx, records flow through tools. In plain Python, a table is a
**list of dicts**: one dict per record, one key per field:

```python
orders = [
    {"order_id": 1, "region": "North", "amount": 120.0},
    {"order_id": 2, "region": "South", "amount": 80.0},
    {"order_id": 3, "region": "North", "amount": 45.5},
]
```

In real projects you'll use **pandas DataFrames** (Module A06), which do all of
this in one line each. Writing the tools by hand first (in this module's
exercises) means you'll understand exactly what pandas and AI-generated code
are doing, and be able to check them.

---

## 3. The translation dictionary

| Alteryx tool | What it does | Plain Python | pandas (Module A06) |
|--------------|--------------|--------------|---------------------|
| **Input Data** | Read a file | `csv.DictReader` | `pd.read_csv("f.csv")` |
| **Select** | Keep / rename / drop fields | dict comprehension | `df[["a","b"]].rename(columns={...})` |
| **Filter** (T/F) | Split rows by a condition | two list comprehensions | `df[df.amount > 100]` |
| **Formula** | New or updated field | `row["x"] = ...` in a loop | `df["x"] = df.a * df.b` |
| **Sort** | Order rows | `sorted(rows, key=...)` | `df.sort_values("a")` |
| **Unique** (U/D) | First of each key / duplicates | track seen keys in a set | `df.drop_duplicates("key")` |
| **Join** (J/L/R) | Match two inputs on a key | dict lookup | `pd.merge(a, b, on="key", how=...)` |
| **Union** | Stack inputs | `a + b` | `pd.concat([a, b])` |
| **Summarize** | Group by + aggregate | dict accumulators | `df.groupby("g").agg(...)` |
| **Cross Tab** | Rows → columns (pivot) | nested dicts | `df.pivot_table(...)` |
| **Transpose** | Columns → rows | loop over keys | `df.melt(...)` |
| **Multi-Row Formula** | Use the previous row | loop that remembers the previous row | `df["prev"] = df.a.shift(1)` |
| **Sample** | First N / random N | slicing, `random.sample` | `df.head(n)`, `df.sample(n)` |
| **Output Data** | Write a file | `csv.DictWriter` | `df.to_csv("out.csv", index=False)` |

---

## 4. Alteryx's multiple outputs, in Python

Some Alteryx tools have several output anchors. In Python, a function can
**return several values**:

```python
def filter_rows(rows, condition):
    true_rows = [r for r in rows if condition(r)]
    false_rows = [r for r in rows if not condition(r)]
    return true_rows, false_rows          # T and F anchors

big, small = filter_rows(orders, lambda r: r["amount"] > 100)
print(len(big), len(small))
```

The Join tool's **J, L, R** anchors (matched, left-only, right-only) work the
same way; you'll build it in the exercises. Checking the L and R outputs is
as important in Python as in Alteryx: unmatched rows are where data-quality
problems hide.

---

## 5. Formula and Multi-Row Formula

```python
# Formula: margin = (price - cost) / price
for row in products:
    row["margin"] = round((row["price"] - row["cost"]) / row["price"], 3)

# Multi-Row Formula: running total, and change vs previous row
running = 0
previous = None
for row in monthly:
    running += row["sales"]
    row["running_total"] = running
    row["change"] = None if previous is None else row["sales"] - previous["sales"]
    previous = row
```

`lambda r: ...` (Module 11 of the Python track) is the Python version of the
expression box in a Formula or Filter tool.

---

## 6. Summarize and Cross Tab

```python
# Summarize: group by region, Sum(amount), Count
summary = {}
for r in orders:
    s = summary.setdefault(r["region"], {"region": r["region"], "Sum_amount": 0, "Count": 0})
    s["Sum_amount"] += r["amount"]
    s["Count"] += 1
print(list(summary.values()))
```

Cross Tab is "group by two things and spread one of them across columns".
You'll write it in the exercises, then see the one-line pandas version in A06.

---

## 7. Python inside Alteryx: the Python tool (Designer 2025.1)

The Python tool (Developer category) runs Python as a step in your workflow.
Data comes in from the input anchor as a **pandas DataFrame**, and you send
DataFrames to output anchors:

```python
from ayx import Alteryx

df = Alteryx.read("#1")                          # input anchor 1 → DataFrame
df["is_large"] = df["amount"] > 1000             # any Python / pandas logic
Alteryx.write(df, 1)                             # → output anchor 1
```

### What's specific to your version (2025.1)

| Topic | In Designer 2025.1 | Why it matters to you |
|-------|--------------------|-----------------------|
| **Python version** | Embedded **Python 3.10** | Write 3.10-compatible code. Everything in the Python track works on 3.10 except a few newer conveniences, and AI assistants should be told: *"target Python 3.10"*. |
| **Interactive Mode** | **Available**: the tool opens a Jupyter notebook where you run cells and see DataFrames as you go | Develop and debug interactively, then switch to production mode so the workflow runs the code unattended |
| **AMP engine** | Native AMP support for the Python tool arrived later (2026.2) | If your workflows run on AMP, test Python-tool workflows carefully, and check the engine-compatibility guidance in Alteryx Help if results or performance look off |
| **Packages** | pandas and common libraries come with the embedded environment; extra packages are installed through the `ayx` package's install helper or by an admin | Installing packages may need admin rights or IT approval. Ask before relying on a new library in a shared workflow |

> **When your company upgrades:** Designer 2026.1 removed Interactive Mode and
> moved the embedded Python to 3.13, and 2026.2 made the Python tool AMP-native.
> Code written for 3.10 generally keeps working on 3.13, but re-test shared
> workflows after any upgrade, and keep a copy of your notebook code as `.py`
> files so nothing lives only inside a tool.

### A practical development loop on 2025.1

1. Connect a **small sample** (Sample tool → first 100 rows) into the Python tool.
2. Develop in **Interactive Mode**: read, transform, `print(df.shape)`, inspect.
3. Keep the logic in **functions**, so the notebook stays readable.
4. Switch to production mode, remove the sample, and compare row counts and
   totals with the Alteryx-only version of the step.
5. Save the code in your team's repository or shared folder as well.

Good uses: an API call per row (AI classification, A07), advanced text
processing, a statistics library Alteryx doesn't have, or reusing a script a
colleague wrote.

## 8. Using AI to translate workflows

A powerful ambassador demo:

```text
Here's the list of tools in my Alteryx workflow, in order, with their
configuration:
1. Input: sales.csv
2. Filter: [Region] != "Test"
3. Formula: Margin = ([Price]-[Cost])/[Price]
4. Join to products.csv on ProductID (keep J and L outputs)
5. Summarize: group by Category, Sum(Revenue), Avg(Margin)
6. Output: summary.xlsx

Write equivalent Python using pandas. Comment each block with the
Alteryx tool it replaces. Print row counts after each step so I can
compare them with the Alteryx results.
```

Then **run both and compare row counts and totals**. That's how you build
trust in the translation, and in AI-generated code generally.

---

## Key takeaways
- An Alteryx workflow is a program; a table is a list of dicts (or a DataFrame).
- Multiple output anchors → functions that return several values.
- Formula ≈ a computed key; Multi-Row ≈ a loop that remembers the previous row; Summarize ≈ dict accumulators.
- The Python tool (`Alteryx.read` / `Alteryx.write`) lets you mix both worlds.

**Continue reading:** [Python Tool](https://help.alteryx.com/current/en/designer/tools/developer/python-tool.html) (Alteryx Designer documentation). How to use Python inside your workflows, including reading and writing data with the `ayx` package and managing packages. Use the version selector in Alteryx Help to read the 2025.1 page, since the tool changed in 2026.

**Next:** [Module A06: pandas for business analytics](../A06_pandas_analytics/lesson.md)
