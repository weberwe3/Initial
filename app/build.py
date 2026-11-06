"""
Build the interactive course into one self-contained HTML file.

    python app/build.py            # writes app/dist/index.html (+ checks quiz answers)
    python app/build.py --engine   # also downloads the Python-in-the-browser engine
                                   # into app/dist/pyodide/ (needed only for hosting
                                   # where CDN fetches are blocked)

The lessons, exercises, tests and solutions are read straight from modules/,
so the terminal course and the interactive course never drift apart.
"""

import contextlib
import io
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APP = ROOT / "app"
DIST = APP / "dist"
sys.path.insert(0, str(APP))

from learning_content import M as M_PY  # noqa: E402
from learning_content_ai import M_AI  # noqa: E402

M = {**M_PY, **M_AI}

PYODIDE_VERSION = "0.26.4"
ENGINE_FILES = ["pyodide.js", "pyodide.asm.js", "pyodide.asm.wasm", "python_stdlib.zip", "pyodide-lock.json"]

TRACKS = [
    {"id": "python", "name": "Python", "long": "Python: zero to intermediate"},
    {"id": "ai", "name": "AI", "long": "AI for business: zero to super user"},
]
# (part name, module ids, track id)
PARTS = [
    ("Part 1 · Foundations", ["00", "01", "02", "03", "04", "05", "06"], "python"),
    ("Part 2 · Real programs", ["07", "08", "09", "10"], "python"),
    ("Part 3 · Intermediate", ["11", "12", "13", "14", "15"], "python"),
    ("Part 1 · AI foundations", ["A00", "A01", "A02", "A03"], "ai"),
    ("Part 2 · AI + Python for analytics", ["A04", "A05", "A06", "A07", "A08", "A09"], "ai"),
    ("Part 3 · Super user & ambassador", ["A10", "A11", "A12", "A13"], "ai"),
]
TRACK_ROOTS = [("python", ROOT / "modules"), ("ai", ROOT / "ai")]

# The recommended order: both tracks interleaved, every module after the ones it builds on.
# Steps are module ids ("05", "A05") or project routes ("project-1").
PATH = [
    {"name": "Orientation & first wins", "weeks": "Weeks 1–2", "steps": ["A00", "00", "A01", "A02"],
     "why": "Start with AI you can use at work tomorrow: early, visible payoffs keep motivation high. "
            "Python is installed in parallel so coding can start next phase."},
    {"name": "Use AI safely; write your first code", "weeks": "Weeks 3–5", "steps": ["A03", "01", "02", "03", "04"],
     "why": "Guardrails come before any work data touches an AI tool. Python basics are spread over three weeks "
            "so each idea gets practice and review before the next one arrives."},
    {"name": "Data in Python + AI-assisted analysis", "weeks": "Weeks 6–8", "steps": ["05", "06", "A04", "project-1"],
     "why": "A04's exercises use lists and dictionaries, so those come first. Project 1 consolidates everything so far, "
            "and building from memory is retrieval practice at its strongest."},
    {"name": "Lead early; write real programs", "weeks": "Weeks 9–11", "steps": ["A12", "07", "08", "A05"],
     "why": "You're already an AI ambassador, so the playbook comes early: start a pilot now and let it run while you learn. "
            "A05 (Alteryx to Python) needs functions (07) and benefits from error handling (08)."},
    {"name": "Files, packages and pandas", "weeks": "Weeks 12–14", "steps": ["09", "10", "A06", "project-2"],
     "why": "pandas runs in a virtual environment (10) and reads files (09). Project 2 is the best consolidation "
            "of Python Part 2 and a strong portfolio piece."},
    {"name": "AI from code", "weeks": "Weeks 15–17", "steps": ["11", "14", "A07", "A08"],
     "why": "Calling AI from Python uses comprehensions (11) and web/API skills (14). Evaluation (A08) follows "
            "straight away, so you never put unmeasured AI into a workflow."},
    {"name": "Advanced patterns", "weeks": "Weeks 18–21", "steps": ["12", "13", "A09", "15", "A10", "A11"],
     "why": "Classes and tests make bigger programs reliable. Decorators (15) are exactly what @mcp.tool() uses, "
            "so they come right before agents, MCP and Skills."},
    {"name": "Prove it and position yourself", "weeks": "Weeks 22–26", "steps": ["project-ai", "A13", "project-3"],
     "why": "The AI capstone ties every skill into portfolio evidence, and the career module turns it into your next role. "
            "The Python capstone is optional if your AI capstone meets its checklist."},
]

