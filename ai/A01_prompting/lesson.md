# Module A01: Prompting Fundamentals

**Goal:** write prompts that get useful, consistent, checkable results the first time, and know how to fix them when they don't.
**Time:** 3 hours.

Prompting is the most valuable AI skill you can teach your team, and the one
most people never learn properly. It isn't about magic phrases. It's about
**giving a capable newcomer everything they need to do the job well.**

---

## 1. The newcomer test

Before sending a prompt, ask: *if I handed this to a smart new hire on their
first day, could they do a great job with only this text?*

Weak:
```text
Summarize this data.
```

Strong:
```text
You're helping a retail operations team prepare for their Monday meeting.

Below is last week's store-level sales extract (CSV). Summarize it for the
regional director in 5 bullet points:
- overall trend vs. the prior week
- the 2 best and 2 worst stores, with the % change
- anything unusual that needs follow-up

Keep it under 120 words. Use plain language, no jargon. If the data has
problems (missing stores, odd values), say so instead of guessing.

<data>
...
</data>
```

The second prompt says **who it's for, what to do, what good looks like, and
what to do when unsure.** That's the whole game.

---

## 2. The five building blocks

| Block | Question it answers | Example |
|-------|---------------------|---------|
| **Role / context** | Who is this for, and what's the situation? | "You're supporting a finance team closing the month…" |
| **Task** | What exactly should be produced? | "Write 3 user stories with acceptance criteria" |
| **Inputs** | What material should it use? | The data, document, notes: clearly marked |
| **Format** | What shape should the answer take? | "A table with columns X, Y, Z" / "JSON" / "≤5 bullets" |
| **Examples** | What does a great answer look like? | One or two worked examples |

Add **constraints** (length, tone, what not to do) and an **escape hatch**
("if you're not sure, say so"). The escape hatch is the single cheapest way
to reduce made-up answers.

---

## 3. Separate instructions from data

When you paste data or documents, wrap them in clear markers so the model
never confuses *your instructions* with *the content*:

```text
Classify each customer comment below as Praise, Complaint, or Question.

<comments>
1. The new dashboard is so much faster!
2. Why can't I export to Excel anymore?
3. Third time this month the report failed.
</comments>
```

XML-style tags (`<data>`, `<comments>`, `<document>`) work well with modern
models and make prompts easy to template. This matters even more when you
later send *thousands* of rows through code (Module A07).

---

## 4. Examples beat adjectives ("few-shot" prompting)

"Write it in a concise, professional style" means different things to
different people, and models. Showing beats telling:

```text
Turn each raw note into a one-line action item.

Example:
Note: "Sam to check w/ finance re Q3 accruals before Fri??"
Action: Sam — confirm Q3 accruals with Finance — due Friday

Now do these:
...
```

One to three examples usually do it. Make them **varied** (so it doesn't copy
one too literally) and **representative** of the tricky cases.

---

## 5. Ask for structure you can use

If the output is going into Excel, Alteryx or code, ask for a format a
machine can read:

```text
Return ONLY a JSON array, one object per comment, with keys
"id" (number), "label" (Praise|Complaint|Question), "reason" (≤12 words).
```

Tables (Markdown or CSV) are great for humans; JSON is best for code. In
A07 you'll see APIs that *guarantee* valid JSON.

---

## 6. Let it think, then answer

For analysis, ask the model to work through the problem before concluding:

```text
First, list the factors that could explain the drop in conversion.
Then rank them by how well the data supports each one.
Finally, give your single most likely explanation and what data would confirm it.
```

Breaking a task into explicit steps improves reasoning on harder problems and
makes the answer easier to check. Many current models also "think" internally
before answering; you still get better results when you spell out the steps
that matter to *you*.

---

## 7. Iterate like an analyst

Prompting is iterative. When output is off, diagnose before rewriting:

| Symptom | Likely fix |
|---------|-----------|
| Generic, bland answer | Add context: audience, purpose, constraints |
| Wrong format | Show the exact format, or give an example |
| Invents facts or numbers | Provide the source material; add "only use the data provided; say if it's missing" |
| Inconsistent across runs | Tighter instructions, examples, fixed labels |
| Too long | Give a hard limit ("max 5 bullets, ≤15 words each") |
| Misses the point | State what *good* looks like and *why* you need it |

Keep a **prompt library**: prompts that worked, saved with a note on when to
use them. As an ambassador, a shared team library is one of the highest-value
things you can create (Module A11).

---

## 8. Templates: prompts as reusable assets

A prompt you use weekly should be a template with placeholders:

```python
template = """You're preparing a {audience} update.
Summarize the {metric} results below in {n} bullets.
<data>
{data}
</data>"""

prompt = template.format(audience="leadership", metric="churn", n=3, data="...")
print(prompt)
```

Templates make results consistent across the team and let you run the same
prompt over many inputs, the bridge from "chatting with AI" to "AI in a
workflow".

---

## Key takeaways
- Pass the newcomer test: role, task, inputs, format, examples, plus an "if unsure, say so".
- Wrap pasted data in tags; keep instructions separate.
- Show examples instead of piling on adjectives.
- Ask for structured output when it's going into a tool.
- Iterate by diagnosing the symptom; save winners in a prompt library.

**Continue reading:** [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) (Anthropic's Claude documentation). Clear, practical guidance on clarity, examples, XML tags, step-by-step reasoning and more, written by a model vendor and applicable to any assistant.

**Next:** [Module A02: AI tools at work](../A02_ai_tools_at_work/lesson.md)
