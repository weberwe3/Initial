# Module A04: AI-Assisted Data Analysis

**Goal:** use AI to speed up every stage of an analysis (framing, exploring, coding, explaining) while keeping the numbers trustworthy.
**Time:** 3–4 hours.

AI doesn't replace analysis. It removes the slow parts: blank-page framing,
syntax lookups, first-pass exploration, and write-ups. The skill is knowing
**which parts to hand over and how to check them.**

---

## 1. The analyst-in-the-loop pattern

```text
  You                         AI                          Code (Python/Alteryx)
  ─────────────────────────────────────────────────────────────────────────────
  Frame the question   ──►  Suggest hypotheses, metrics, pitfalls
  Describe the data    ──►  Propose an analysis plan + write the code
                                                     ──►  Run on the real data
  Check results        ◄──────────────────────────────────  Numbers you can trust
  Interpret            ──►  Draft the narrative, charts, exec summary
  Decide & sign off
```

The key move: **AI writes the analysis; code computes the numbers; you
verify and decide.** LLMs are unreliable calculators but excellent
programmers. Let each do what it's good at.

---

## 2. Stage by stage

### Framing
```text
I'm analysing why repeat-purchase rate fell from 34% to 29% this quarter
for our online store. Suggest 8 hypotheses across product, pricing,
customer mix, operations and measurement. For each: the data that would
test it and how I'd know it's the cause, not a coincidence.
```
Asking for "measurement" hypotheses catches the classic trap: the metric
changed because the *definition or tracking* changed.

### Describing data without sending it
You often don't need to share the rows. Send a **profile**:

```text
Columns: order_id (str), customer_id (str), order_date (date, 2024-01..2024-12),
region (4 values: North/South/East/West), channel (web/app/store),
revenue (float, 0–4,800, 2% missing), discount_pct (0–40).
~120k rows. One row per order.
```

With that, AI can write a complete analysis script you run locally on the real
data, so nothing sensitive leaves your machine. You'll build a profiler in the
exercises.

### Exploring
Upload non-sensitive data to an assistant with **code execution**, or ask for
code to run yourself:
```text
Write Python (pandas) to: check missing values and duplicates, summarise
revenue by region and channel, and flag outliers using the IQR method.
Comment each step so a new analyst could follow it.
```

### Explaining results
```text
Here are the summary tables. Write a 150-word summary for the
operations director: lead with the answer, give two supporting numbers,
one caveat, and a recommended next step. Don't add any number that isn't
in the tables.
```
That last sentence matters: it forbids inventing figures.

---

## 3. Verification techniques

| Technique | How |
|-----------|-----|
| **Recompute key numbers** | Totals, averages and growth rates in Python or Alteryx, never from the AI's prose |
| **Reconcile to a source of truth** | Does the total match the finance report / dashboard? |
| **Check row counts at each step** | Joins and filters silently drop or duplicate rows |
| **Read the code** | Ask "explain this line by line"; watch for wrong filters, joins and date ranges |
| **Sanity bounds** | Percentages between 0 and 100? Growth plausible? Units right? |
| **Second opinion** | A fresh chat critiques the analysis: "what could make this wrong?" |

In the exercises you'll write `verify_claim`, which checks an AI's stated
total against the real data within a tolerance: a tiny function with a big
habit behind it.

---

## 4. Common AI analysis mistakes to watch for

- **Averaging averages** (e.g. averaging regional conversion rates instead of
  recomputing from totals).
- **Simpson's paradox:** a trend that reverses when you split by segment.
- **Correlation stated as causation.**
- **Wrong date windows** or time zones.
- **Silently dropped rows** from missing values or join mismatches.
- **Confident precision:** "revenue grew 12.37%" from a rough eyeball.

When you spot one, add a line to your prompt template to prevent it next time.

---

## 5. Working with plain Python data (preview of A05)

Before pandas, it helps to see analysis as simple operations on rows. Each row
is a dict, like a record in an Alteryx stream:

```python
rows = [
    {"region": "North", "revenue": 120.0},
    {"region": "South", "revenue": 80.0},
    {"region": "North", "revenue": 50.0},
]
totals = {}
for r in rows:
    totals[r["region"]] = totals.get(r["region"], 0) + r["revenue"]
print(totals)   # {'North': 170.0, 'South': 80.0}
```

That's a Summarize tool, grouped by region, summing revenue: three lines of
Python.

---

## Key takeaways
- AI writes and explains; code computes; you verify and decide.
- Share a data profile instead of the data whenever you can.
- Forbid invented numbers ("only use figures in the tables").
- Recompute, reconcile, and check row counts: every time it matters.

**Continue reading:** [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) (Anthropic's Claude documentation). Concrete techniques for keeping AI answers grounded: letting the model say "I don't know", requiring quotes from source material, and verifying claims.

**Next:** [Module A05: From Alteryx to Python](../A05_alteryx_to_python/lesson.md)
