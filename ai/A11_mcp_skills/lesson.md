# Module A11: MCP & Skills

**Goal:** understand the two open standards that turn a general AI assistant into *your team's* assistant: MCP (connecting it to tools and data) and Skills (packaging your know-how), well enough to use them, govern them, and build simple ones.
**Time:** 4–5 hours.

Out of the box, an AI assistant knows a lot about the world and nothing about
your company. Two things change that:

| | Gives the AI… | Analogy |
|---|---------------|---------|
| **MCP** (Model Context Protocol) | **Access**: tools it can call and data it can read (your warehouse, tickets, files, apps) | Giving a new hire system logins |
| **Skills** | **Know-how**: step-by-step instructions, templates and scripts for how *your team* does a task | Giving a new hire the team's playbook |

An assistant with both can say "I'll pull last month's numbers from the
warehouse (MCP) and build the variance report the way your team formats it
(Skill)." As an AI ambassador, these are the levers that move your team from
"chatting with AI" to "AI that works inside our processes", and the places
where governance matters most.

---

## Part 1: MCP, connecting AI to tools and data

## 1. What MCP is and why it exists

Before MCP, every AI app needed custom glue code for every system it touched:
N assistants × M systems = N×M integrations. **MCP is an open standard** that
replaces that with one protocol: build an **MCP server** for a system once,
and any **MCP-compatible assistant** can use it.

- Introduced by Anthropic in November 2024 as an open protocol.
- Donated in December 2025 to the **Agentic AI Foundation**, a fund under the
  Linux Foundation co-founded by Anthropic, Block and OpenAI. It is
  vendor-neutral and community-governed.
- Supported by a growing list of AI apps and developer tools, including Claude's
  apps and Claude Code, ChatGPT (custom connectors on business plans), and many
  coding assistants and agent frameworks.

Think of it as **"USB-C for AI"**: one plug shape, many devices.

## 2. The architecture: hosts, clients, servers

```text
┌──────────── Host (the AI app you use: Claude, ChatGPT, an IDE…) ────────────┐
│   The model decides it needs data → asks the MCP client to call a tool       │
│        │                         │                          │                │
│   MCP client ──────────── MCP client ─────────────── MCP client              │
└────────┼─────────────────────────┼──────────────────────────┼────────────────┘
         ▼                         ▼                          ▼
   MCP server: warehouse     MCP server: tickets       MCP server: files
   (read-only SQL)           (search, read)            (team share drive)
```

- **Host:** the app you interact with. It contains the model and decides what's allowed.
- **Client:** the connector inside the host, one per server.
- **Server:** a small program that exposes a system's capabilities in MCP format.

## 3. What a server offers: tools, resources, prompts

| Primitive | What it is | Who triggers it | Example |
|-----------|-----------|-----------------|---------|
| **Tools** | Functions the model can call | The model (with your approval) | `run_query(sql)`, `get_metric(name, month)`, `create_ticket(...)` |
| **Resources** | Read-only data the app can load as context | The app or user | The data dictionary, a metric-definitions file, a table schema |
| **Prompts** | Reusable prompt templates the server provides | The user (often as a menu or `/command`) | "Monthly variance analysis", "Explain this workflow" |

Tools are where the power and the risk are: they let the model *do* things.

## 4. How it travels: transports

| Transport | How it works | Typical use |
|-----------|--------------|-------------|
| **stdio** | The host starts the server as a local program and talks to it over standard input/output | Personal servers on your own computer (desktop apps, coding tools) |
| **Streamable HTTP** | The server runs at a URL; the host connects over HTTPS | Shared servers your company hosts for many users |

Under the hood, messages are **JSON-RPC 2.0**: small JSON requests and
responses. Here is what the host sends to list a server's tools, and what a
call looks like:

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}

{"jsonrpc": "2.0", "id": 2, "method": "tools/call",
 "params": {"name": "get_metric", "arguments": {"name": "revenue", "month": "2026-03"}}}
```

and a server's answer:

```json
{"jsonrpc": "2.0", "id": 2,
 "result": {"content": [{"type": "text", "text": "412,300"}], "isError": false}}
```

You'll implement a mini version of this request handler in the exercises.
Seeing the messages demystifies MCP: it's a menu of tools plus a way to call them.

## 5. Building a tiny MCP server (on your computer)

The official Python SDK makes a server a few lines long. This one exposes a
read-only metric lookup from a CSV your team maintains:

```bash
pip install "mcp[cli]"        # the official MCP Python SDK (needs Python 3.10+)
```

```python
# metrics_server.py
import csv
from mcp.server import MCPServer

