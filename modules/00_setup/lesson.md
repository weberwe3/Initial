# Module 00: Setup

**Goal:** get Python running on your computer and run your first program.
**Time:** 30–60 minutes.

---

## 1. What is programming, really?

A program is a list of instructions, written precisely enough that a computer
can follow them. Python is a *language* for writing those instructions, and it
was designed to be readable by humans first.

```python
print("Hello!")
```

That's a complete Python program. It tells the computer to show the text
`Hello!` on the screen.

Computers are fast but completely literal. They do exactly what you wrote, not
what you meant. Most of learning to program is learning to say what you mean
precisely. That's a skill, and it gets easier with practice.

---

## 2. Install Python

### Windows
1. Go to <https://www.python.org/downloads/> and download the latest Python 3.
2. Run the installer. **Tick "Add python.exe to PATH"** at the bottom of the
   first screen. This matters.
3. Click *Install Now*.

### macOS
1. Download the latest Python 3 from <https://www.python.org/downloads/>.
2. Run the `.pkg` installer.
3. On a Mac, the command is usually `python3` rather than `python`. Wherever
   this course says `python`, type `python3`.

### Linux
Python 3 is almost certainly installed already. Use `python3`.

### Check it worked
Open a **terminal** (Windows: search for "PowerShell"; Mac: search for
"Terminal") and type:

```bash
python --version
```

You should see something like `Python 3.13.1`. Any version 3.10 or newer is fine.

---

## 3. Install an editor: VS Code

You *could* write Python in Notepad, but a proper editor colours your code,
spots typos, and runs programs with one click.

1. Install **Visual Studio Code** from <https://code.visualstudio.com/>.
2. Open it, click the Extensions icon (four squares on the left), search for
   **Python** (by Microsoft), and install it.
3. **File → Open Folder…** and open this course folder.

---

## 4. Two ways to run Python

### a) The interactive prompt (REPL)
Type `python` in a terminal and press Enter. You'll see `>>>`. Python is now
waiting for one instruction at a time:

```
>>> 2 + 3
5
>>> print("hi")
hi
>>> exit()
```

Use the REPL to try small ideas quickly. It's a calculator that speaks Python.

### b) Running a file
Real programs live in files ending in `.py`. Create a file called `hello.py`
containing:

```python
print("Hello, world!")
print("I am learning Python.")
```

Run it from the terminal (in the same folder):

```bash
python hello.py
```

Or press the ▶ button in the top-right of VS Code.

---

## 5. Using the course checker

From the course's top folder:

```bash
python check.py
```

You'll see a progress table. Every module starts empty. Your job over the next
12 weeks is to fill it with green.

---

## 6. Habits that will save you hours

- **Save before you run.** VS Code shows a dot on the tab when a file is unsaved.
  Turn on *File → Auto Save*.
- **Read error messages from the bottom up.** The last line says what went
  wrong. Module 08 covers this properly.
- **Change one thing at a time**, then run it again.
- **Typing beats reading.** Type every example in this course yourself.
- **It's normal to feel slow.** Everyone does at first. You're learning a
  language *and* a new way of thinking at the same time.

---

## ✅ Checklist before Module 01

- [ ] `python --version` shows Python 3.10+
- [ ] VS Code is installed with the Python extension
- [ ] You ran `hello.py` and saw your message
- [ ] You ran `python check.py` and saw the progress table

There are no exercises for this module. Head to
[Module 01: First steps](../01_first_steps/lesson.md).

**Continue reading:** [How to Install Python on Your System](https://realpython.com/installing-python/) (Real Python). Step-by-step installs for Windows, macOS and Linux, plus how to fix a broken PATH.
