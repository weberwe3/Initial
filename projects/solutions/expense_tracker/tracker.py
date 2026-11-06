"""
Expense tracker - command-line interface.

    python tracker.py add 12.50 food "Lunch with Sam"
    python tracker.py list --month 2026-11
    python tracker.py summary
    python tracker.py import bank.csv
    python tracker.py export out.csv --month 2026-11
    python tracker.py budget food 300

Only this file prints or reads arguments. All the logic lives in expenses/.
"""

import argparse
import sys
from datetime import date
from pathlib import Path

from expenses import reports, storage
from expenses.models import Expense

DEFAULT_FILE = Path("expenses.json")


def money(x: float) -> str:
    return f"${x:,.2f}"


def cmd_add(args, expenses, budgets):
    e = Expense(args.amount, args.category, args.description, args.date or date.today().isoformat())
    expenses.append(e)
    print(f"Added {money(e.amount)} for {e.category} on {e.date}.")
    return True  # data changed - save it


def cmd_list(args, expenses, budgets):
    shown = reports.filter_expenses(expenses, args.month, args.category)
    if not shown:
        print("No matching expenses.")
        return False
    for e in shown:
        print(f"{e.date}  {e.category:<14} {money(e.amount):>11}  {e.description}")
    print(f"{'':12}{'Total':<14} {money(reports.total(shown)):>11}")
    return False


def cmd_summary(args, expenses, budgets):
    month = args.month or date.today().isoformat()[:7]
    shown = reports.filter_expenses(expenses, month)
    print(reports.month_label(month))
    print("─" * 40)
    if not shown:
        print("Nothing recorded this month.")
        return False
    totals = reports.totals_by_category(shown)
    over = reports.over_budget(totals, budgets)
    for category, amount in totals.items():
        warning = f"   ⚠ over budget ({money(over[category])})" if category in over else ""
        print(f"{category:<14}{money(amount):>11}{warning}")
    print("─" * 40)
    print(f"{'Total':<14}{money(reports.total(shown)):>11}")
    big = reports.biggest(shown)
    print(f"Biggest expense: {big.description or big.category} ({money(big.amount)})")
    return False


def cmd_import(args, expenses, budgets):
    new, problems = storage.import_csv(args.csv_file)
    expenses.extend(new)
    print(f"Imported {len(new)} expenses.")
    for p in problems:
        print(f"  skipped {p}")
    return bool(new)


def cmd_export(args, expenses, budgets):
    shown = reports.filter_expenses(expenses, args.month, args.category)
    storage.export_csv(args.csv_file, shown)
    print(f"Wrote {len(shown)} expenses to {args.csv_file}.")
    return False


def cmd_budget(args, expenses, budgets):
    budgets[args.category.lower()] = args.limit
    print(f"Monthly budget for {args.category}: {money(args.limit)}")
    return True


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Track your spending.")
    parser.add_argument("--file", type=Path, default=DEFAULT_FILE, help="data file (default: expenses.json)")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("add", help="record an expense")
    p.add_argument("amount", type=float)
    p.add_argument("category")
    p.add_argument("description", nargs="?", default="")
    p.add_argument("--date", help="YYYY-MM-DD (default: today)")
    p.set_defaults(func=cmd_add)

    for name, func, helptext in [("list", cmd_list, "show expenses"),
                                 ("export", cmd_export, "write expenses to CSV")]:
        p = sub.add_parser(name, help=helptext)
        if name == "export":
            p.add_argument("csv_file", type=Path)
        p.add_argument("--month", help="YYYY-MM")
        p.add_argument("--category")
        p.set_defaults(func=func)

    p = sub.add_parser("summary", help="monthly report by category")
    p.add_argument("--month", help="YYYY-MM (default: this month)")
    p.set_defaults(func=cmd_summary)

    p = sub.add_parser("import", help="import a bank CSV export")
    p.add_argument("csv_file", type=Path)
    p.set_defaults(func=cmd_import)

    p = sub.add_parser("budget", help="set a monthly budget for a category")
    p.add_argument("category")
    p.add_argument("limit", type=float)
    p.set_defaults(func=cmd_budget)
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        expenses, budgets = storage.load(args.file)
        changed = args.func(args, expenses, budgets)
    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    if changed:
        storage.save(args.file, expenses, budgets)
    return 0


if __name__ == "__main__":
    sys.exit(main())
