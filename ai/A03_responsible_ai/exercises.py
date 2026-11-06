"""
Module A03 exercises: A data-minimisation toolkit.   Run:  python check.py A3

Before data goes anywhere near an AI tool, these functions strip or mask what
the AI doesn't need. (A safety net, not a guarantee: names in free text,
for example, need human judgement or specialised tools.)
"""

import re

EMAIL_RE = r"[\w.+-]+@[\w-]+\.[\w.]+"
PHONE_RE = r"\(?\b\d{3}\)?[-. ]?\d{3}[-. ]\d{4}\b"   # 555-123-4567, (555) 123-4567, 555.123.4567


def redact_emails(text):
    # TODO: replace every email address with "[EMAIL]". Use EMAIL_RE and re.sub.
    raise NotImplementedError


def redact_phones(text):
    # TODO: replace every phone number with "[PHONE]". Use PHONE_RE.
    raise NotImplementedError


def redact_pii(text, extra_terms=()):
    # TODO: redact emails and phones, then replace each term in extra_terms
    # (e.g. client names) with "[REDACTED]", case-insensitively.
    # Hint: re.sub(re.escape(term), "[REDACTED]", text, flags=re.IGNORECASE)
    raise NotImplementedError


def find_pii(text):
    # TODO: return {"emails": <count>, "phones": <count>} found in text.
    raise NotImplementedError


def pseudonymise(rows, column, prefix="CUST"):
    # TODO: rows is a list of dicts. Return a NEW list of NEW dicts where the
    # value in `column` is replaced by a stable code: the first distinct value
    # becomes f"{prefix}_001", the second f"{prefix}_002", and so on.
    # The same original value must always get the same code.
    # Don't modify the input rows.
    raise NotImplementedError


def drop_columns(rows, columns):
    # TODO: return new dicts without the listed columns (data minimisation).
    raise NotImplementedError


def safe_to_share(text, banned_terms):
    # TODO: return True only if the text contains no emails, no phones, and
    # none of banned_terms (case-insensitive).
    raise NotImplementedError
