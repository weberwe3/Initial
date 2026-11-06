# Module A10: Agents & Automation

**Goal:** understand how AI agents work (models using tools in a loop), when to use them instead of a simple workflow, and how to keep them safe.
**Time:** 3–4 hours.

"Agents" are the most hyped and most misunderstood part of AI. Strip away
the hype and an agent is simple: **a model that can call tools, look at the
results, and decide what to do next, in a loop, until the task is done.**

---

## 1. From chat to workflow to agent

| Level | Who decides the steps? | Example |
|-------|------------------------|---------|
| **Single call** | You (one step) | Classify this comment |
| **Workflow** | You, in code or Alteryx, with AI at some steps | For each ticket: classify → if "billing", extract the invoice ID → route |
| **Agent** | The model, choosing tools as it goes | "Find why March revenue in the West dropped and draft a summary" |

**Start with the simplest level that works.** Workflows are predictable, cheaper
and easier to test. Agents earn their place when the steps genuinely can't be
known in advance, and when mistakes can be caught and undone.

---

## 2. How tool use works

You describe tools to the model: a name, what it does, and its inputs.

```text
Tool: run_sql      — run a read-only SQL query on the sales warehouse. Input: {query}
Tool: get_metric   — fetch a KPI by name and month. Input: {name, month}
Tool: send_draft   — save an email draft for review (never sends). Input: {to, subject, body}
```

Then the loop:

```text
1. You send the task and the tool list.
2. The model replies either with an answer, OR a request: "call get_metric
   with {name: 'revenue', month: '2026-03'}".
3. YOUR code runs the tool and sends back the result.
4. Repeat until the model gives a final answer (or you hit a step limit).
```

The model never runs anything itself. **Your code does, so your code decides
what's allowed.** That's the foundation of agent safety. You'll build this
loop with a fake model in the exercises.

In the real API, a tool-calling loop looks like this (on your computer):

```python
import anthropic

client = anthropic.Anthropic()
tools = [{
    "name": "get_metric",
    "description": "Get a business KPI for a month. Returns a number.",
    "input_schema": {
        "type": "object",
        "properties": {"name": {"type": "string"}, "month": {"type": "string"}},
        "required": ["name", "month"],
    },
}]
messages = [{"role": "user", "content": "How did revenue change from Feb to Mar 2026?"}]

while True:
    response = client.messages.create(model="claude-opus-5-5", max_tokens=4000,
                                      tools=tools, messages=messages)
    if response.stop_reason != "tool_use":
        break
    messages.append({"role": "assistant", "content": response.content})
    results = []
    for block in response.content:
        if block.type == "tool_use":
            value = get_metric(**block.input)          # your own function
            results.append({"type": "tool_result", "tool_use_id": block.id, "content": str(value)})
    messages.append({"role": "user", "content": results})

print(next(b.text for b in response.content if b.type == "text"))
```

Official SDKs also include helpers that run this loop for you.

---

## 3. Connecting tools: MCP

The **Model Context Protocol (MCP)** is an open standard for connecting AI
assistants to tools and data sources (databases, file stores, ticketing systems,
SaaS apps) without custom glue for each assistant. When an assistant offers
"connectors" or "integrations", MCP is often what's underneath. For an
ambassador: it means one approved connector to, say, your data warehouse can
serve several AI tools, with access controls in one place.

---

## 4. Coding agents

Coding assistants that can read files, run commands and edit code (Claude Code,
GitHub Copilot's agent features, and others) are the most mature agents today.
For an analyst they can:

- turn an Alteryx workflow description into a tested Python script,
- write and run data-quality checks on a folder of files,
- build a small internal tool or dashboard,
- explain an unfamiliar codebase or SQL repository.

Use them in a project folder, review every change, and keep work under version
control (git) so anything can be undone.

---

## 5. Guardrails for agents

| Guardrail | How |
|-----------|-----|
| **Least privilege** | Read-only database users; tools that *draft* rather than *send* |
| **Approval gates** | Risky tools (send, delete, pay, write to production) need a human "yes" |
| **Step and cost limits** | Stop after N steps or $X |
| **Validate tool inputs** | Check arguments before running anything |
| **Log everything** | Every tool call and result, for audit and debugging |
| **Sandbox** | Test environments, copies of data |
| **Treat external content as untrusted** | Text from web pages, emails or documents can contain instructions ("ignore previous instructions…"), known as *prompt injection*. Never let tool output alone authorise an action |

---

## 6. Automation patterns in an Alteryx shop

| Pattern | Shape |
|---------|-------|
| **AI step in a scheduled workflow** | Alteryx workflow → Python tool calls the API per row → results to a table → dashboard |
| **Triage agent** | New tickets/emails → classify → extract → route, with confidence thresholds and human review |
| **Analyst co-pilot** | Agent with read-only SQL and metric tools answers ad-hoc questions with the queries it used, so results are checkable |
| **Report drafter** | Workflow computes the numbers → AI drafts the narrative → analyst edits and approves |

Notice that in every pattern **numbers come from code and a person approves
anything that leaves the team.**

---

## Key takeaways
- An agent = model + tools + loop; your code executes the tools and sets the rules.
- Prefer single calls and workflows; use agents when the steps can't be known ahead.
- MCP standardises connecting tools and data to AI assistants.
- Guardrails: least privilege, approval gates, limits, validation, logging, and distrust of injected instructions.

**Continue reading:** [Building effective AI agents](https://www.anthropic.com/research/building-effective-agents) (Anthropic). A practical, hype-free guide to agent and workflow patterns (prompt chaining, routing, orchestrator-workers, evaluator loops) and when each is worth the complexity.

**Next:** [Module A11: The AI ambassador playbook](../A11_ambassador_playbook/lesson.md)
