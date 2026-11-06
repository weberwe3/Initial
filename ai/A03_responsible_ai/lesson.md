# Module A03: Responsible AI & Data Governance

**Goal:** use AI safely with company data, recognise the main risks, and set guardrails your team can follow.
**Time:** 3 hours.

As an AI ambassador you're not just the person who knows the tricks. You're
the person people trust to tell them **what's safe**. This module makes you
that person.

---

## 1. The four risks to manage

| Risk | What goes wrong | Example |
|------|-----------------|---------|
| **Data exposure** | Confidential or personal data goes somewhere it shouldn't | Pasting a customer list into an unapproved chatbot |
| **Inaccuracy** | Wrong output is trusted and acted on | A hallucinated figure ends up in a board deck |
| **Bias & fairness** | Output treats groups unfairly | AI-screened CVs or credit decisions skewed by patterns in historic data |
| **Accountability gaps** | Nobody owns the decision or can explain it | "The AI decided" with no human review or record |

Each has a standard control: **approved tools and data minimisation**,
**verification**, **testing for bias plus human review**, and **clear ownership
and documentation**.

---

## 2. Know your data classes

Most companies classify data, something like:

| Class | Examples | Typical AI rule |
|-------|----------|-----------------|
| Public | Published reports, marketing copy | Any tool |
| Internal | Process docs, non-sensitive metrics | Approved tools |
| Confidential | Financials, strategy, contracts | Approved enterprise tools only |
| Restricted / personal | Customer PII, health, payment, HR data | Only specifically approved systems, often anonymised first |

Find your company's actual policy and the list of approved tools. If there isn't
one, helping create it is a high-value ambassador project.

### What "enterprise" plans usually add
Contractual commitments not to train on your data, retention controls, admin
management, single sign-on and audit logs. **Consumer and enterprise versions of
the same assistant can have very different data terms.** Check which one you're using.

---

## 3. Data minimisation: send less, get the same answer

You rarely need real personal data for AI to help. Before sharing:

1. **Remove columns you don't need.** Asking about a formula? Send headers and 3 fake rows.
2. **Redact identifiers:** names, emails, phone numbers, account numbers.
3. **Pseudonymise consistently:** replace each customer with `CUST_001`,
   `CUST_002`… so patterns survive but identities don't.
4. **Aggregate:** send monthly totals by region, not transaction-level rows.
5. **Describe instead of send:** a data profile (column names, types, ranges)
   is often enough for AI to write the analysis code you then run locally.

You'll build a redaction and pseudonymisation toolkit in the exercises.
Regex-based redaction is a helpful safety net, **not a guarantee**: it misses
things like names in free text. Combine it with judgement and approved tools.

```python
import re
text = "Contact jane.doe@example.com or 555-123-4567 about invoice 8812."
print(re.sub(r"[\w.+-]+@[\w-]+\.[\w.]+", "[EMAIL]", text))
```

---

## 4. Verification: trust, but verify

A simple rule your team can remember:

> **The more it matters, the more you check.**

| Stakes | Example | Check |
|--------|---------|-------|
| Low | Brainstorm, first draft of an email | Read it |
| Medium | Internal analysis, documentation | Spot-check facts, test the code |
| High | Numbers for leadership, customer-facing, legal, financial | Recompute independently; second reviewer; cite sources |

Practical techniques:
- Ask for **sources or the exact rows** behind a claim.
- Have AI **write code** that computes the number, then run it yourself.
- **Recompute key figures** in Alteryx or Python (Module A04 exercises).
- Ask a second, fresh chat to **critique** the first answer.

---

## 5. Bias and fairness

LLMs learn from human text and historic data, which contain biases. Risk is
highest when AI influences decisions about **people**: hiring, lending,
pricing, performance, eligibility.

- Don't use general assistants to make or rank decisions about individuals.
- When classifying text at scale, **check error rates by segment** (region,
  language, customer type). A model that's 95% accurate overall can be much
  worse for one group.
- Keep a human accountable for decisions, with the ability to override.

---

## 6. Regulation in one minute

Rules are evolving and vary by country and industry. Know that they exist:

- **Privacy laws** (e.g. GDPR in the EU, state laws in the US) apply to personal
  data whether or not AI is involved.
- **The EU AI Act** sorts AI uses into risk tiers, with the strictest duties for
  "high-risk" uses such as employment and credit decisions.
- **Industry rules** (finance, healthcare, insurance) often add model-risk and
  documentation requirements.
- Frameworks like the **NIST AI Risk Management Framework** give organisations a
  common structure: govern, map, measure, manage.

You don't need to be a lawyer. You need to know **when to involve** legal,
privacy and risk colleagues: early, whenever personal data or decisions about
people are involved.

---

## 7. A team guardrail card

A one-page card is one of the most useful things an ambassador can publish:

```text
✅ DO
- Use approved tools: [list]
- Remove or mask personal and confidential data before sharing
- Verify numbers and facts before they leave the team
- Say when content is AI-assisted where it matters
- Save good prompts to the team library

❌ DON'T
- Paste customer, employee, or financial details into unapproved tools
- Let AI make decisions about people
- Present AI output as verified without checking it
- Share credentials, API keys, or passwords with any AI tool

❓ ASK [ambassador / privacy contact] when unsure
```

---

## Key takeaways
- Four risks: data exposure, inaccuracy, bias, accountability gaps, each with a control.
- Know your data classes and approved tools; consumer and enterprise terms differ.
- Minimise data: drop, redact, pseudonymise, aggregate, or just describe it.
- The more it matters, the more you check. Keep humans accountable.

**Continue reading:** [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) (NIST). The widely used, vendor-neutral framework for governing AI risk, useful for structuring your team's guardrails and for speaking the same language as risk and compliance colleagues.

**Next:** [Module A04: AI-assisted data analysis](../A04_ai_assisted_analysis/lesson.md)
