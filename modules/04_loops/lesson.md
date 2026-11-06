# Module 04: Loops

**Goal:** repeat work automatically with `for` and `while`.
**Time:** 3 hours.

Loops are where programming starts to save you real time. Doing something once
by hand is fine. Doing it 10,000 times is a job for a loop.

---

## 1. `for` loops: do something for each item

```python
for letter in "hey":
    print(letter)
# h
# e
# y
```

Read it as: "for each `letter` in `"hey"`, run the indented block". The
variable `letter` takes each value in turn.

### `range()`: counting
```python
for i in range(5):        # 0, 1, 2, 3, 4   (5 numbers, starting at 0)
    print(i)

range(1, 6)       # 1, 2, 3, 4, 5      start, stop (stop not included)
range(0, 20, 5)   # 0, 5, 10, 15       start, stop, step
range(10, 0, -1)  # 10, 9, ..., 1      counting down
```

---

## 2. The accumulator pattern

This is the most important loop pattern. Start with an empty/zero value, then
build it up inside the loop:

```python
total = 0
for n in range(1, 101):
    total += n
print(total)   # 5050
```

```python
shout = ""
for ch in "hello":
    shout += ch.upper() + "!"
print(shout)   # H!E!L!L!O!
```

```python
count = 0
for ch in "mississippi":
    if ch == "s":
        count += 1
print(count)   # 4
```

> Almost every "go through these and work out X" problem is: **set up a
> variable before the loop, update it inside, use it after.**

---

## 3. `while` loops: repeat until something changes

```python
countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Lift off!")
```

Use `while` when you **don't know in advance** how many times to repeat, like
"keep asking until the user types a valid answer".

```python
answer = ""
while answer != "yes":
    answer = input("Are we there yet? ").lower()
print("Finally!")
```

> ⚠️ If the condition never becomes false, the loop runs forever. Press
> **Ctrl+C** in the terminal to stop a runaway program.

---

## 4. `break` and `continue`

```python
# break: leave the loop immediately
for n in range(2, 100):
    if n % 7 == 0:
        print("First multiple of 7:", n)
        break

# continue: skip to the next round
for n in range(10):
    if n % 2 == 0:
        continue
    print(n)          # prints only odd numbers
```

The "loop forever until break" pattern is common for menus:

```python
while True:
    choice = input("(a)dd, (l)ist, (q)uit: ")
    if choice == "q":
        break
    print("You chose", choice)
```

---

## 5. Nested loops

A loop inside a loop. The inner loop runs completely for each round of the outer:

```python
for row in range(1, 4):
    line = ""
    for col in range(1, 4):
        line += f"{row * col:4}"
    print(line)
#    1   2   3
#    2   4   6
#    3   6   9
```

---

## 6. Real-world example: compound interest

```python
balance = 1000.0
rate = 0.05
years = 0
while balance < 2000:
    balance *= 1 + rate
    years += 1
print(f"Your money doubles after {years} years: ${balance:,.2f}")
```

---

## Key takeaways
- `for x in something:` goes through each item; `range()` produces numbers.
- **Accumulator pattern:** initialise before, update inside, use after.
- `while condition:` repeats until the condition is false.
- `break` leaves a loop; `continue` skips to the next round.

**Continue reading:** [Iterations](https://www.py4e.com/html3/05-iterations) (Python for Everybody, chapter 5). A gentle, free textbook chapter on loops and the counting, summing and max/min patterns.

**Next:** [Module 05: Lists & tuples](../05_lists/lesson.md)
