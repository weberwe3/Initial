# Python Foundry

Two hands-on learning tracks, built on the science of memory:

| Track | From → to | Length |
|-------|-----------|--------|
| **[Python](#the-roadmap)** | Never written code → writing real, tested Python programs | 16 modules, ~12 weeks |
| **[AI for business](#the-ai-track-zero-to-ai-super-user)** | No AI experience → AI super user and AI ambassador at work, including Python + AI for business analytics | 13 modules + capstone, ~10–12 weeks |

No prior experience assumed. You need a computer and roughly **4–6 hours a
week** per track. The tracks work on their own or side by side; the AI track's
Python-heavy modules (A05–A10) are easier after Python modules 00–09.

---

## ✨ The interactive version (recommended)

Open **`python-foundry.html`** in your browser (double-click it). You get the
whole course as an app with real Python running in the page. Nothing to install.

- **Two tracks:** switch between Python and AI for business at the top of the
  sidebar. Progress, reviews and search cover both.
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

## The AI track: zero to AI super user

Designed for analysts and AI ambassadors: from "what is an LLM?" to leading AI
adoption on a team, with the intersection of **Python and AI for business
analytics** at its core (including a module that maps Alteryx tools to Python).
Exercises run offline in the browser; code that needs an API key or pandas is
marked "run on your computer".

Check AI-track exercises with `python check.py A5` (module A05), and so on.

### Part 1: AI foundations
| # | Module | You'll be able to… |
|---|--------|--------------------|
| A00 | [What AI Actually Is](ai/A00_what_is_ai/lesson.md) | Understand what today's AI is, how large language models work, and what they're good and bad at, well enough to explain it to your team. |
| A01 | [Prompting Fundamentals](ai/A01_prompting/lesson.md) | Write prompts that get useful, consistent, checkable results the first time, and know how to fix them when they don't. |
| A02 | [AI Tools at Work](ai/A02_ai_tools_at_work/lesson.md) | Know the landscape of AI tools, choose the right one for a task, and build a repeatable set of AI-assisted workflows for business analysis. |
| A03 | [Responsible AI & Data Governance](ai/A03_responsible_ai/lesson.md) | Use AI safely with company data, recognise the main risks, and set guardrails your team can follow. |

### Part 2: AI + Python for business analytics
| # | Module | You'll be able to… |
|---|--------|--------------------|
| A04 | [AI-Assisted Data Analysis](ai/A04_ai_assisted_analysis/lesson.md) | Use AI to speed up every stage of an analysis (framing, exploring, coding, explaining) while keeping the numbers trustworthy. |
| A05 | [From Alteryx to Python](ai/A05_alteryx_to_python/lesson.md) | Translate the Alteryx tools you use every day into Python, so you can read, write and AI-generate Python with confidence, and combine both in one workflow. |
| A06 | [pandas for Business Analytics](ai/A06_pandas_analytics/lesson.md) | Do everyday analyst work in pandas (load, clean, reshape, summarise, chart and export) and know it well enough to check AI-written pandas code. |
| A07 | [Calling AI from Python](ai/A07_llm_apis/lesson.md) | Call an LLM from Python, get structured answers back, and run AI over every row of a dataset reliably, safely and within budget. |
| A08 | [AI Text Analytics & Evaluation](ai/A08_text_analytics_evals/lesson.md) | Turn piles of free text (survey comments, tickets, reviews, call notes) into numbers a business can act on, and prove the AI's labels are accurate enough to trust. |
| A09 | [Chat with Your Documents (RAG)](ai/A09_rag_documents/lesson.md) | Understand retrieval-augmented generation (how AI answers questions from your company's documents with citations) well enough to build a small version and evaluate vendor tools. |

### Part 3: AI super user & ambassador
| # | Module | You'll be able to… |
|---|--------|--------------------|
| A10 | [Agents & Automation](ai/A10_agents_automation/lesson.md) | Understand how AI agents work (models using tools in a loop), when to use them instead of a simple workflow, and how to keep them safe. |
| A11 | [The AI Ambassador Playbook](ai/A11_ambassador_playbook/lesson.md) | Lead AI adoption on your team: find and prioritise use cases, measure value, teach colleagues, manage risk, and communicate results to leadership. |
| A12 | [Your AI Career](ai/A12_ai_career/lesson.md) | Turn this curriculum into career capital: a clear target role, a portfolio that proves your skills, and a story that positions you for AI-related positions. |

**AI capstone:** [Customer-feedback insights pipeline](projects/A_capstone.md):
label design, a gold set, a baseline vs an AI classifier, an evaluated pipeline,
a governance note, and an ambassador pack for leadership.

### AI track reading list
| # | Module | Read next |
|---|--------|-----------|
| A00 | What AI Actually Is | [Large Language Models explained briefly](https://www.3blue1brown.com/lessons/mini-llm/) · 3Blue1Brown |
| A01 | Prompting Fundamentals | [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) · Anthropic's Claude documentation |
| A02 | AI Tools at Work | [One Useful Thing](https://www.oneusefulthing.org/) · Ethan Mollick, Wharton |
| A03 | Responsible AI & Data Governance | [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) · NIST |
| A04 | AI-Assisted Data Analysis | [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) · Anthropic's Claude documentation |
| A05 | From Alteryx to Python | [Python Tool](https://help.alteryx.com/current/en/designer/tools/developer/python-tool.html) · Alteryx Designer documentation |
| A06 | pandas for Business Analytics | [Python for Data Analysis, 3rd edition](https://wesmckinney.com/book/) · Wes McKinney, the creator of pandas |
| A07 | Calling AI from Python | [Get started with Claude](https://platform.claude.com/docs/en/get-started) · Anthropic's Claude documentation |
| A08 | AI Text Analytics & Evaluation | [Classification: accuracy, recall, precision, and related metrics](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall) · Google Machine Learning Crash Course |
| A09 | Chat with Your Documents (RAG) | [Contextual retrieval](https://www.anthropic.com/research/contextual-retrieval) · Anthropic |
| A10 | Agents & Automation | [Building effective AI agents](https://www.anthropic.com/research/building-effective-agents) · Anthropic |
| A11 | The AI Ambassador Playbook | [The State of AI](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) · McKinsey Global Survey |
| A12 | Your AI Career | [AI Engineer Roadmap](https://roadmap.sh/ai-engineer) · roadmap.sh |

---

## Continue reading (Python track)

One hand-picked, free resource per module for going deeper. The same link
appears at the end of each lesson.

| # | Module | Read next |
|---|--------|-----------|
| 00 | Setup | [How to Install Python on Your System](https://realpython.com/installing-python/) · Real Python |
| 01 | First Steps | [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html) · the official Python tutorial |
| 02 | Strings (Working with Text) | [Strings and Character Data in Python](https://realpython.com/python-strings/) · Real Python |
| 03 | Decisions | [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) · the official Python tutorial |
| 04 | Loops | [Iterations](https://www.py4e.com/html3/05-iterations) · Python for Everybody, chapter 5 |
| 05 | Lists & Tuples | [Data Structures](https://docs.python.org/3/tutorial/datastructures.html) · the official Python tutorial |
| 06 | Dictionaries & Sets | [Dictionaries in Python](https://realpython.com/python-dicts/) · Real Python |
| 07 | Functions | [Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/) · Real Python |
| 08 | Errors & Debugging | [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) · the official Python tutorial |
| 09 | Files & Data | [Reading and Writing Files](https://automatetheboringstuff.com/3e/chapter10.html) · Automate the Boring Stuff with Python, 3rd ed., chapter 10 |
| 10 | Modules, Packages & pip | [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html) · the official Python tutorial |
| 11 | Pythonic Code | [Python List Comprehension: Tutorial With Examples](https://realpython.com/list-comprehension-python/) · Real Python |
| 12 | Classes & Objects | [Classes](https://docs.python.org/3/tutorial/classes.html) · the official Python tutorial |
| 13 | Testing | [Get Started](https://docs.pytest.org/en/stable/getting-started.html) · the pytest documentation |
| 14 | Working with the Web | [Quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/) · the Requests documentation |
| 15 | Intermediate Power Tools | [Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/) · Real Python |

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
