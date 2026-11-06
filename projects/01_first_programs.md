# Checkpoint Project 1: Your First Real Programs

**After:** Module 06 · **Time:** 3–5 hours

Exercises train individual skills; projects make you combine them. Build these
in a new folder, e.g. `my_projects/`, as complete programs you run with
`python guess.py`.

There's no checker for projects. You'll know it works because you can use it.
Reference solutions are in [`solutions/project1/`](solutions/project1/), but
try for real first.

---

## Part A: Number-guessing game

The computer picks a secret number between 1 and 100. The player guesses until
they get it, and the program says "too high" or "too low" each time.

```
I'm thinking of a number between 1 and 100.
Your guess: 50
Too high!
Your guess: 25
Too low!
Your guess: 37
🎉 Got it in 3 guesses!
```

### Requirements
1. Pick the secret with `import random` and `random.randint(1, 100)`.
2. Loop until the guess is right.
3. Count the guesses and report the total at the end.
4. If the player types something that isn't a number, say so and **don't** count it
   (hint: `.isdigit()`).

### Level up (pick any)
- Let the player choose a difficulty (1–10, 1–100, 1–1000).
- Limit the number of guesses and reveal the number if they lose.
- Ask "Play again? (y/n)" and keep a best score across rounds.
- Swap roles: **you** think of a number and the *computer* guesses (hint: halve the range each time).

---

## Part B: Bill splitter & tip calculator

```
Bill total: $86.40
Tip percentage (15/18/20 or custom): 18
How many people? 3

Subtotal:        $86.40
Tip (18%):       $15.55
Total:          $101.95
Each person pays: $33.98
```

### Requirements
1. Ask for the bill, tip percent, and number of people.
2. Print a neatly aligned summary using f-string formatting (`:>10.2f`).
3. Re-ask if any input is invalid (negative, zero people, not a number).

### Level up
- Let each person enter what they ordered (a list of item prices per person) and
  split the tip proportionally.
- Store everyone's name and share in a dict and print a per-person table.

---

## Part C: Word statistics

Ask the user to paste a paragraph. Report:

- Number of words and characters
- The 5 most common words (ignore case and punctuation)
- The longest word
- Average word length

Hint: to strip punctuation, loop over the characters and keep only
`ch.isalpha() or ch == " "`.

---

## What you're practising
`input`, type conversion, `while` loops, `if/elif/else`, string methods,
lists, dicts, and the counting pattern: all of Part 1 in one place.
