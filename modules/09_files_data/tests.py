import json
import tempfile
from pathlib import Path

CSV_TEXT = """date,category,description,amount
2026-10-01,rent,October rent,1200.00
2026-10-02,food,Groceries,84.20
2026-10-05,food,"Dinner out, birthday",56.75
"""


def _tmp():
    return Path(tempfile.mkdtemp())


def test_count_lines(ex):
    p = _tmp() / "a.txt"
    p.write_text("one\ntwo\nthree\n", encoding="utf-8")
    assert ex.count_lines(p) == 3


def test_longest_line(ex):
    p = _tmp() / "a.txt"
    p.write_text("short\nthe longest one\nmid size\n", encoding="utf-8")
    assert ex.longest_line(p) == "the longest one"


def test_write_lines(ex):
    p = _tmp() / "out.txt"
    p.write_text("OLD CONTENT\n", encoding="utf-8")
    ex.write_lines(p, ["a", "b"])
    assert p.read_text(encoding="utf-8") == "a\nb\n", "should overwrite, one item per line"


def test_append_log(ex):
    p = _tmp() / "log.txt"
    ex.append_log(p, "first")
    ex.append_log(p, "second")
    assert p.read_text(encoding="utf-8") == "first\nsecond\n"


def test_load_expenses(ex):
    p = _tmp() / "e.csv"
    p.write_text(CSV_TEXT, encoding="utf-8")
    rows = ex.load_expenses(p)
    assert len(rows) == 3
    assert rows[0]["amount"] == 1200.0, "amount should be a float"
    assert rows[2]["description"] == "Dinner out, birthday", "use the csv module - it handles quoted commas"


def test_category_totals_from_csv(ex):
    p = _tmp() / "e.csv"
    p.write_text(CSV_TEXT, encoding="utf-8")
    assert ex.category_totals_from_csv(p) == {"rent": 1200.0, "food": 140.95}


def test_write_summary_csv(ex):
    p = _tmp() / "s.csv"
    ex.write_summary_csv(p, {"rent": 1200.0, "food": 140.95})
    lines = p.read_text(encoding="utf-8").strip().splitlines()
    assert lines[0] == "category,total", f"header was {lines[0]!r}"
    assert "rent,1200.0" in lines and "food,140.95" in lines


def test_save_and_load_json(ex):
    p = _tmp() / "d.json"
    data = {"name": "Ada", "skills": ["python", "maths"]}
    ex.save_json(p, data)
    assert json.loads(p.read_text(encoding="utf-8")) == data
    assert ex.load_json(p) == data


def test_load_json_missing(ex):
    assert ex.load_json(_tmp() / "nope.json", {"empty": True}) == {"empty": True}


def test_files_by_extension(ex):
    d = _tmp()
    for name in ["a.txt", "b.TXT", "c.csv", "README"]:
        (d / name).write_text("x")
    (d / "sub.folder").mkdir()
    assert ex.files_by_extension(d) == {"txt": 2, "csv": 1, "": 1}
