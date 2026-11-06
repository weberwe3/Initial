# Module 09: Files & Data

**Goal:** read and write text, CSV and JSON files, and work with folders.
**Time:** 4 hours.

This is where Python becomes *useful in your actual life*. Spreadsheets,
exports, logs, and folders full of files are all now things you can automate.

Sample files for this module are in [`data/`](data/).

---

## 1. Paths with `pathlib`

```python
from pathlib import Path

data_dir = Path("data")
file = data_dir / "notes.txt"      # join paths with /  (works on Windows too)

file.name        # 'notes.txt'
file.stem        # 'notes'
file.suffix      # '.txt'
file.parent      # Path('data')
file.exists()    # True / False
Path.home()      # your home folder
Path.cwd()       # the folder you ran Python from
```

> ⚠️ Relative paths like `"data/notes.txt"` are relative to where you **ran**
> the program from, not where the `.py` file lives. To be safe in scripts:
> ```python
> HERE = Path(__file__).parent
> file = HERE / "data" / "notes.txt"
> ```

---

## 2. Reading and writing text

### The quick way
```python
text = Path("data/notes.txt").read_text(encoding="utf-8")
Path("output.txt").write_text("Hello file!\n", encoding="utf-8")
```

### The `with open(...)` way (more control)
```python
with open("data/notes.txt", encoding="utf-8") as f:
    for line in f:                  # reads one line at a time, so it's memory-friendly
        print(line.rstrip("\n"))

with open("log.txt", "a", encoding="utf-8") as f:   # "a" = append
    f.write("Another line\n")
```

| Mode | Meaning |
|------|---------|
| `"r"` | read (default) |
| `"w"` | write: **erases** the file first! |
| `"a"` | append to the end |

`with` automatically closes the file when the block ends, even if an error
happens. Always use it with `open`.

Always pass `encoding="utf-8"`. Otherwise accented characters and emoji can
break on Windows.

---

## 3. CSV files (spreadsheet data)

CSV = "comma-separated values". Every spreadsheet program can export it.

`data/expenses.csv`:
```
date,category,description,amount
2026-10-01,rent,October rent,1200.00
2026-10-02,food,Groceries,84.20
...
```

### Reading as dictionaries (recommended)
```python
import csv

with open("data/expenses.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["category"], float(row["amount"]))
```

Each row is a dict keyed by the header row. **Every value is a string**, so
convert numbers with `float()` / `int()`.

### Writing
```python
rows = [
    {"name": "Ada", "score": 95},
    {"name": "Grace", "score": 98},
]
with open("scores.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(rows)
```

(`newline=""` stops blank lines appearing between rows on Windows.)

Why not just `line.split(",")`? Because real CSVs contain commas inside quoted
fields: `"Smith, John",42`. The `csv` module handles that correctly.

---

## 4. JSON (structured data)

JSON looks almost exactly like Python dicts and lists. It's the language of
web APIs and config files.

```python
import json

settings = {"theme": "dark", "font_size": 14, "recent": ["a.txt", "b.txt"]}

# Python → JSON file
with open("settings.json", "w", encoding="utf-8") as f:
    json.dump(settings, f, indent=2)

# JSON file → Python
with open("settings.json", encoding="utf-8") as f:
    loaded = json.load(f)

# To/from strings
text = json.dumps(settings)
back = json.loads(text)
```

JSON is perfect for **saving your program's state** between runs (you'll do
exactly that in Project 2).

---

## 5. Working with folders

```python
from pathlib import Path

folder = Path("data")

for p in folder.iterdir():             # everything in the folder
    print(p.name, "folder" if p.is_dir() else "file")

for p in folder.glob("*.csv"):         # matching a pattern
    print(p)

for p in folder.rglob("*.txt"):        # recursive: includes subfolders
    print(p)

Path("output/reports").mkdir(parents=True, exist_ok=True)   # create folders
```

Renaming / moving / copying:

```python
import shutil

src = Path("report.txt")
src.rename("archive/report.txt")       # move / rename
shutil.copy("a.txt", "backup/a.txt")   # copy
```

> ⚠️ Scripts that move or delete files should **print what they would do
> first** (a "dry run") before you let them actually do it.

---

## 6. Real-world example: a monthly spending report

```python
import csv
from pathlib import Path

HERE = Path(__file__).parent

def load_expenses(path):
    with open(path, newline="", encoding="utf-8") as f:
        return [
            {**row, "amount": float(row["amount"])}
            for row in csv.DictReader(f)
        ]

def totals_by_category(expenses):
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    return totals

expenses = load_expenses(HERE / "data" / "expenses.csv")
for category, total in totals_by_category(expenses).items():
    print(f"{category:<12} ${total:>9,.2f}")
```

(`{**row, "amount": ...}` means "copy all of row's keys, then override
`amount`". It's a neat trick for dicts.)

---

## Key takeaways
- Use `pathlib.Path` for paths; `Path(__file__).parent` for files next to your script.
- `with open(path, encoding="utf-8") as f:`. `"w"` erases, `"a"` appends.
- `csv.DictReader` / `DictWriter` for spreadsheets; values come back as strings.
- `json.load` / `json.dump` to save and load Python data.
- `glob` / `rglob` to find files; dry-run before moving anything.

**Continue reading:** [Reading and Writing Files](https://automatetheboringstuff.com/3e/chapter10.html) (Automate the Boring Stuff with Python, 3rd ed., chapter 10). Paths, files and saving data, from the classic free book on practical automation.

**Next:** [Module 10: Modules, packages & pip](../10_modules_packages/lesson.md)
