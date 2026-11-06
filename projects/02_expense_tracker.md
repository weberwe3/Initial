# Checkpoint Project 2: Personal Expense Tracker

**After:** Module 10 · **Time:** 8–12 hours (spread over a week)

Build a command-line tool you'll actually use to track your spending. It saves
data between runs, imports bank CSV exports, and prints monthly reports.

This is your first *multi-file* program. A reference solution lives in
[`solutions/expense_tracker/`](solutions/expense_tracker/). Look at the
structure if you're stuck on organisation, but write your own code.

---

## What it should do

```bash
python tracker.py add 12.50 food "Lunch with Sam"
python tracker.py add 1200 rent "November rent" --date 2026-11-01
python tracker.py list
python tracker.py list --month 2026-11 --category food
python tracker.py summary --month 2026-11
python tracker.py import bank_export.csv
python tracker.py export november.csv --month 2026-11
python tracker.py budget food 300        # set a monthly budget for a category
```

Example `summary` output:

```
November 2026
────────────────────────────────────
rent          $1,200.00
food            $412.30   ⚠ over budget ($300.00)
transport        $65.00
fun             $134.00
────────────────────────────────────
Total         $1,811.30
Biggest expense: November rent ($1,200.00)
```

---

## Suggested structure

```
expense_tracker/
    tracker.py            # command-line interface only (argparse, printing)
    expenses/
        __init__.py
        models.py         # Expense dataclass
        storage.py        # load/save JSON, import/export CSV
        reports.py        # pure functions: filter, totals, summaries
    tests/
        test_reports.py
        test_storage.py
```

**The key design rule:** `reports.py` and `models.py` never call `print()` or
`input()`. They take data in and return data out. Only `tracker.py` talks to
the user. This keeps the logic testable (Module 13).

---

## Milestones

Build it in this order, getting each step working before the next.

1. **Model.** An `Expense` dataclass: `amount`, `category`, `description`, `date`
   (store dates as `"YYYY-MM-DD"` strings for easy JSON and sorting).
2. **Storage.** `load_expenses(path)` / `save_expenses(path, expenses)` using
   JSON. A missing file means "no expenses yet", not a crash.
3. **`add` and `list` commands** with `argparse` subcommands.
4. **Reports.** `filter_expenses(expenses, month=None, category=None)`,
   `totals_by_category(expenses)`, `biggest(expenses)`. Write tests for these
   *first* (TDD) or *straight after*.
5. **`summary` command** with nicely aligned output.
6. **CSV import/export.** Real bank exports have different column names; map
   them (e.g. `"Transaction Amount"` → `amount`). Skip and report rows that
   can't be parsed instead of crashing.
7. **Budgets.** Store per-category monthly limits in the same JSON file and
   flag overspending in the summary.

### Level up
- `delete` / `edit` commands (give each expense an `id`).
- Auto-categorise imported rows by keyword ("TESCO" → food).
- A bar chart in the terminal using `"█" * int(amount / scale)`.
- Install `rich` and print a coloured table.
- Recurring expenses (rent every month).

---

## Skills checklist
- [ ] Multiple modules in a package, imported from a main script
- [ ] A dataclass
- [ ] JSON persistence with graceful handling of a missing file
- [ ] CSV reading and writing with `csv.DictReader` / `DictWriter`
- [ ] `argparse` with subcommands
- [ ] Input validation with helpful error messages
- [ ] At least 8 pytest tests, all passing
