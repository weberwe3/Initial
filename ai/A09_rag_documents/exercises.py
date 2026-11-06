"""
Module A09 exercises: A tiny RAG system from scratch.   Run:  python check.py A9

You'll build every piece except the LLM call: chunking, retrieval with cosine
similarity, a grounded prompt, and citation checking.
"""

import math
import re

STOPWORDS = {"a", "an", "the", "is", "are", "of", "to", "and", "or", "in", "on", "for", "do", "i",
             "what", "how", "it", "be", "can", "my", "with", "at", "by", "this", "that", "any"}


def chunk_words(text, size, overlap=0):
    # TODO: split text into words (text.split()) and return a list of chunks,
    # each a string of up to `size` words. Each new chunk starts `size - overlap`
    # words after the previous one. Stop once a chunk reaches the end of the text.
    # chunk_words("a b c d e", 2, 1) -> ["a b", "b c", "c d", "d e"]
    # Raise ValueError if overlap >= size.
    raise NotImplementedError


def tokenize(text):
    # TODO: lowercase words made of letters/digits (re.findall(r"[a-z0-9]+", ...)),
    # with STOPWORDS removed.  tokenize("What is the Refund policy?") -> ["refund", "policy"]
    raise NotImplementedError


def vectorize(text):
    # TODO: return {word: count} for tokenize(text).
    raise NotImplementedError


def cosine(a, b):
    # TODO: cosine similarity of two {word: count} vectors, rounded to 4 decimals.
    # Return 0.0 if either vector is empty.
    raise NotImplementedError


def retrieve(question, chunks, k=2):
    # TODO: return the indexes of the k chunks most similar to the question
    # (cosine of their vectors), best first. Ties keep the original order.
    # Leave out chunks with similarity 0.
    raise NotImplementedError


def grounded_prompt(question, sources):
    # TODO: sources is a list of chunk strings. Return:
    # "Answer the question using ONLY the numbered sources below. Cite sources like [1].\n"
    # "If the sources don't contain the answer, say you couldn't find it.\n\n"
    # "<sources>\n[1] first source\n[2] second source\n</sources>\n\n"
    # "Question: <question>"
    raise NotImplementedError


def citations(answer):
    # TODO: return the sorted, de-duplicated source numbers cited like [2] or [1][3].
    # citations("Yes [2]. Also see [1] and [2].") -> [1, 2]
    raise NotImplementedError


def unsupported_citations(answer, n_sources):
    # TODO: return cited numbers that don't exist (< 1 or > n_sources), sorted.
    # These are hallucinated citations - a red flag in any RAG system.
    raise NotImplementedError
