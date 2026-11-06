"""Module A08 solutions."""

import random


def accuracy(pred, gold):
    if len(pred) != len(gold):
        raise ValueError("pred and gold must be the same length")
    return round(sum(p == g for p, g in zip(pred, gold)) / len(gold), 3)


def confusion_matrix(pred, gold):
    matrix = {}
    for p, g in zip(pred, gold):
        matrix[(g, p)] = matrix.get((g, p), 0) + 1
    return matrix


def precision_recall(pred, gold, label):
    tp = sum(1 for p, g in zip(pred, gold) if p == label and g == label)
    predicted = sum(1 for p in pred if p == label)
    actual = sum(1 for g in gold if g == label)
    precision = round(tp / predicted, 3) if predicted else 0.0
    recall = round(tp / actual, 3) if actual else 0.0
    return precision, recall


def label_distribution(labels):
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    ordered = sorted(counts.items(), key=lambda kv: -kv[1])   # sorted() is stable: ties keep first-seen order
    return {label: round(n / len(labels) * 100, 1) for label, n in ordered}


def disagreements(rows, pred_field="pred", gold_field="gold"):
    return [r for r in rows if r[pred_field] != r[gold_field]]


def keyword_baseline(text, rules, default="other"):
    lower = text.lower()
    for label, keywords in rules:
        if any(k.lower() in lower for k in keywords):
            return label
    return default


def sample_for_gold(rows, n, seed=42):
    if n >= len(rows):
        return list(rows)
    return random.Random(seed).sample(rows, n)