# Soft prerequisites (the app warns, it never blocks). Used to validate PATH at build time.
PREREQS = {
    "01": ["00"], "02": ["01"], "03": ["02"], "04": ["03"], "05": ["04"], "06": ["05"], "07": ["06"],
    "08": ["07"], "09": ["08"], "10": ["09"], "11": ["10"], "12": ["11"], "13": ["12"], "14": ["10", "11"],
    "15": ["12"],
    "A01": ["A00"], "A02": ["A01"], "A03": ["A02"], "A04": ["A03", "06"], "A05": ["A04", "07"],
    "A06": ["A05", "10"], "A07": ["A01", "08", "11", "14"], "A08": ["A07", "11"], "A09": ["A08"],
    "A10": ["A07", "08"], "A11": ["A10", "15"], "A12": ["A02", "A03"], "A13": ["A12"],
}


def validate_path(module_ids, project_routes):
    steps = [s for phase in PATH for s in phase["steps"]]
    expected = set(module_ids) | set(project_routes)
    if sorted(steps) != sorted(expected):
        raise SystemExit(f"PATH must list every module and project exactly once. "
                         f"Missing: {sorted(expected - set(steps))}, extra/duplicate: "
                         f"{sorted(x for x in steps if steps.count(x) > 1 or x not in expected)}")
    position = {s: i for i, s in enumerate(steps)}
    for mid, reqs in PREREQS.items():
        for r in reqs:
            if position[r] > position[mid]:
                raise SystemExit(f"PATH puts {mid} before its prerequisite {r}")


def rewrite_links(md: str) -> str:
    # ../04_loops/lesson.md -> #m-04 ; ../../projects/02_x.md -> #project-2 ; cheatsheet
    md = re.sub(r"\((?:\.\./)*modules/(\d\d)_[a-z_]+/lesson\.md\)", r"(#m-\1)", md)
    md = re.sub(r"\(\.\./(\d\d)_[a-z_]+/lesson\.md\)", r"(#m-\1)", md)
    md = re.sub(r"\((?:\.\./)*projects/0(\d)_[a-z_]+\.md\)", r"(#project-\1)", md)
    md = re.sub(r"\((?:\.\./)*ai/(A\d\d)_[a-z_]+/lesson\.md\)", r"(#m-\1)", md)
    md = re.sub(r"\(\.\./(A\d\d)_[a-z_]+/lesson\.md\)", r"(#m-\1)", md)
    md = re.sub(r"\((?:\.\./)*projects/A_capstone\.md\)", "(#project-ai)", md)
    md = re.sub(r"\((?:\.\./)*cheatsheet\.md\)", "(#cheatsheet)", md)
    md = re.sub(r"\[`?data/`?\]\(data/\)", "`data/`", md)
    return md


def split_lesson(md: str):
    md = rewrite_links(md)
    # drop the trailing "**Next:**" navigation lines - the app has its own
    md = re.sub(r"^\*\*Next:\*\*.*$", "", md, flags=re.M)
    md = re.sub(r"^\*\*Checkpoint:\*\*(.*)$", r"> **Checkpoint:**\1", md, flags=re.M)
    lines = md.strip().splitlines()
    title_line = lines[0]
    m = re.match(r"# Module A?\d\d: (.*)", title_line)
    title = m.group(1).strip() if m else title_line.lstrip("# ")
    chunks, current, current_title = [], [], None
    intro = []
    for line in lines[1:]:
        if line.startswith("## "):
            if current_title is None:
                intro = current
            else:
                chunks.append({"title": current_title, "md": "\n".join(current).strip().strip("-").strip()})
            current_title = re.sub(r"^\d+\.\s*", "", line[3:].strip())
            current = []
        else:
            current.append(line)
    if current_title is not None:
        chunks.append({"title": current_title, "md": "\n".join(current).strip().strip("-").strip()})
    intro_md = "\n".join(intro).strip().strip("-").strip()
    goal = re.search(r"\*\*Goal:\*\*\s*(.*?)\s*(?=\n\*\*Time:|\Z)", intro_md, re.S)
    time = re.search(r"\*\*Time:\*\*\s*(.*)", intro_md)
    rest = re.sub(r"\*\*Goal:\*\*.*?(?=\n\*\*Time:|\Z)", "", intro_md, flags=re.S)
    rest = re.sub(r"\*\*Time:\*\*.*\n?", "", rest).strip()
    return {
        "title": title,
        "goal": " ".join(goal.group(1).split()) if goal else "",
        "time": time.group(1).strip() if time else "",
        "intro": rest,
        "sections": [c for c in chunks if c["md"]],
    }


def verify_outputs():
    """Run every predict-the-output question and make sure the stored answer is right."""
    problems = 0
    for mid, mod in M.items():
        for i, q in enumerate(mod["quiz"]):
            if q.get("type") != "output":
                continue
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                exec(q["code"], {"__name__": "__quiz__"})
            got = "\n".join(line.rstrip() for line in buf.getvalue().strip().splitlines())
            if got != q["answer"]:
                problems += 1
                print(f"  ✗ module {mid} quiz {i}: expected {q['answer']!r}, Python printed {got!r}")
    return problems


