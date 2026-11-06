# Module A12: The AI Ambassador Playbook

**Goal:** lead AI adoption on your team: find and prioritise use cases, measure value, teach colleagues, manage risk, and communicate results to leadership.
**Time:** 4 hours, then ongoing.

Being labelled an "AI ambassador" is an opportunity: you're being asked to
lead change, not just use tools. The people who do this well become the
natural candidates for AI-focused roles. This module is the playbook.

---

## 1. What a great ambassador actually does

| Role | In practice |
|------|-------------|
| **Practitioner** | Uses AI daily on real work; has stories and receipts |
| **Teacher** | Runs short demos, office hours, and pairs with colleagues |
| **Curator** | Maintains the team prompt library, guardrail card and tool guide |
| **Scout** | Finds and prioritises use cases; runs small pilots |
| **Translator** | Explains AI to leadership in business terms, and leadership's goals to the team |
| **Guardian** | Knows the policies; raises risks early; partners with IT, security, legal |

You don't need to be the most technical person. You need to be the most
**useful** person on AI for your team.

---

## 2. Finding use cases

Run a 45-minute **use-case workshop**:

1. Everyone lists tasks they do weekly that are **repetitive, text-heavy, or
   slow to start** (drafting, summarising, reformatting, searching, explaining).
2. For each: hours per week, number of people, how painful, and data sensitivity.
3. Cluster similar ideas; pick the top few to score.

Good first use cases share traits: **frequent, low-risk, easy to verify,
measurable**, e.g. meeting notes → action items, first drafts of recurring
reports, SQL/formula help, documenting Alteryx workflows, classifying
survey comments.

---

## 3. Prioritising: value × feasibility

Score each use case 1–5 on **value** (time saved, quality, revenue/risk impact)
and **feasibility** (data available and allowed, tool approved, easy to verify),
then place it on a 2×2:

```text
            Feasibility →
          low                 high
 high  ┌──────────────────┬──────────────────┐
 Value │ Strategic bet    │ QUICK WIN ✅     │
       │ (plan it)        │ (do it now)      │
       ├──────────────────┼──────────────────┤
  low  │ Avoid            │ Fill-in          │
       │                  │ (if time allows) │
       └──────────────────┴──────────────────┘
```

Start with **quick wins**: they build credibility and momentum. Subtract
points for risk (personal data, customer-facing output, decisions about
people). You'll code this scoring in the exercises.

---

## 4. Running a pilot

```text
Week 0  Define: task, baseline time/quality, success metric, guardrails
Week 1–3  3–6 volunteers use the approach; log time and issues
Week 4  Measure vs baseline; collect quotes; decide: scale, adjust, or stop
```

Write down the **baseline before you start** (how long it takes today, error
rate, turnaround). Without a baseline, there's no proof.

---

## 5. Measuring value

| Metric | How to get it |
|--------|---------------|
| **Time saved** | Before/after timings on real tasks; weekly self-report |
| **Adoption** | Active users ÷ licensed users; weekly active trend |
| **Quality** | Error rates, rework, reviewer scores, stakeholder feedback |
| **Speed** | Turnaround time for requests or reports |
| **Capability** | Analyses now possible that weren't (e.g. all 20k comments read, not a sample) |
| **Confidence** | Short survey: "How confident are you using AI for X?" (1–5), before and after training |

Translate to money carefully and conservatively:

> annual value ≈ hours saved per week × people × working weeks × loaded hourly cost

Then subtract tool costs. Present ranges, state assumptions, and prefer
**measured** savings over hoped-for savings. Leaders trust modest, evidenced
numbers more than big projections.

---

## 6. Teaching your team

What works:
- **15-minute "show, don't tell" demos** on a real team task, live.
- **Office hours:** a weekly slot to bring a task and solve it together.
- **Prompt library:** a shared doc or page of tested prompts, by task, with
  an example output and an owner.
- **Buddy pairing:** sit with someone for 30 minutes on their own work.
- **Celebrate wins:** share a "tip of the week" with a real time saving.

Meet people where they are. Sceptics often have valid concerns (accuracy,
job security, data). Acknowledge them, show the guardrails, and start with
tasks they dislike doing.

---

## 7. Talking to leadership

Leaders want to know: *What's the value? What's the risk? What do you need?*

```text
One-page AI update
1. Headline: "AI-assisted reporting saved the team ~14 hrs/week in the pilot."
2. Evidence: baseline vs pilot numbers, adoption, two quotes.
3. Risks & controls: data rules followed, verification steps, incidents (none).
4. Next: scale to 2 more teams; needs: licences for 12 people, 2 hrs/week of my time.
```

Speak in the language of **business outcomes** (cycle time, capacity,
quality, risk), not model names.

---

## 8. Governance partnership

Partner early with IT, security, data governance and legal. Bring them
**specific** use cases with data classes and controls, not vague enthusiasm.
Help write: approved-tools list, data rules, an intake form for new use cases,
and an incident path ("AI produced something wrong that got out: what do we do?").
Being the bridge between enthusiasts and risk owners is one of the most valued
ambassador skills.

---

## Key takeaways
- Practitioner, teacher, curator, scout, translator, guardian.
- Find use cases in workshops; prioritise by value × feasibility, minus risk; start with quick wins.
- Pilot with a baseline; measure time, adoption, quality, and confidence.
- Report modest, evidenced value to leadership with risks and asks.

**Continue reading:** [The State of AI](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) (McKinsey Global Survey). The annual survey of how organisations adopt AI and where they see value, useful benchmarks and language for making the business case to leadership.

**Next:** [Module A13: Your AI career](../A13_ai_career/lesson.md)
