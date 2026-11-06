# Capstone: Build Your Own Tool

**After:** Module 15 · **Time:** 15–25 hours (2–3 weeks)

This is where you prove to yourself that you can program. You'll design and
build something real from scratch, for **your** track, and finish it properly:
with tests, a README, and code you'd be happy to show someone.

---

## The rules

Your project must include:

- [ ] **At least 3 modules** (files), organised as a package
- [ ] **At least one class or dataclass** that earns its place
- [ ] **Reading and/or writing files** (CSV, JSON, text) *or* calling a web API
- [ ] **Error handling**: bad input or a failed request shouldn't crash it
- [ ] **A command-line interface** (`argparse`) or an interactive menu
- [ ] **At least 10 pytest tests**, all passing
- [ ] **Type hints** on your function signatures
- [ ] **A `README.md`** explaining what it does, how to install it, and how to run it
- [ ] **A `requirements.txt`** if you use third-party packages
- [ ] Use at least one Module 15 tool (a generator, decorator, or context manager) where it genuinely helps

---

## Pick a project from your track

### 🛠 Automation / productivity
- **Downloads folder organiser**: sort files into folders by type/date, with a
  `--dry-run` mode, an undo log (JSON), and a config file for custom rules.
- **Spreadsheet cleaner**: take a messy CSV export (inconsistent dates, stray
  spaces, duplicates, mixed-case names) and produce a clean file plus a report
  of what changed. Stretch: read/write `.xlsx` with `openpyxl`.
- **Report generator**: combine several CSVs into a weekly summary, written
  out as a Markdown or HTML file you could email.
- **Bulk file renamer**: preview-then-apply renames using patterns
  (`IMG_2041.jpg` → `2026-11-06_holiday_001.jpg`).

### 📊 Data & analysis
- **Personal finance analyser**: extend Project 2 with trends over months,
  averages, the "where did my money go" top 10, and charts with `matplotlib`.
- **Habit / fitness tracker**: log entries, compute streaks and weekly
  averages, chart progress.
- **Dataset explorer**: download a public dataset (e.g. from data.gov or Kaggle),
  then write a tool that answers 5 interesting questions about it.

### 🌐 Web & APIs
- **Weather dashboard**: use Open-Meteo (no key needed) to show the
  forecast for saved cities, cache responses to disk, and warn about rain.
- **Price / stock watcher**: track values over time in a JSON or SQLite file
  and alert when they cross a threshold.
- **GitHub stats tool**: summarise a user's or organisation's repositories:
  languages, stars, recent activity.
- **News digest**: pull headlines from an RSS feed or API, de-duplicate, and
  write a daily digest file.

### 🎮 Games & creative
- **Text adventure engine**: rooms, items and puzzles loaded from a JSON file,
  so the *game* is data and the *engine* is code. Save/load games.
- **Card game** (blackjack, war...) with classes for `Card`, `Deck`, `Hand`,
  `Player`, plus a simple computer opponent.
- **Life simulation**: Conway's Game of Life or a predator/prey simulation in
  the terminal, with patterns loaded from files.
- **Quiz app**: questions from a JSON/CSV file, scoring, high-score table,
  spaced repetition for questions you got wrong.

Got your own idea? Even better. Use it, as long as it meets the rules above.
The best projects solve a problem you actually have.

---

## How to approach it

1. **Write a one-paragraph description** of what it does and who it's for.
2. **List the features**, then cut it down to a minimum version you could build
   in a weekend. Everything else goes on a "later" list.
3. **Sketch the structure**: which modules, which classes, which functions?
   Data in, data out. Keep printing in one place.
4. **Build the smallest end-to-end slice first.** For example, the organiser
   moves *one* file type correctly before you handle all of them.
5. **Write tests as you go**, not at the end.
6. **Commit to git regularly** (see below).
7. **Polish**: README, help text, error messages, remove dead code.
8. **Show someone.** Explaining your code is the final test of understanding it.

### Use git
```bash
git init
git add .
git commit -m "First working version"
```
Commit every time something works. It's an unlimited undo button, and a
GitHub profile with real projects is worth more than any certificate.

---

## Self-review checklist

Before you call it done, read your code as if someone else wrote it:

- [ ] Could a stranger run it using only the README?
- [ ] Are names clear? Would you know what `process(d)` does in six months?
- [ ] Is any function over ~30 lines? Can it be split?
- [ ] Is anything copy-pasted 3+ times? Make it a function.
- [ ] Does bad input give a helpful message instead of a traceback?
- [ ] Do all the tests pass? Do they test the boundaries?

---

## 🎓 After the capstone

You're an intermediate Python programmer. Where next depends on your track:

| Track | Next things to learn |
|-------|----------------------|
| Automation | `openpyxl`, `pandas`, `playwright` (browser automation), scheduling with cron / Task Scheduler |
| Data | `pandas`, `matplotlib`/`seaborn`, Jupyter notebooks, SQL basics, `polars` |
| Web | `FastAPI` or `Flask`, `SQLAlchemy`, HTML basics, deploying to a cloud host |
| Games | `pygame`, `arcade`, basic vector maths |
| Everyone | `git` & GitHub, SQL, reading open-source code, contributing a small fix to a project you use |

Keep building. The fastest way to improve now is one small project every couple of weeks.
