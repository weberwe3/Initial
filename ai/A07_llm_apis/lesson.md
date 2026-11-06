# Module A07: Calling AI from Python

**Goal:** call an LLM from Python, get structured answers back, and run AI over every row of a dataset reliably, safely and within budget.
**Time:** 4 hours.

Chat is great for one task at a time. The API is how AI becomes part of a
**workflow**: classifying 5,000 survey comments, extracting fields from
invoices, or summarising every ticket, the same way, every time.

> The API examples below run **on your computer** (they need an API key and
> internet access). The exercises run right here: they use a *fake* model so
> you can practise the surrounding code (the part that makes AI workflows
> reliable) without an account.

---

## 1. Setup (on your computer)

```bash
pip install anthropic
```

API access needs a key from your provider's console, or your company's
approved gateway. **Never paste keys into code or chats.** Store them in an
environment variable:

```bash
# macOS / Linux
export ANTHROPIC_API_KEY="..."
# Windows PowerShell
$env:ANTHROPIC_API_KEY="..."
```

Many companies route AI through Azure, AWS Bedrock or Google Vertex instead
of a vendor directly. The code looks almost identical; ask your platform
team which is approved.

---

## 2. Your first API call

```python
import anthropic

client = anthropic.Anthropic()          # reads ANTHROPIC_API_KEY from the environment

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1000,
    system="You are a concise assistant for a retail analytics team.",
    messages=[{"role": "user", "content": "Give 3 reasons repeat purchases might fall."}],
)

for block in response.content:
    if block.type == "text":
        print(block.text)

print(response.usage.input_tokens, response.usage.output_tokens)
```

The pieces:
- **`model`:** which model. Larger models are more capable and more expensive;
  smaller ones are cheaper and faster. Test on your task before choosing.
- **`system`:** standing instructions (role, rules, format).
- **`messages`:** the conversation. The API remembers nothing between calls;
  you send the history each time.
- **`max_tokens`:** a ceiling on the answer length.
- **`response.content`:** a list of blocks. Read the `text` blocks.
- **`response.usage`:** tokens used, which you multiply by price for cost (A00).

---

## 3. Structured output: JSON you can trust

For workflows you want **data**, not prose. Current APIs can constrain the
answer to a JSON schema you define:

```python
import json
import anthropic

client = anthropic.Anthropic()
schema = {
    "type": "object",
    "properties": {
        "sentiment": {"type": "string", "enum": ["positive", "neutral", "negative"]},
        "topic": {"type": "string", "enum": ["price", "quality", "delivery", "service", "other"]},
        "summary": {"type": "string"},
    },
    "required": ["sentiment", "topic", "summary"],
    "additionalProperties": False,
}

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1000,
    messages=[{"role": "user", "content": "Classify this review: 'Arrived two weeks late and the box was crushed.'"}],
    output_config={"format": {"type": "json_schema", "schema": schema}},
)
text = next(b.text for b in response.content if b.type == "text")
print(json.loads(text))
```

**Enums (fixed label lists)** are the secret to consistent classification:
the model can't invent a new category spelling. Without schema support (older
tools, some gateways), ask for JSON in the prompt and **parse defensively**.
You'll write that parser in the exercises.

---

## 4. AI over every row: the core workflow pattern

```python
def classify(comment):
    response = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=300,
        system="Classify customer comments. Labels: price, quality, delivery, service, other.",
        messages=[{"role": "user", "content": f"<comment>{comment}</comment>"}],
        output_config={"format": {"type": "json_schema", "schema": schema}},
    )
    return json.loads(next(b.text for b in response.content if b.type == "text"))

results = []
for row in rows:                                 # rows: list of dicts from your CSV
    try:
        result = classify(row["comment"])
        results.append({**row, **result, "status": "ok"})
    except Exception as e:                       # never let one bad row kill the run
        results.append({**row, "status": f"error: {e}"})
```

Rules for production-grade row loops:

1. **Isolate failures:** one bad row shouldn't stop 4,999 good ones; record errors.
2. **Retry transient errors:** rate limits and timeouts happen; back off and retry
   (the official SDKs already retry some errors automatically).
3. **Validate every answer:** check required fields and allowed labels.
4. **Save progress:** write results as you go so a crash doesn't lose the run.
5. **Estimate cost first:** rows × tokens × price (A00), then run a 50-row pilot.
6. **Keep the raw response:** for auditing and debugging.

For big, non-urgent jobs, providers offer **batch APIs**: submit thousands of
requests, collect results later, at a significant discount.

---

## 5. Testable design: inject the model

The exercises use a pattern worth adopting in real code: pass the model call
in as a function.

```python
def classify_rows(rows, text_field, call_model):
    ...
    label = call_model(row[text_field])
```

In production, `call_model` calls the API. In tests, it's a fake that returns
canned answers. Your loop, retry, validation and cost logic gets tested
instantly and for free. This is how professional AI applications are built.

---

## 6. Cost and model choice

| Lever | Effect |
|-------|--------|
| Shorter prompts and answers | Directly fewer tokens |
| Smaller model for simple tasks | Often far cheaper; test quality first (A08) |
| Prompt caching | Reusing a long, unchanging prefix (instructions, examples) is billed at a fraction of the price on many APIs |
| Batch API | Discounted asynchronous processing |
| Don't send what you don't need | Data minimisation saves money *and* risk |

Choosing a model is an **evaluation question, not a guess**: run your top two
candidates on the same 100 labelled rows and compare accuracy and cost (A08).

---

## 7. Where to run it in an Alteryx shop

- **Python tool in Alteryx:** call the API per row inside your existing workflow.
- **A standalone script** scheduled on a server, writing results back to a database.
- **A notebook** for one-off analyses.

Whichever you choose: key in a secret store, data rules respected, logs kept.

---

## Key takeaways
- `messages.create(model, system, messages, max_tokens)` → read the text blocks and usage.
- Use JSON schemas with enums for consistent, machine-readable answers.
- Row loops: isolate failures, retry, validate, save progress, pilot first.
- Inject the model call so the rest of the workflow is testable for free.

**Continue reading:** [Get started with Claude](https://platform.claude.com/docs/en/get-started) (Anthropic's Claude documentation). Set up an API key and make your first calls, with links to structured outputs, batch processing and prompt caching.

**Next:** [Module A08: AI text analytics & evaluation](../A08_text_analytics_evals/lesson.md)