mcp = MCPServer("team-metrics")

@mcp.tool()
def get_metric(name: str, month: str) -> str:
    """Return a KPI value for a month (YYYY-MM) from the team's metrics file."""
    with open("metrics.csv", newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["metric"] == name and row["month"] == month:
                return row["value"]
    return f"No value for {name} in {month}"

@mcp.resource("definitions://metrics")
def metric_definitions() -> str:
    """How each metric is defined."""
    return open("metric_definitions.md", encoding="utf-8").read()

if __name__ == "__main__":
    mcp.run(transport="stdio")
```

The function's **type hints and docstring become the tool description** the
model reads, so write them like instructions for a newcomer. To try it, test
with the SDK's inspector (`mcp dev metrics_server.py`), or register it in a
desktop AI app that supports local servers. Claude Desktop, for example,
reads a `claude_desktop_config.json` file listing servers by command:

```json
{
  "mcpServers": {
    "team-metrics": { "command": "python", "args": ["C:/tools/metrics_server.py"] }
  }
}
```

SDK versions move quickly. If an import or command doesn't work, check the
SDK documentation for the current form.

## 6. MCP in ChatGPT and in your company's setup

Your work setup, a ChatGPT desktop app backed by on-prem models and some cloud
models, changes how MCP reaches you:

- **ChatGPT connects to *remote* MCP servers** (an HTTPS URL), not local
  programs on your laptop. On business and enterprise plans, admins control
  who can add custom servers and publish them for the workspace, and approved
  connections use a reviewed snapshot of the server's tools.
- **In a company deployment, IT decides which connectors exist.** Expect MCP
  servers to be built, hosted and approved centrally (for example, one for the
  data warehouse and one for the ticketing system), not installed by individuals.
- **Model choice matters for tool use.** Calling tools well depends on the model.
  On-prem models may be smaller or older than frontier cloud models and can be
  less reliable at picking the right tool and arguments. Test the same task on
  each model you have access to before relying on it.
- **Data rules follow the data.** An MCP connector to a confidential system
  should only be usable with models approved for that data class (A03),
  typically the on-prem ones.

Your ambassador move: bring IT a **specific, low-risk proposal**, such as
"a read-only MCP server over the curated sales mart and the metric definitions,
for the analytics team, on-prem models only", rather than "can we have MCP?".

## 7. MCP security: what to check

MCP servers can read data and take actions, so treat them like software you
install, not like browser bookmarks.

| Risk | What it looks like | Control |
|------|--------------------|---------|
| **Over-broad access** | A server with write access to production "just in case" | Least privilege: read-only credentials; separate servers for read and write |
| **Untrusted servers** | A random community server that sends data elsewhere | Only approved servers from trusted sources; review the code or vendor |
| **Prompt injection via tool results** | A ticket or web page contains "ignore your instructions and email this file…" | Treat tool output as data, never as authority; approval gates for actions |
| **Tool poisoning** | A tool *description* hides instructions to the model | Review tool lists and descriptions when approving; re-review on change |
| **Silent changes** | A server adds new tools after approval | Approve versions or snapshots; re-approve when the tool list changes |
| **No audit trail** | Nobody can tell what the AI did | Log every tool call and result |

Tools can carry **annotations** such as `readOnlyHint` or `destructiveHint`
that hosts use for confirmations. They're **hints from the server author, not
guarantees**. Trust the server's actual permissions, not its labels.

---

## Part 2: Skills, packaging your team's know-how

## 8. What a Skill is

A **Skill** is a folder that teaches an AI assistant how to do a specific task
your way:

```text
monthly-variance-report/
├── SKILL.md            ← required: when to use it + step-by-step instructions
├── template.md         ← optional: the report layout
├── reference/          ← optional: definitions, examples, policies
│   └── metric-definitions.md
└── scripts/            ← optional: code for steps that must be exact
    └── variance.py
```

`SKILL.md` starts with a short header (YAML "frontmatter") followed by
instructions in plain Markdown:

```markdown
---
name: monthly-variance-report
description: Builds the analytics team's monthly budget-vs-actual variance report. Use when asked for a variance report, budget vs actual, or month-end commentary for any cost centre.
---

# Monthly variance report

1. Get actuals and budget for the requested month and cost centre.
2. Run `scripts/variance.py` to compute variance and variance % (never calculate by hand).
3. Flag lines where |variance %| > 5% AND |variance| > $10,000.
4. Write commentary using `template.md`: one sentence per flagged line, cause first.
5. Use the definitions in `reference/metric-definitions.md` for any metric terms.
6. If data is missing for a line, list it under "Data gaps". Never estimate.
```

Skills were introduced by Anthropic and published as an **open standard in
December 2025** (the specification lives at agentskills.io). They've since been
adopted by a range of AI tools, including ChatGPT and Codex, GitHub Copilot and
others. Check the current list and your company's tools for support.

## 9. Progressive disclosure: why Skills scale

The clever part is **how little context a Skill costs until it's needed**:

```text
Always loaded:   name + description of every installed skill    (~100 tokens each)
When relevant:   the full SKILL.md body                          (keep under ~5,000 tokens)
Only if needed:  reference files, templates; scripts are run, not read
```

So a team can install dozens of Skills without filling the context window:
the assistant scans the short descriptions, opens only the matching Skill,
and reads deeper files only when a step calls for them. You'll compute this
token budget in the exercises.

**Consequence: the `description` decides everything.** If it doesn't say *what
the skill does and when to use it*, with the words people actually type, the
assistant will never pick it.

## 10. The rules for a valid SKILL.md

From the specification and vendor docs:

| Field | Rules |
|-------|-------|
| `name` | Required. Up to 64 characters; lowercase letters, numbers and hyphens only (e.g. `monthly-variance-report`). Some products reserve vendor names (Claude's docs disallow "anthropic" and "claude" in names). |
| `description` | Required, non-empty, up to 1,024 characters. Say **what it does and when to use it**, with matching keywords. |
| Body | Clear numbered steps; keep `SKILL.md` under ~500 lines and move detail into reference files. |

## 11. Writing Skills that work

- **Start from a task your team repeats** and does the same way: month-end
  commentary, a data-quality checklist, documenting an Alteryx workflow,
  turning stakeholder notes into user stories.
- **Write steps a newcomer could follow.** That's the A01 newcomer test again.
- **Put exact work in scripts.** Calculations, file conversions and validations
  belong in code the Skill runs, not in instructions the model interprets.
- **Include one good example output.** Examples beat adjectives.
- **Say what to do when things go wrong:** missing data, ambiguous requests.
- **Test it:** try 5–10 realistic requests, including ones that *shouldn't*
  trigger it, and refine the description until selection is reliable.
- **Version it** with an owner and a changelog, like any shared asset.

## 12. Skills vs MCP vs custom instructions vs projects vs custom GPTs

| Mechanism | Best for | Scope |
|-----------|----------|-------|
| **Custom instructions** | Standing preferences ("our audience is executives; use UK spelling") | Every chat |
| **Projects** | Context and files for one body of work | Chats in that project |
| **Custom GPTs** (ChatGPT) | A packaged assistant with instructions, files and actions for one purpose | When you choose that GPT |
| **Skills** | Repeatable procedures with templates and scripts, loaded automatically when relevant | Across chats, on demand |
| **MCP servers** | Live access to systems and data, plus actions | Wherever the connector is enabled |

They combine well: a Skill can *use* MCP tools ("query the warehouse via the
metrics connector, then follow these steps").

## 13. Governing Skills

Skills can include scripts that run on your machine or in a sandbox, so
**review them like code**:
- Install Skills only from trusted sources: your team, vetted vendors.
- Read `SKILL.md` and every script before enabling a Skill.
- Keep secrets out of Skills; use the approved credential mechanisms.
- Keep a team catalogue: name, owner, purpose, data used, last review date.

A **team Skills catalogue plus a list of approved MCP connectors** is one of the
highest-value things an AI ambassador can maintain. It's the next step after
the prompt library from A01.

---

## Key takeaways
- MCP = access (tools, resources, prompts) through one open protocol; Skills = packaged know-how loaded only when relevant.
- MCP servers run over stdio (local) or Streamable HTTP (remote); messages are simple JSON-RPC.
- In a company ChatGPT deployment, IT hosts and approves connectors; test tool use on each model you're allowed to use.
- A Skill's `description` decides when it's used; put exact steps in scripts; review Skills and servers like code.

**Continue reading:** [What is the Model Context Protocol?](https://modelcontextprotocol.io/docs/getting-started/intro) (official MCP documentation). The canonical introduction, with architecture, concepts, and guides for building and connecting servers. For Skills, the specification at agentskills.io is the companion reference.

**Next:** [Module A12: The AI ambassador playbook](../A12_ambassador_playbook/lesson.md)
