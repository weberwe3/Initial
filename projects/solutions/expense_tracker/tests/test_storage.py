import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from expenses import storage  # noqa: E402
from expenses.models import Expense  # noqa: E402
import tracker  # noqa: E402


def test_missing_file_is_a_fresh_start(tmp_path):
    assert storage.load(tmp_path / "nope.json") == ([], {})


def test_save_then_load_round_trip(tmp_path):
    path = tmp_path / "data.json"
    items = [Expense(9.99, "fun", "Book", "2026-11-02")]
    storage.save(path, items, {"fun": 50})
    assert storage.load(path) == (items, {"fun": 50})


def test_import_bank_csv_maps_columns_and_reports_bad_rows(tmp_path):
    csv_path = tmp_path / "bank.csv"
    csv_path.write_text(
        "Transaction Date,Details,Transaction Amount\n"
        "2026-11-01,TESCO,-23.40\n"
        "2026-11-02,Coffee,\"1,003.50\"\n"
        "not a date,Broken,5\n",
        encoding="utf-8",
    )
    expenses, problems = storage.import_csv(csv_path)
    assert [e.amount for e in expenses] == [23.40, 1003.50]
    assert expenses[0].description == "TESCO"
    assert expenses[0].category == "uncategorised"
    assert len(problems) == 1 and "line 4" in problems[0]


def test_export_csv(tmp_path):
    out = tmp_path / "out.csv"
    storage.export_csv(out, [Expense(5, "food", "Snack", "2026-11-01")])
    assert out.read_text(encoding="utf-8").splitlines() == [
        "date,category,description,amount",
        "2026-11-01,food,Snack,5.00",
    ]


def test_cli_add_then_summary(tmp_path, capsys):
    data = tmp_path / "e.json"
    assert tracker.main(["--file", str(data), "add", "12.5", "food", "Lunch", "--date", "2026-11-03"]) == 0
    assert tracker.main(["--file", str(data), "budget", "food", "10"]) == 0
    assert tracker.main(["--file", str(data), "summary", "--month", "2026-11"]) == 0
    out = capsys.readouterr().out
    assert "November 2026" in out
    assert "over budget" in out


def test_cli_reports_bad_input_without_crashing(tmp_path, capsys):
    data = tmp_path / "e.json"
    assert tracker.main(["--file", str(data), "add", "-5", "food"]) == 1
    assert "Error" in capsys.readouterr().err
