"""Module A09 solutions."""

import math
import re

STOPWORDS = {"a", "an", "the", "is", "are", "of", "to", "and", "or", "in", "on", "for", "do", "i",
             "what", "how", "it", "be", "can", "my", "with", "at", "by", "this", "that", "any"}


def chunk_words(text, size, overlap=0):
    if overlap >= size:
        raise ValueError("overlap must be smaller than size")
    words = text.split()
    chunks, step = [], size - overlap
    for start in range(0, len(words), step):
        chunks.append(" ".join(words[start:start + size]))
        if start + size >= len(words):
            break
    return chunks


def tokenize(text):
    return [w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOPWORDS]


def vectorize(text):
    vec = {}
    for w in tokenize(text):
        vec[w] = vec.get(w, 0) + 1
    return vec


def cosine(a, b):
    if not a or not b:
        return 0.0
    dot = sum(v * b.get(w, 0) for w, v in a.items())
    norm = math.sqrt(sum(v * v for v in a.values())) * math.sqrt(sum(v * v for v in b.values()))
    return round(dot / norm, 4)


def retrieve(question, chunks, k=2):
    q = vectorize(question)
    scored = [(cosine(q, vectorize(c)), i) for i, c in enumerate(chunks)]
    scored = [s for s in scored if s[0] > 0]
    scored.sort(key=lambda s: -s[0])          # stable sort keeps original order on ties
    return [i for _, i in scored[:k]]


def grounded_prompt(question, sources):
    numbered = "\n".join(f"[{i}] {s}" for i, s in enumerate(sources, start=1))
    return ("Answer the question using ONLY the numbered sources below. Cite sources like [1].\n"
            "If the sources don't contain the answer, say you couldn't find it.\n\n"
            f"<sources>\n{numbered}\n</sources>\n\n"
            f"Question: {question}")


def citations(answer):
    return sorted({int(n) for n in re.findall(r"\[(\d+)\]", answer)})


def unsupported_citations(answer, n_sources):
    return [n for n in citations(answer) if n < 1 or n > n_sources]
