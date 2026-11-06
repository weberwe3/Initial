# Module 15: Intermediate Power Tools

**Goal:** understand the features that separate intermediate Python from
beginner Python: generators, decorators, context managers, and type hints.
**Time:** 4–5 hours.

You'll see these constantly in other people's code and in libraries. After
this module, they'll read as tools rather than magic.

---

## 1. Iterators and generators

A `for` loop works on anything *iterable*: lists, strings, files, dicts,
`range`... A **generator** is a function that produces values *one at a time*,
on demand, using `yield`:

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i          # hand back a value, pause here until the next one is requested
        i += 1

for x in count_up_to(3):
    print(x)             # 1, 2, 3

gen = count_up_to(3)
next(gen)   # 1
next(gen)   # 2
```

### Why bother?
**Memory and laziness.** A list of a billion numbers needs gigabytes. A
generator needs almost nothing, because each value is made only when needed.

```python
def read_large_log(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            if "ERROR" in line:
                yield line.rstrip()

for error in read_large_log("server.log"):   # works on a 50 GB file
    print(error)
```

### Pipelines
Generators chain together like an assembly line:

```python
lines = read_lines("data.csv")
rows = (line.split(",") for line in lines)
big = (r for r in rows if float(r[3]) > 100)
for r in big:
    print(r)
```

Nothing is read until the final loop asks for it.

### `itertools`: the generator toolkit
```python
import itertools
list(itertools.islice(count_up_to(1000), 5))   # first 5 only: [1, 2, 3, 4, 5]
itertools.chain([1, 2], [3])                   # 1, 2, 3
for key, group in itertools.groupby(sorted_items, key=lambda x: x["category"]):
    ...
```

---

## 2. Decorators

Remember that functions are values (Module 07)? A **decorator** is a function
that takes a function and returns an upgraded version of it.

```python
import time
import functools

def timer(func):
    @functools.wraps(func)                # keeps the original name/docstring
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)    # call the original
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.3f}s")
        return result
    return wrapper

@timer
def slow_add(a, b):
    time.sleep(0.5)
    return a + b

slow_add(2, 3)     # prints "slow_add took 0.501s", returns 5
```

`@timer` above a function is shorthand for `slow_add = timer(slow_add)`.

The `*args, **kwargs` pattern means "accept any arguments and pass them all
through", so the wrapper works with any function.

### Decorators you'll meet in the wild
```python
@dataclass                      # Module 12
@property                       # Module 12
@functools.cache                # remember results of expensive calls
@pytest.fixture                 # Module 13
@app.get("/users")              # web frameworks (FastAPI/Flask) map URLs to functions
```

### Decorators with arguments
```python
def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == times:
                        raise
                    print(f"Attempt {attempt} failed, retrying…")
        return wrapper
    return decorator

@retry(times=3)
def flaky_download():
    ...
```

Three levels of functions: `retry(3)` returns a decorator, which wraps your
function. It's the trickiest pattern in this course. Re-read it slowly.

---

## 3. Context managers (`with`)

You've used `with open(...) as f:`, which guarantees the file is closed even if
an error occurs. You can make your own:

```python
from contextlib import contextmanager
import time

@contextmanager
def timed(label):
    start = time.perf_counter()
    try:
        yield                         # the body of the `with` block runs here
    finally:
        print(f"{label}: {time.perf_counter() - start:.3f}s")

with timed("loading data"):
    data = load_everything()
```

Everything before `yield` is setup; everything after (in `finally`) is
cleanup that **always** runs.

The class version uses `__enter__` and `__exit__`:

```python
class ChangeDirectory:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.old = os.getcwd()
        os.chdir(self.path)
        return self

    def __exit__(self, exc_type, exc, tb):
        os.chdir(self.old)          # always go back
        return False                # don't hide exceptions
```

Use context managers for anything with a "set up → use → clean up" shape:
files, database connections, locks, temporary changes.

---

## 4. Type hints

Type hints say what types a function expects and returns:

```python
def apply_discount(price: float, percent: float = 0) -> float:
    return round(price * (1 - percent / 100), 2)

def average(numbers: list[float]) -> float: ...
def find_user(user_id: int) -> dict | None: ...      # might return None
def counts(words: list[str]) -> dict[str, int]: ...
```

Python **does not enforce** these at runtime. They're for:
- **You and your readers**: the signature documents itself.
- **Your editor**: VS Code autocompletes and warns about mistakes.
- **Type checkers** like `mypy` or `pyright`, which catch bugs before you run the code:
  ```bash
  pip install mypy
  mypy my_script.py
  ```

Add hints to function signatures in any code you'll keep. Skip them for quick
throwaway scripts.

---

## 5. A few more things worth knowing

```python
# match statement: structural pattern matching (Python 3.10+)
match command.split():
    case ["add", item]:
        add(item)
    case ["remove", item]:
        remove(item)
    case ["quit"]:
        quit()
    case _:
        print("Unknown command")

# Enum: a fixed set of named options
from enum import Enum
class Status(Enum):
    TODO = "todo"
    DONE = "done"

# logging: better than print for real programs
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logging.info("Processing %d files", 12)
logging.warning("Disk almost full")
```

---

## Key takeaways
- **Generators** (`yield`) produce values lazily, which is great for big data and pipelines.
- **Decorators** wrap functions to add behaviour: `@timer`, `@retry(3)`, `@cache`.
- **Context managers** (`with`) guarantee cleanup; build them with `@contextmanager`.
- **Type hints** document intent and let tools catch bugs.

**You've finished the lessons!** Time for the
[Capstone project](../../projects/03_capstone.md).
