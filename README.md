# Python: Zero to Intermediate

A hands-on course that takes you from **never having written code** to
**writing real, useful Python programs**: scripts that automate boring work,
handle files and data, talk to web APIs, and come with their own tests.

No prior experience assumed. No math beyond arithmetic. You need a computer and
roughly **4–6 hours a week**. At that pace the course takes about **12 weeks**.

---

## ✨ The interactive version (recommended)

Open **`python-foundry.html`** in your browser (double-click it). You get the
whole course as an app with real Python running in the page. Nothing to install.

- **Six-stage loop per module:** guess first → short lesson steps with runnable
  examples → Parsons puzzle → coding exercises with instant checks → recall quiz
  → explain it in your own words.
- **Spaced-repetition review** that brings cards back on an expanding schedule
  (1, 3, 7, 16, 35… days) and mixes topics together.
- **Predict-before-you-run** mode, confidence ratings and a calibration chart,
  memory-strength bars, a study plan, a notebook, and a playground.
- **Search everything** (press `/` or Ctrl+K): lessons, flashcards, quiz
  questions, exercises, cheatsheet and projects.
- The **"How it's designed"** page explains the memory research behind each feature.

Progress is saved in your browser. The app is generated from the same
`modules/` folder as the terminal course: run `python app/build.py` after
editing a lesson. It needs an internet connection the first time, to download
Python into the page.

---

## How this course works

Each module is a folder in `modules/` with three files you'll use:

| File | What it's for |
|------|---------------|
| `lesson.md` | Read this first. Short explanations, lots of examples, "try it" prompts. |
| `exercises.py` | Your work. Fill in each function where it says `# TODO`. |
| `solutions.py` | Worked answers. **Only open these after a real attempt.** |

You never have to guess whether your answer is right. From the top folder of
the course, run:

```bash
python check.py        # your progress across the whole course
python check.py 4      # check your answers for module 04
```

You'll see a ✓ for each exercise that works, a ✗ with a hint for each that
doesn't, and `…` for ones you haven't started yet.

### The learning loop (this is the important part)

1. **Read** the lesson and type the examples yourself. Don't copy-paste:
   typing is how your fingers and brain learn the syntax.
2. **Predict, then run.** Before you run something, guess what it will print.
   Wrong guesses are where the learning happens.
3. **Do the exercises**, then run `python check.py N`.
4. **Stuck for more than 20 minutes?** Re-read the lesson section, add `print()`
   calls to see what's going on (Module 08 teaches this properly), then peek at
   *one line* of the solution, not the whole thing.
5. **Do the checkpoint project.** Projects are where it all clicks.

---

## The roadmap

### Part 1: Foundations (weeks 1–4)
| # | Module | You'll be able to… |
|---|--------|--------------------|
| 00 | [Setup](modules/00_setup/lesson.md) | Install Python and an editor, run your first program |
| 01 | [First steps](modules/01_first_steps/lesson.md) | Print, store values in variables, do arithmetic |
| 02 | [Strings](modules/02_strings/lesson.md) | Work with text: slice, search, format with f-strings |
| 03 | [Decisions](modules/03_decisions/lesson.md) | Make your program choose with `if` / `elif` / `else` |
| 04 | [Loops](modules/04_loops/lesson.md) | Repeat work with `for` and `while` |
| 05 | [Lists & tuples](modules/05_lists/lesson.md) | Store and process collections of things |
| 06 | [Dictionaries & sets](modules/06_dicts_sets/lesson.md) | Look things up by name, count, de-duplicate |

**Checkpoint project 1:** [Number-guessing game + tip calculator](projects/01_first_programs.md)

### Part 2: Writing real programs (weeks 5–8)
| # | Module | You'll be able to… |
|---|--------|--------------------|
| 07 | [Functions](modules/07_functions/lesson.md) | Break problems into reusable, named pieces |
| 08 | [Errors & debugging](modules/08_errors_debugging/lesson.md) | Read tracebacks, fix bugs, handle errors gracefully |
| 09 | [Files & data](modules/09_files_data/lesson.md) | Read and write text, CSV and JSON files |
| 10 | [Modules, packages & pip](modules/10_modules_packages/lesson.md) | Use the standard library and install packages safely |

**Checkpoint project 2:** [Personal expense tracker (CLI)](projects/02_expense_tracker.md)

### Part 3: Intermediate Python (weeks 9–12)
| # | Module | You'll be able to… |
|---|--------|--------------------|
| 11 | [Pythonic code](modules/11_pythonic_code/lesson.md) | Comprehensions, `sorted` with keys, `zip`, `enumerate`, lambdas |
| 12 | [Classes & objects](modules/12_classes/lesson.md) | Model things with classes and dataclasses |
| 13 | [Testing](modules/13_testing/lesson.md) | Prove your code works with `pytest` |
| 14 | [Working with the web](modules/14_web_apis/lesson.md) | Call web APIs, handle JSON responses |
| 15 | [Intermediate power tools](modules/15_power_tools/lesson.md) | Generators, decorators, context managers, type hints |

**Capstone:** [Build your own tool](projects/03_capstone.md). Pick the track
that matches what *you* want Python for (see below).

---

## Choose your track

The fundamentals are the same for everyone, but the capstone and the "stretch"
ideas are better when they're about something you care about. Pick one now and
keep it in mind as you go:

- **Automation / productivity:** rename and sort files, clean spreadsheets,
  generate reports, automate repetitive office tasks.
- **Data & analysis:** load CSVs, summarise numbers, find trends, make charts.
- **Web & APIs:** pull data from online services, build small bots and
  dashboards.
- **Games & creative:** text adventures, simulations, generative art.

Not sure? Pick **automation**. It pays off fastest in everyday life.

### Make it yours
Tell Claude about your job, hobbies, and what you'd love to automate, and ask
it to rewrite the exercise examples and the capstone ideas around your world
(your spreadsheets, your sport's stats, your side business...). The checker
and structure stay the same; only the examples change.

---

## What "intermediate" means at the end

When you finish, you will be able to:

- Write a 200–500 line program, split across multiple files, that someone else
  can read.
- Read and write CSV/JSON, work with folders of files, and call web APIs.
- Use virtual environments and install third-party packages.
- Design with functions and classes, and know when to use which.
- Write tests with `pytest` and debug with confidence.
- Read other people's Python code and the official docs without panicking.

After this, good next steps are a framework for your track: **pandas** (data),
**FastAPI/Flask** (web), **Playwright/openpyxl** (automation), or **pygame**
(games).

---

## Quick reference

- Python docs: <https://docs.python.org/3/>
- The cheatsheet for this course: [`cheatsheet.md`](cheatsheet.md)
- Stuck-on-an-error guide: [Module 08](modules/08_errors_debugging/lesson.md)
