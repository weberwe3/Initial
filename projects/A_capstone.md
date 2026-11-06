# AI Track Capstone: Customer-Feedback Insights Pipeline

**After:** Module A12 · **Time:** 15–25 hours over 2–4 weeks

Build the project that proves you can take AI from idea to measured business
value: an AI pipeline that turns thousands of free-text comments into
decisions, evaluated properly and presented like an AI ambassador would.

It doubles as your strongest portfolio piece (Module A13) and as a template
you can reuse at work.

---

## The scenario

Your organisation collects customer feedback (surveys, reviews, support
tickets) but only reads a sample. Leadership wants to know **what customers
complain about most, how that's changing, and what to fix first.**

**Data:** use a public dataset of product reviews or support tickets, or
generate a realistic synthetic set. If you use work data, follow your
company's rules (A03) and anonymise it first.

---

## Deliverables

### 1. Label design (A08)
- [ ] Ask AI to propose themes from a random sample of ~200 comments
- [ ] Finalise 5–10 labels with one-line definitions, one example each, and "other"
- [ ] Note who would own each label in a real business

### 2. Gold set (A08)
- [ ] Hand-label 100–200 randomly sampled comments
- [ ] Record your labelling rules for tricky cases

### 3. Baseline (A08)
- [ ] Keyword-rules classifier; measure accuracy, precision and recall on the gold set

### 4. AI classifier (A07)
- [ ] Prompt with label definitions and examples; JSON output with an enum of labels
- [ ] Row loop with failure isolation, validation, retries and progress saving
- [ ] Cost estimate before the full run, and actual cost after
- [ ] Measure on the gold set; compare with the baseline; iterate at least twice on the prompt
- [ ] Optional: compare two models on accuracy *and* cost

### 5. Pipeline (A05–A06)
Pick one and justify your choice:
- [ ] **Alteryx-first:** input → clean → Python tool (API call) → summarise → output
- [ ] **Python-first:** a pandas script or notebook, with an Alteryx workflow for the
      downstream reporting

Print or log row counts at every step and reconcile them.

### 6. Insights (A04)
- [ ] Label distribution overall, by month and by one segment
- [ ] Top themes with three real example quotes each (selected by code)
- [ ] AI-drafted executive summary from your computed tables, edited by you,
      with no number that isn't in the tables

### 7. Governance note (A03)
- [ ] One page: data used, data classes, minimisation steps, approved tools,
      verification, human review, known limitations

### 8. Ambassador pack (A12)
- [ ] Value estimate: hours saved and coverage gained (from sample to 100%), with assumptions
- [ ] A 5-slide (or one-page) leadership update: headline, evidence, risks and controls, next step, ask
- [ ] A 15-minute demo script for your team

---

## Stretch goals

- **RAG add-on (A09):** let users ask questions of the comments ("What do customers
  say about the mobile app?") with cited examples.
- **Agent add-on (A10):** a read-only agent that answers trend questions by
  calling your summary functions, with every tool call logged.
- **MCP add-on (A11):** expose your summary tables through a small read-only MCP
  server (e.g. `get_theme_counts(month)`), and write a proposal for IT to host
  it for your team's approved models.
- **Skill add-on (A11):** package your monthly insights procedure as a Skill
  (`SKILL.md` + template + the script that computes the tables), and test that
  it triggers on realistic requests.
- **Monitoring:** compare each month's label distribution with the last and flag big shifts.
- **Segment fairness:** check accuracy by language, region or customer type.

---

## Self-review checklist

- [ ] Could a colleague rerun it from your README?
- [ ] Is every number traceable to code, not to AI prose?
- [ ] Did you report accuracy on the gold set honestly, including where it fails?
- [ ] Would your governance note satisfy your privacy or risk team?
- [ ] Does the leadership update lead with a business outcome, not a model name?

When you're done, add it to your portfolio with a short write-up: problem,
approach, evaluation, result, next steps. Then present it to your team.
That's what an AI ambassador does.
