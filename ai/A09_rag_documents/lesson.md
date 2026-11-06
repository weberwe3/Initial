# Module A09: Chat with Your Documents (RAG)

**Goal:** understand retrieval-augmented generation (how AI answers questions from your company's documents with citations) well enough to build a small version and evaluate vendor tools.
**Time:** 3–4 hours.

"Can we have a chatbot that knows our policies / reports / process docs?" is
one of the first requests every AI ambassador gets. The technique behind
almost all of them is **RAG: Retrieval-Augmented Generation.**

---

## 1. The problem RAG solves

LLMs don't know your internal documents, and pasting hundreds of documents
into every question is slow, expensive and often over the context limit. RAG
splits the job:

```text
            ┌───────────── once, ahead of time ─────────────┐
 Documents → split into chunks → index (keywords and/or embeddings)

            ┌───────────── every question ──────────────────┐
 Question → retrieve the most relevant chunks → prompt the LLM:
            "Answer using ONLY these sources, cite them" → answer + citations
```

The model writes the answer; **retrieval decides what it knows.** If the right
chunk isn't retrieved, even the best model can't answer correctly. So most
RAG quality problems are retrieval problems.

---

## 2. Chunking

Documents are split into passages of a few hundred words, usually with some
**overlap** so a sentence cut at a boundary still appears whole in one chunk.

- Too small: chunks lose context ("it" refers to what?).
- Too large: retrieval is fuzzy and prompts get expensive.
- Smart chunking follows structure (headings, sections, table rows) and keeps
  metadata (document name, section, date) for citations and filtering.

## 3. Retrieval: keywords and meaning

| Method | How it works | Good at |
|--------|--------------|---------|
| **Keyword search** (e.g. TF-IDF, BM25) | Matches words, weighting rare words more | Exact terms: product codes, policy names, error messages |
| **Semantic search** (embeddings) | Turns text into vectors of numbers where similar meanings sit close together | Paraphrases: "time off" finds "annual leave" |
| **Hybrid** | Combine both, then often re-rank | Most production systems |

Both compare a query vector with chunk vectors using **cosine similarity**:
how closely two vectors point in the same direction (1 = identical direction,
0 = unrelated). In the exercises you'll build keyword retrieval with word-count
vectors and cosine similarity, the same mechanics that semantic search uses,
just with simpler vectors.

```python
import math
a = {"refund": 2, "policy": 1}
b = {"refund": 1, "window": 1}
dot = sum(a[w] * b.get(w, 0) for w in a)
norm = math.sqrt(sum(v * v for v in a.values())) * math.sqrt(sum(v * v for v in b.values()))
print(round(dot / norm, 3))
```

---

## 4. The grounded prompt

Retrieval is only half; the prompt must keep the model honest:

```text
Answer the question using ONLY the numbered sources below.
Cite sources in square brackets, like [2], after each claim.
If the sources don't contain the answer, say "I couldn't find that in the
provided documents." Don't use outside knowledge.

<sources>
[1] (Travel Policy, §3) Economy class is required for flights under 6 hours…
[2] (Expenses FAQ) Receipts are required for any expense over $25…
</sources>

Question: Do I need a receipt for a $40 taxi?
```

Citations let users **verify**, and let you measure whether answers are
actually supported by the sources.

---

## 5. Evaluating a RAG system

Test it like any AI system (A08), with a set of real questions and known answers:

| Check | Question |
|-------|----------|
| **Retrieval hit rate** | Is the chunk containing the answer in the top k results? |
| **Faithfulness** | Is every claim supported by a cited source? |
| **Answer correctness** | Does it match the expected answer? |
| **Refusal when appropriate** | Does it say "not found" for questions the docs can't answer? |

Write 30–50 questions with your subject-matter experts, including a few
"trick" questions the documents *don't* answer.

---

## 6. Build vs buy

Many tools now offer "chat with your files": enterprise assistants with
connectors to SharePoint or Google Drive, BI tools with document Q&A, and
platform features in your cloud provider. As an ambassador, your job is
often to **evaluate** them, not build from scratch:

- Does it respect existing document **permissions**?
- Does it **cite sources** you can click?
- How does it handle tables, PDFs and scanned documents?
- Can you test it on **your** question set before buying?
- Where is the data stored and processed? (A03)

Building a small RAG yourself (this module's exercises) is what lets you ask
these questions with authority.

---

## Key takeaways
- RAG = retrieve relevant chunks, then answer from them with citations.
- Retrieval quality decides answer quality: chunk well, use hybrid search when you can.
- The grounded prompt: only these sources, cite them, say when it's not there.
- Evaluate with real questions, including ones the documents can't answer.

**Continue reading:** [Contextual retrieval](https://www.anthropic.com/research/contextual-retrieval) (Anthropic). A clear write-up of how RAG retrieval fails and how combining embeddings, keyword search and contextual chunking reduces failed retrievals dramatically.

**Next:** [Module A10: Agents & automation](../A10_agents_automation/lesson.md)
