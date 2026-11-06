# Module A00: What AI Actually Is

**Goal:** understand what today's AI is, how large language models work, and what they're good and bad at, well enough to explain it to your team.
**Time:** 2–3 hours.

You don't need maths or code for this module. You need a clear mental model,
because every good decision about AI (which task to give it, how much to trust
the answer, what it will cost) comes from understanding what's happening
underneath.

---

## 1. Three things people mean by "AI"

| Term | What it is | Example you've seen |
|------|------------|---------------------|
| **Machine learning (ML)** | Software that learns patterns from historical data to make predictions | Churn models, demand forecasts, fraud scores, Alteryx's predictive tools |
| **Generative AI** | Models that *create* new content: text, images, code, audio | Drafting an email, generating a chart description |
| **Large language models (LLMs)** | The generative models behind chat assistants, trained on huge amounts of text | Claude, ChatGPT, Gemini, Microsoft Copilot |

Classic ML answers a narrow, predefined question ("will this customer churn?")
and needs labelled training data for that one question. LLMs are
**general-purpose**: one model can summarise, classify, translate, write SQL
and explain a chart, all directed by plain-language instructions.

As a business analyst you'll use both. This track focuses on LLMs because
that's where the change in day-to-day work is happening, but you'll see in
A08 that you evaluate an LLM classifier the same way you'd evaluate a
classic ML model.

---

## 2. How an LLM works in one paragraph

An LLM reads your text as **tokens** (chunks of words), then repeatedly
predicts **the most fitting next token**, adds it, and predicts again. That's
it. It learned which tokens tend to follow which by training on an enormous
amount of text, then was further trained by people to follow instructions and
be helpful and safe.

Everything follows from that:

- It's excellent at anything that looks like *language patterns*: writing,
  summarising, reformatting, explaining, translating, coding.
- It doesn't "look things up" unless it's connected to a search tool or your
  documents (Module A09). It generates what *sounds* right.
- The same question can get slightly different answers each time.

---

## 3. Tokens: the unit of everything

Models read, think, and charge in tokens, not words.

- A token is roughly **¾ of an English word** (about 4 characters).
- "Business analytics is fun" ≈ 5 tokens. A page of text ≈ 500–700 tokens.
- Numbers, code and non-English text usually take more tokens per character.

Two practical consequences:

1. **Cost.** API pricing is per million tokens, with output tokens costing
   several times more than input tokens. Long answers cost more than long
   questions.
2. **Context window.** Each model has a maximum number of tokens it can
   consider at once: your instructions, the documents you paste, the
   conversation so far, *and* its answer. Modern models handle hundreds of
   thousands of tokens or more, but bigger isn't free: more tokens means more
   cost and slower answers.

```python
# A rough rule of thumb you'll implement in the exercises
text = "Quarterly revenue grew 12% driven by the enterprise segment."
approx_tokens = len(text) / 4
print(round(approx_tokens))
```

For exact counts, providers offer token-counting tools. The ~4-characters
rule is for quick estimates and budgets.

---

## 4. What LLMs are great at (in a BA's job)

| Task | Why it works well |
|------|-------------------|
| Drafting requirements, user stories, emails, summaries | Pure language generation |
| Turning messy notes into structured tables | Reformatting is pattern-matching |
| Writing and explaining SQL, Excel formulas, regex, Python | Code is language with strict patterns |
| Explaining an unfamiliar workflow, dataset or document | Summarising and explaining |
| Classifying or tagging free text at scale (feedback, tickets) | Reading comprehension plus consistent labels |
| Brainstorming hypotheses, edge cases, test cases | Breadth of exposure |

## 5. What they're bad at, and why

| Weakness | Why it happens | What you do about it |
|----------|----------------|----------------------|
| **Hallucination:** confident, wrong facts or numbers | It generates plausible text, not verified facts | Ground it in your data/documents; verify numbers yourself |
| **Exact arithmetic over big data** | It predicts digits like words | Let *code* do the maths (AI writes the code, Python/Alteryx runs it) |
| **Knowing your business** | It's never seen your data, acronyms, or rules | Give context: definitions, examples, the actual data |
| **Recent events** | Training data has a cutoff | Use tools with web search, or provide the information |
| **Consistency across thousands of rows** | Some randomness in generation | Clear instructions, structured output, and evaluation (A08) |

The single most important habit: **AI drafts, you decide.** Treat output like
work from a fast, smart, new colleague who doesn't know your business and
sometimes bluffs.

---

## 6. Models, versions and vendors

- **Vendors** build model families: Anthropic (Claude), OpenAI (GPT),
  Google (Gemini), Meta (Llama), and others. Microsoft Copilot and many
  business tools are built on top of these.
- Families come in **sizes**: larger models are more capable and slower and
  cost more; smaller ones are fast and cheap, often good enough for simple
  classification.
- Models are replaced every few months. Build skills and processes that
  survive a model change: clear prompts, evaluation sets, and verification habits.

---

## 7. A mental model to share with your team

> An LLM is a very well-read assistant that has read most of the public
> internet but has never been inside our company. It writes fast and well,
> it's great at first drafts and explanations, and it will sometimes state
> things that aren't true with total confidence. Give it context, ask for
> structure, and check anything that matters.

You'll explain this many times as an AI ambassador. Make it yours.

---

## Key takeaways
- LLMs predict the next token; that explains both their power and their failure modes.
- Tokens drive cost and context limits: ~4 characters or ~¾ of a word each.
- Great at language, reformatting, code and explanation; weak at exact maths, your private facts, and guaranteed accuracy.
- Let code do the arithmetic and let you make the decisions.

**Continue reading:** [Large Language Models explained briefly](https://www.3blue1brown.com/lessons/mini-llm/) (3Blue1Brown). A short, beautifully animated explanation of how LLMs work, with no maths required, and the full transformer series if you want to go deeper.

**Next:** [Module A01: Prompting fundamentals](../A01_prompting/lesson.md)
