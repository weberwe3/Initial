"""
check.py - the course's friendly test runner.

Usage (from the top folder of the course):

    python check.py              # list every module and your progress
    python check.py 3            # check your answers for Python module 03
    python check.py A5           # check your answers for AI-track module A05
    python check.py 3 --solutions   # check the official solutions instead

You never need to edit this file. It loads your exercises.py, runs the
checks in tests.py against it, and tells you what passed and what didn't.
"""

import importlib.util
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).parent
MODULES = ROOT / "modules"
AI_MODULES = ROOT / "ai"

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
DIM = "\033[2m"
BOLD = "\033[1m"
RESET = "\033[0m"

if not sys.stdout.isatty():
    GREEN = RED = YELLOW = DIM = BOLD = RESET = ""


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    # Let a module's files import each other (e.g. helpers next to exercises).
    sys.path.insert(0, str(path.parent))
    try:
        spec.loader.exec_module(module)
    finally:
        sys.path.pop(0)
    return module


def find_module(number):
    text = str(number).strip().upper()
    if text.startswith("A"):
        if not text[1:].isdigit():
            return None
        matches = sorted(AI_MODULES.glob(f"A{int(text[1:]):02d}_*"))
    elif text.isdigit():
        matches = sorted(MODULES.glob(f"{int(text):02d}_*"))
    else:
        return None
    return matches[0] if matches else None


def run_module(folder, use_solutions=False, quiet=False):
    target = folder / ("solutions.py" if use_solutions else "exercises.py")
    tests_file = folder / "tests.py"
    if not tests_file.exists():
        if not quiet:
            print(f"{DIM}{folder.name} has no automatic checks (read the lesson!).{RESET}")
        return None

    try:
        student = load(target, f"student_{folder.name}")
    except ModuleNotFoundError as e:
        if not quiet:
            print(f"{RED}{target.name} needs a package that isn't installed: {e.name}{RESET}")
            print(f"Install it (ideally inside a virtual environment, see Module 10):\n\n    pip install {e.name}\n")
        return (0, 1)
    except Exception:
        if not quiet:
            print(f"{RED}Your file {target.name} could not even be loaded.{RESET}")
            print("That usually means a typo (SyntaxError) or an error at the top level.")
            print("Here is what Python said - read the LAST line first:\n")
            traceback.print_exc(limit=1)
        return (0, 1)

    tests = load(tests_file, f"tests_{folder.name}")
    checks = [(n, f) for n, f in vars(tests).items() if n.startswith("test_") and callable(f)]

    passed = 0
    for name, fn in checks:
        label = name[5:].replace("_", " ")
        try:
            fn(student)
        except NotImplementedError:
            if not quiet:
                print(f"  {YELLOW}…{RESET} {label} {DIM}(not started yet){RESET}")
        except AssertionError as e:
            if not quiet:
                msg = str(e) or "the answer wasn't what was expected"
                print(f"  {RED}✗{RESET} {label}\n      {DIM}{msg}{RESET}")
        except Exception as e:
            if not quiet:
                print(f"  {RED}✗{RESET} {label}\n      {DIM}crashed with {type(e).__name__}: {e}{RESET}")
        else:
            passed += 1
            if not quiet:
                print(f"  {GREEN}✓{RESET} {label}")
    return (passed, len(checks))


def overview():
    print(f"\n{BOLD}Python Foundry - your progress{RESET}")
    folders = []
    for title, root in [("Python track", MODULES), ("AI track", AI_MODULES)]:
        if root.is_dir():
            folders.append(title)
            folders.extend(f for f in sorted(root.iterdir()) if f.is_dir())
    for folder in folders:
        if isinstance(folder, str):
            print(f"\n  {BOLD}{folder}{RESET}")
            continue
        result = run_module(folder, quiet=True)
        if result is None:
            status = f"{DIM}reading only{RESET}"
        else:
            p, t = result
            bar = "█" * p + "░" * (t - p)
            colour = GREEN if p == t else (YELLOW if p else DIM)
            status = f"{colour}{bar} {p}/{t}{RESET}"
        print(f"  {folder.name:<32} {status}")
    print(f"\nRun {BOLD}python check.py <number>{RESET} to see details for one module.\n")


def main(argv):
    if not argv:
        overview()
        return 0
    folder = find_module(argv[0])
    if folder is None:
        print(f"No module numbered {argv[0]}. Try: python check.py")
        return 1
    use_solutions = "--solutions" in argv
    print(f"\n{BOLD}{folder.name}{RESET}" + (f" {DIM}(solutions){RESET}" if use_solutions else ""))
    result = run_module(folder, use_solutions)
    if result is None:
        return 0
    p, t = result
    if p == t:
        print(f"\n{GREEN}{BOLD}All {t} checks passed. Nice work - on to the next module!{RESET}\n")
        return 0
    print(f"\n{p}/{t} passed. Fix one thing at a time, then run this again.\n")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
