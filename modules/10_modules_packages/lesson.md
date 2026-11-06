# Module 10: Modules, Packages & pip

**Goal:** split code across files, use Python's huge standard library, and
install third-party packages safely with virtual environments.
**Time:** 3–4 hours.

---

## 1. Importing

A **module** is just a `.py` file. `import` lets you use code from another one.

```python
import math
math.sqrt(16)        # 4.0
math.pi              # 3.14159...

from math import sqrt, pi   # import specific names
sqrt(16)

import datetime as dt       # give it a shorter name
dt.date.today()
```

Prefer `import module` or `from module import name`. Avoid `from module import *`:
it dumps unknown names into your file and makes it unclear where things come from.

---

## 2. Your own modules

Make `money.py`:

```python
# money.py
def format_money(amount):
    return f"${amount:,.2f}"

TAX_RATE = 0.2
```

Then in `main.py`, in the **same folder**:

```python
from money import format_money, TAX_RATE
print(format_money(100 * (1 + TAX_RATE)))
```

### Why `if __name__ == "__main__":`
When Python imports `money.py`, it runs the whole file. Anything at the top
level, like a test `print` or `input()`, would run too. Code under
`if __name__ == "__main__":` only runs when the file is executed directly:

```python
# money.py
def format_money(amount):
    return f"${amount:,.2f}"

if __name__ == "__main__":
    print(format_money(1234.5))   # quick manual test; doesn't run on import
```

### Packages
A **package** is a folder of modules:

```
budget_app/
    main.py
    budget/
        __init__.py      # can be empty; marks the folder as a package
        storage.py
        reports.py
```

```python
# in main.py
from budget.storage import load_expenses
from budget.reports import monthly_summary
```

Project 2 is structured this way.

---

## 3. The standard library: batteries included

Python ships with hundreds of modules. The ones worth knowing now:

```python
# Dates and times
from datetime import date, datetime, timedelta
today = date.today()
deadline = today + timedelta(days=30)
(deadline - today).days                      # 30
datetime.now().strftime("%Y-%m-%d %H:%M")    # '2026-11-06 14:05'
datetime.strptime("06/11/2026", "%d/%m/%Y")  # parse text into a datetime

# Random
import random
random.randint(1, 6)            # dice roll
random.choice(["a", "b", "c"])  # pick one
random.shuffle(my_list)         # shuffle in place

# Counting made easy
from collections import Counter, defaultdict
Counter("mississippi").most_common(2)   # [('i', 4), ('s', 4)]
groups = defaultdict(list)               # missing keys start as []
groups["food"].append(12.5)

# Statistics
import statistics
statistics.mean([1, 2, 3, 4])     # 2.5
statistics.median([3, 1, 2])      # 2

# Talking to the operating system
import os, sys, shutil
os.environ.get("HOME")
sys.argv                 # command-line arguments

# Command-line tools
import argparse          # proper command-line options (see below)
```

Browse the full list: <https://docs.python.org/3/library/>. Before writing
something general-purpose, check whether the standard library already has it.

### Command-line arguments with `argparse`
```python
import argparse

parser = argparse.ArgumentParser(description="Convert temperatures")
parser.add_argument("celsius", type=float)
parser.add_argument("--round", type=int, default=1)
args = parser.parse_args()
print(round(args.celsius * 9 / 5 + 32, args.round))
```
```bash
python convert.py 21.5 --round 0
python convert.py --help         # free help text!
```

---

## 4. Third-party packages and `pip`

Beyond the standard library, there are 500,000+ packages on
[PyPI](https://pypi.org). You install them with `pip`.

### Always use a virtual environment ("venv")
A venv is a private folder of packages for one project, so projects don't
fight over versions.

```bash
# create it once, inside your project folder
python -m venv .venv

# activate it (every time you open a new terminal)
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

# your prompt now starts with (.venv)
pip install requests
pip list
pip freeze > requirements.txt     # record exact versions

# later / on another computer:
pip install -r requirements.txt
```

VS Code: *Ctrl+Shift+P → "Python: Select Interpreter"* and pick `.venv`.

### Packages worth knowing exist
| Package | For |
|---------|-----|
| `requests` / `httpx` | Calling web APIs (Module 14) |
| `pytest` | Testing (Module 13) |
| `pandas` | Data analysis, Excel/CSV wrangling |
| `openpyxl` | Reading/writing Excel files |
| `matplotlib` | Charts |
| `rich` | Beautiful terminal output |
| `flask` / `fastapi` | Web apps and APIs |
| `pygame` | Games |

### ⚠️ Safety
Installing a package runs code from the internet on your computer. Check the
spelling (typo-squatting is a real attack), prefer well-known packages with
many downloads, and look at the project's homepage before installing.

---

## Key takeaways
- `import module` / `from module import name`. Your own `.py` files are modules.
- Guard script code with `if __name__ == "__main__":`.
- Learn `datetime`, `random`, `collections`, `pathlib`, `csv`, `json`, `argparse`.
- One **venv** per project; `pip install` inside it; `requirements.txt` to record it.

**Continue reading:** [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html) (the official Python tutorial). venv and pip explained by the Python docs themselves.

**Checkpoint:** you've finished Part 2. Build
[Project 2: Expense tracker](../../projects/02_expense_tracker.md).

**Next:** [Module 11: Pythonic code](../11_pythonic_code/lesson.md)
