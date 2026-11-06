# Module A02: AI Tools at Work

**Goal:** know the landscape of AI tools, choose the right one for a task, and build a repeatable set of AI-assisted workflows for business analysis.
**Time:** 2–3 hours, plus a week of deliberately using AI for real tasks.

The fastest way to become the person your team asks about AI is to be the
person who uses it well, every day, on real work. This module maps the tools
and gives you workflows to start with tomorrow.

---

## 1. The tool landscape (by job, not by brand)

Products change every few months; the *categories* are stable.

| Category | What it's for | Examples |
|----------|---------------|----------|
| **General chat assistants** | Thinking partner, writing, analysis of pasted or uploaded material | Claude, ChatGPT, Gemini, Microsoft Copilot |
| **Copilots inside your apps** | AI where you already work: email, docs, spreadsheets, BI | Microsoft 365 Copilot, Google Workspace AI, AI features in Tableau/Power BI |
| **AI in your analytics platform** | Explaining, documenting and building workflows | Alteryx's AI features (e.g. workflow summaries and an AI assistant; names and availability vary by version and licence) |
| **Coding assistants** | Writing, explaining and fixing code; running code for you | Claude Code, GitHub Copilot, assistants with a code-execution / "analysis" mode |
| **APIs** | Putting a model inside your own workflows and tools at scale | Anthropic, OpenAI, Google, Azure APIs (Module A07) |
| **Agents** | Multi-step work where the AI uses tools: search, files, apps | Agent features in assistants; custom agents (Module A10) |

**Your company's approved tools come first.** Before anything else, find out
which tools are licensed and approved for which data (Module A03). Using an
unapproved tool with company data is the fastest way to lose the trust an
ambassador needs.

---

## 2. Features that matter more than the brand

When comparing tools, look for:

- **File uploads:** analyse a CSV, PDF, or slide deck directly.
- **Code execution / data analysis:** the assistant writes *and runs* Python
  on your file, so the maths is done by code, not guessed.
- **Projects / custom instructions:** save context (team glossary, report
  standards) so you don't repeat it in every chat.
- **Connectors:** search your company's documents, email, tickets, or drive.
- **Web search:** for recent information, with sources.
- **Enterprise controls:** data retention, no training on your data, admin
  settings, audit logs. This is what makes a tool safe for work data.

---

## 3. Your setup: one desktop app, several models behind it

Many companies (including yours) give people a familiar chat app, such as a
ChatGPT desktop app, that routes to **several models behind the scenes**:
some **on-premises** (running on company servers, often open-weight models)
and a **limited set of cloud models**. That's a smart design for data control,
and it changes how a super user works.

| | On-prem models | Cloud models |
|---|----------------|--------------|
| **Data** | Usually stays inside the company network, so it's often approved for more sensitive data | Leaves the network under contract, so it's often restricted to lower data classes or specific use cases |
| **Capability** | Often smaller or older; good at summarising, drafting, reformatting, simple classification | Usually the most capable at complex reasoning, long documents, code, and tool use |
| **Context window** | Can be smaller, so long documents may need splitting | Usually large |
| **Features** | File analysis, code execution, web search or connectors may be unavailable or limited | More likely to support the full feature set |
| **Availability** | Generally available | Often quota-limited or approved per use case |

**How to work well in this setup:**
1. **Know the menu.** Find out exactly which models you can pick, which are
   on-prem vs cloud, and **which data each is approved for**. Write it down;
   your colleagues will want the same cheat sheet.
2. **Route by task and data.** Sensitive data → approved on-prem model.
   Hard reasoning on non-sensitive material → cloud model, if allowed.
   Everyday drafting → whichever is approved and fastest.
3. **Prompt smaller models more explicitly.** Shorter inputs, clearer
   numbered steps, an example of the output, one task per prompt (A01).
   What a frontier model infers, a smaller model may need spelled out.
4. **Benchmark your own top tasks.** Run your five most common prompts on each
   model and note quality. Re-test when IT adds or upgrades a model. That
   comparison table is a ready-made ambassador deliverable.
