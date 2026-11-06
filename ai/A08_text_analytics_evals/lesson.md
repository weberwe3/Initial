# Module A08: AI Text Analytics & Evaluation

**Goal:** turn piles of free text (survey comments, tickets, reviews, call notes) into numbers a business can act on, and prove the AI's labels are accurate enough to trust.
**Time:** 4 hours.

Free text is the most under-used data in most companies because reading it
doesn't scale. LLMs change that. But "the AI labelled it" isn't good enough for
a decision; **"the AI's labels agree with experts 92% of the time on a 200-row
test set" is.** This module teaches both halves.

---

## 1. What you can do with text now

| Task | Example | Output |
|------|---------|--------|
| **Classification** | Tag each comment: price / quality / delivery / service | One label per row |
| **Sentiment** | Positive / neutral / negative, or a 1–5 score | Label or number |
| **Extraction** | Pull product, competitor, order ID, requested action | Fields (JSON) |
| **Summarisation** | One-line summary per ticket; theme summary per month | Text |
| **Theme discovery** | "What are customers complaining about that we don't track?" | A proposed label set |

A strong workflow combines them: *discover* themes on a sample, *agree* a
label set with the business, *classify* everything, *evaluate*, then *report*.

---

## 2. Designing a label set (the part people skip)

Labels are a business decision, not an AI decision.

1. Ask AI to propose themes from a **random sample** of ~200 comments.
2. Review with stakeholders: merge, split and rename into **5–10 labels** that
   map to owners and actions ("Delivery: late" → logistics team).
3. Write a **one-line definition and one example** per label.
4. Always include **"other"** (and "multiple"/"unclear" if needed), so the model
   isn't forced into a wrong label.

Those definitions go straight into your classification prompt, and they're
what your human reviewers use too.

---

## 3. Evaluation: how you know it works

### Build a "gold" set
Take a **random sample** (100–300 rows), have one or two people label it
carefully using the definitions, and resolve disagreements. This is your
answer key. Keep it fixed; you'll reuse it every time you change the prompt
or model.

### Measure
Run the AI on the gold set and compare:

| Metric | Question it answers |
|--------|---------------------|
| **Accuracy** | What fraction of labels are right overall? |
| **Precision** (per label) | When the AI says "delivery", how often is it really delivery? |
| **Recall** (per label) | Of all the real delivery comments, how many did the AI catch? |
| **Confusion matrix** | Which labels get mixed up with which? |

Accuracy alone can mislead: if 80% of comments are "other", a model that
always says "other" is 80% accurate and useless. Look at per-label precision
and recall, especially for the labels that drive decisions.

```python
gold = ["price", "delivery", "other", "delivery"]
pred = ["price", "other",    "other", "delivery"]
correct = sum(g == p for g, p in zip(gold, pred))
print(f"accuracy = {correct / len(gold):.0%}")
```

### Improve, then re-measure
Look at the **disagreements**: they tell you exactly what to fix. Common fixes:
clearer label definitions, an example of the confusing case, a new label, or a
better model. Change one thing at a time and re-run the same gold set. This
loop (prompt → measure → inspect errors → adjust) is the core skill of
professional AI work.

---

## 4. Baselines: is AI even needed?

Before reaching for an LLM, try a **keyword rules** baseline ("late", "delay",
"shipping" → delivery). Then compare on the gold set:

- If rules get 90%, maybe that's enough, and it's cheaper and fully explainable.
- If AI gets 93% vs rules' 60%, you've *quantified* the AI's value: a great
  ambassador story.

In Alteryx terms, the rules baseline is a Formula tool with `Contains()`;
you'll build it in Python in the exercises.

---

## 5. Human-in-the-loop at scale

Even good models make mistakes. Design for it:

- **Confidence routing:** ask the model for a confidence level, or use
  "unclear" as a label; route low-confidence rows to a person.
- **Spot checks:** review a small random sample every run (e.g. 2%).
- **Monitor drift:** if this month's label distribution suddenly shifts, check
  whether customers changed or the model / data did.

---

## 6. From labels to insight

Classification is the middle of the job, not the end:

```text
Labels per comment
   → counts and % by label, by month, by segment
   → change vs last period, statistical sanity check on small samples
   → 3 example quotes per top theme (real ones, picked by code)
   → a one-page summary: what changed, why it matters, recommended owner
```

AI can draft that summary too, from the computed tables, with the "don't add
numbers that aren't in the tables" rule from A04.

---

## Key takeaways
- Label sets are business decisions: definitions, examples, and an "other".
- Build a fixed gold set; measure accuracy *and* per-label precision/recall.
- Read the disagreements; change one thing; re-measure.
- Compare with a keyword baseline to prove the value of AI.

**Continue reading:** [Classification: accuracy, recall, precision, and related metrics](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall) (Google Machine Learning Crash Course). A clear, interactive explanation of the metrics you'll use to evaluate any classifier, AI or otherwise.

**Next:** [Module A09: Chat with your documents (RAG)](../A09_rag_documents/lesson.md)
