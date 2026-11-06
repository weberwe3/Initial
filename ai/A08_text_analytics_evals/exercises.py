"""
Module A08 exercises: Prove the AI's labels are good.   Run:  python check.py A8

`pred` is a list of labels from the AI, `gold` the human answer key, in the
same order.
"""

import random


def accuracy(pred, gold):
    # TODO: fraction of positions where pred == gold, rounded to 3 decimals.
    # Raise ValueError if the lists have different lengths.
    raise NotImplementedError


def confusion_matrix(pred, gold):
    # TODO: return {(gold_label, pred_label): count} for every pair that occurs.
    raise NotImplementedError


def precision_recall(pred, gold, label):
    # TODO: return (precision, recall) for one label, each rounded to 3 decimals.
    #   precision = true positives / everything predicted as label
    #   recall    = true positives / everything that really is label
    # Use 0.0 when the denominator is 0.
    raise NotImplementedError


def label_distribution(labels):
    # TODO: return {label: percentage of all labels, rounded to 1 decimal},
    # ordered from most to least common (ties: first seen first).
    raise NotImplementedError


def disagreements(rows, pred_field="pred", gold_field="gold"):
    # TODO: return the rows where the AI and the human disagree - the list you
    # read to improve the prompt.
    raise NotImplementedError


def keyword_baseline(text, rules, default="other"):
    # TODO: rules is a list of (label, [keywords]) checked IN ORDER. Return the
    # first label whose any keyword appears in the text (case-insensitive),
    # else default.
    raise NotImplementedError


def sample_for_gold(rows, n, seed=42):
    # TODO: return a random sample of n rows (without replacement) using
    # random.Random(seed).sample(rows, n), so the same seed gives the same sample.
    # If n >= len(rows) return a copy of all rows.
    raise NotImplementedError