5. **Never move restricted content to a cloud model** by switching models
   mid-conversation. Start a new chat instead, and check whether the content is
   allowed there at all.
6. **Note which model produced what** for anything important, so results can
   be checked and reproduced.

---

## 4. Ten workflows for a business analyst

Start with these. Each one saves real time within a week.

| # | Workflow | Prompt starter |
|---|----------|----------------|
| 1 | **Requirements from notes** | "Turn these stakeholder interview notes into user stories with acceptance criteria. Flag contradictions and open questions." |
| 2 | **Meeting → actions** | "From this transcript, list decisions, action items (owner, due date), and unresolved questions." |
| 3 | **SQL / formula help** | "Write a SQL query for [goal]. Tables: [schema]. Explain each step, and list assumptions." |
| 4 | **Explain a workflow** | "Here is the XML / tool list of an Alteryx workflow. Explain what it does, step by step, for a non-technical reader." |
| 5 | **Data dictionary** | "From these column names and sample rows, draft a data dictionary: name, description, type, example, caveats." |
| 6 | **Exploratory analysis** | Upload a CSV to a code-execution tool: "Profile this dataset: missing values, outliers, distributions, notable patterns. Show the code you ran." |
| 7 | **Stakeholder writing** | "Rewrite this analysis for a VP: 5 sentences, lead with the decision needed, no jargon." |
| 8 | **Test cases** | "List edge cases and test cases for this business rule: [rule]." |
| 9 | **Regex and text cleanup** | "Write a regex that extracts order IDs like ORD-2024-00123 from free text. Give examples that should and shouldn't match." |
| 10 | **Rubber-duck reviewer** | "Here is my analysis plan. Act as a sceptical senior analyst: what's missing, what could mislead, what would you check first?" |

Notice the pattern: **context, task, format, and an invitation to flag problems.**
That's Module A01 in action.

---

## 5. Choosing the right tool for the task

```text
Is the data confidential or regulated?
├─ Yes → only approved enterprise tools; minimise and anonymise first (A03)
└─ No / approved
   ├─ Needs maths over a dataset? → code-execution / analysis mode, or Python/Alteryx
   ├─ Lives in your email/docs/sheets? → the in-app copilot
   ├─ Needs current information? → assistant with web search, check the sources
   ├─ Same task, hundreds of rows? → API in a workflow (A07)
   └─ Thinking, writing, explaining? → general assistant
```

---

## 6. Habits of AI super users

1. **Default to trying AI first** for any language-heavy task, then judge the result.
2. **Give context once:** keep a reusable "about my team" note (glossary,
   audience, standards) in a project or custom instructions.
3. **Ask for its reasoning or code** when numbers are involved, and check it.
4. **Iterate in the same conversation:** "shorter", "more formal", "now as a table".
5. **Start fresh for a new task.** Long, wandering chats get worse; context matters.
6. **Save what works** in your prompt library.
7. **Track time saved.** You'll need numbers to make the case for AI (A12).

---

## 7. Your one-week challenge

For five working days, use AI on at least **three real tasks a day**. For each, note:

- the task and the tool,
- minutes it would have taken vs. minutes it took,
- quality (better / same / worse) and what you had to fix.

At the end of the week you'll have your first evidence log, your first
prompt-library entries, and real stories to share with your team.

---

## Key takeaways
- Learn tools by category; brands change, jobs don't.
- Approved enterprise tools and data rules come before anything else.
- Code execution for maths, copilots for in-app work, APIs for scale.
- Build daily habits and an evidence log of time saved.

**Continue reading:** [One Useful Thing](https://www.oneusefulthing.org/) (Ethan Mollick, Wharton). The most practical, research-informed writing on using AI at work, with regular, concrete advice on what AI changes for knowledge workers and how organisations adopt it.

**Next:** [Module A03: Responsible AI & data governance](../A03_responsible_ai/lesson.md)
