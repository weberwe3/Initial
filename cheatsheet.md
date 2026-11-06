# Python Cheatsheet

Everything from the course on one page. Keep it open while you work.

## Basics
```python
x = 5                     # assign
x += 1                    # x = x + 1
type(x)                   # <class 'int'>
int("3"), float("2.5"), str(42), bool(0)
7 / 2 == 3.5;  7 // 2 == 3;  7 % 2 == 1;  2 ** 3 == 8
print("a", "b", sep="-", end="!\n")
name = input("Name: ")    # always a string
```

## Strings
```python
f"{name} is {age}"        f"{price:,.2f}"   f"{0.25:.0%}"   f"{x:>8}"
s[0]  s[-1]  s[1:4]  s[::-1]  len(s)
s.strip() .lower() .upper() .title() .replace(a, b)
s.split(",")  ",".join(items)  s.startswith("x")  "sub" in s
s.isdigit() .isalpha() .find("x") .count("x")
```

## Decisions
```python
if x > 10:
    ...
elif x == 10 and not done:
    ...
else:
    ...
value = "yes" if cond else "no"
x in (1, 2, 3)            # membership
```

## Loops
```python
for i in range(5): ...           # 0..4
for i in range(1, 11, 2): ...    # 1,3,5,7,9
for i, item in enumerate(items, start=1): ...
for a, b in zip(list1, list2): ...
while cond: ...
break / continue
```

## Lists & tuples
```python
nums = [3, 1, 2]
nums.append(4) .insert(0, x) .remove(x) .pop() .sort() .reverse() .extend([..])
sorted(nums, key=..., reverse=True)   sum(nums) min(nums) max(nums) len(nums)
copy = nums.copy()
point = (3, 4);  x, y = point;  first, *rest = nums
```

## Dicts & sets
```python
d = {"a": 1}
d["b"] = 2;  d.get("z", 0);  del d["a"];  "a" in d
for k, v in d.items(): ...
counts[k] = counts.get(k, 0) + 1          # counting pattern
s = {1, 2};  s.add(3);  a & b  a | b  a - b
from collections import Counter, defaultdict
```

## Comprehensions
```python
[x * 2 for x in nums if x > 0]
{k: v for k, v in pairs}
{x.lower() for x in words}
sum(x for x in nums)   any(...)   all(...)
```

## Functions
```python
def f(a, b=2, *args, **kwargs) -> int:
    """Docstring."""
    return a + b
f(1, b=3)
lambda x: x * 2
```

## Errors
```python
try:
    ...
except ValueError as e:
    ...
else:  ...    # no error
finally: ...  # always
raise ValueError("why")
```

## Files
```python
from pathlib import Path
p = Path(__file__).parent / "data" / "file.txt"
p.read_text(encoding="utf-8");  p.write_text(s, encoding="utf-8")
with open(p, "a", encoding="utf-8") as f: f.write("line\n")
for f in Path(".").glob("*.csv"): ...

import csv
with open(p, newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f): ...

import json
json.dump(obj, f, indent=2);  obj = json.load(f)
```

## Classes
```python
from dataclasses import dataclass, field

@dataclass
class Item:
    name: str
    price: float = 0.0
    tags: list = field(default_factory=list)

class Account:
    def __init__(self, owner):
        self.owner = owner
    def __str__(self):
        return self.owner
    @property
    def label(self): ...
```

## Power tools
```python
def gen():  yield 1              # generator
@functools.wraps(func)           # inside decorators
@contextmanager                  # with-able function
def cm():
    setup(); 
    try: yield
    finally: cleanup()
```

## Environment & packages
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install requests pytest
pip freeze > requirements.txt
pytest -v
```

## Reading a traceback
**Bottom line first** → that's *what* went wrong. The line above it → *where*.