def gather():
    modules = []
    folders = [(track, f) for track, root in TRACK_ROOTS for f in sorted(root.iterdir()) if f.is_dir()]
    for track, folder in folders:
        mid = folder.name.split("_")[0]
        lesson = split_lesson((folder / "lesson.md").read_text(encoding="utf-8"))
        entry = {"id": mid, "slug": folder.name, "track": track, **lesson, "learn": M.get(mid, {})}
        cr = re.search(r"^\*\*Continue reading:\*\* \[([^\]]+)\]\((https?://[^)]+)\) \(([^)]+)\)\.\s*(.*)$",
                       (folder / "lesson.md").read_text(encoding="utf-8"), re.M)
        if cr:
            entry["read"] = {"title": cr.group(1), "url": cr.group(2), "source": cr.group(3), "why": cr.group(4).strip()}
        if (folder / "exercises.py").exists():
            entry["exercise"] = {
                "code": (folder / "exercises.py").read_text(encoding="utf-8"),
                "tests": (folder / "tests.py").read_text(encoding="utf-8"),
                "solution": (folder / "solutions.py").read_text(encoding="utf-8"),
            }
        support = {}
        for extra in folder.glob("*.py"):
            if extra.name not in ("exercises.py", "tests.py", "solutions.py"):
                support[extra.name] = extra.read_text(encoding="utf-8")
        data_dir = folder / "data"
        if data_dir.is_dir():
            for f in data_dir.iterdir():
                support["data/" + f.name] = f.read_text(encoding="utf-8")
        entry["support"] = support
        modules.append(entry)

    projects = []
    for p in sorted((ROOT / "projects").glob("*.md")):
        md = rewrite_links(p.read_text(encoding="utf-8"))
        md = re.sub(r"\[`?solutions/[^\]]*`?\]\([^)]*\)", "the `projects/solutions/` folder of the course repo", md)
        title = md.splitlines()[0].lstrip("# ").strip()
        is_ai = p.name.startswith("A_")
        projects.append({"n": "ai" if is_ai else str(int(p.name[1])), "track": "ai" if is_ai else "python",
                         "title": title, "md": md})

    cheatsheet = rewrite_links((ROOT / "cheatsheet.md").read_text(encoding="utf-8"))
    validate_path([m["id"] for m in modules], ["project-" + p["n"] for p in projects])
    return {"modules": modules, "projects": projects, "cheatsheet": cheatsheet, "parts": PARTS, "tracks": TRACKS,
            "path": PATH, "prereqs": PREREQS,
            "pyodideVersion": PYODIDE_VERSION}


def download_engine():
    target = DIST / "pyodide"
    target.mkdir(parents=True, exist_ok=True)
    for name in ENGINE_FILES:
        dest = target / name
        if dest.exists():
            continue
        url = f"https://cdn.jsdelivr.net/npm/pyodide@{PYODIDE_VERSION}/{name}"
        print(f"  downloading {name} …")
        urllib.request.urlretrieve(url, dest)
    # Hosts that refuse .zip get the standard library as base64 text instead.
    import base64
    (target / "python_stdlib.txt").write_bytes(base64.b64encode((target / "python_stdlib.zip").read_bytes()))


def build():
    print("Checking predict-the-output answers by running them…")
    bad = verify_outputs()
    if bad:
        sys.exit(f"{bad} quiz answer(s) are wrong - fix app/learning_content.py")
    print("  all answers verified ✓")

    data = gather()
    html = (APP / "template.html").read_text(encoding="utf-8")
    css = "\n".join((APP / "vendor" / f).read_text(encoding="utf-8")
                    for f in ["codemirror.css", "show-hint.css", "lint.css"]) + "\n" + (APP / "styles.css").read_text(encoding="utf-8")
    js = (APP / "app.js").read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = (html.replace("/*__CSS__*/", css)
                .replace("/*__DATA__*/", f"window.COURSE = {payload};")
                .replace("/*__APP__*/", js))
    DIST.mkdir(parents=True, exist_ok=True)
    # artifact.html: page content only (the claude.ai host adds the document skeleton)
    (DIST / "artifact.html").write_text(html, encoding="utf-8")
    # index.html / python-foundry.html: a complete document you can open straight from disk
    full = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            '<style>[hidden]{display:none!important}body{margin:0}img{max-width:100%}</style>\n'
            '</head>\n<body>\n' + html + '\n</body>\n</html>\n')
    (DIST / "index.html").write_text(full, encoding="utf-8")
    (ROOT / "python-foundry.html").write_text(full, encoding="utf-8")
    out = ROOT / "python-foundry.html"
    print(f"Wrote {out.relative_to(ROOT)} and app/dist/ ({out.stat().st_size // 1024} KB)")
    if "--engine" in sys.argv:
        download_engine()


if __name__ == "__main__":
    build()
