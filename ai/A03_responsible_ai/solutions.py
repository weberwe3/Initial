"""Module A03 solutions."""

import re

EMAIL_RE = r"[\w.+-]+@[\w-]+\.[\w.]+"
PHONE_RE = r"\(?\b\d{3}\)?[-. ]?\d{3}[-. ]\d{4}\b"


def redact_emails(text):
    return re.sub(EMAIL_RE, "[EMAIL]", text)


def redact_phones(text):
    return re.sub(PHONE_RE, "[PHONE]", text)


def redact_pii(text, extra_terms=()):
    text = redact_phones(redact_emails(text))
    for term in extra_terms:
        text = re.sub(re.escape(term), "[REDACTED]", text, flags=re.IGNORECASE)
    return text


def find_pii(text):
    return {"emails": len(re.findall(EMAIL_RE, text)), "phones": len(re.findall(PHONE_RE, text))}


def pseudonymise(rows, column, prefix="CUST"):
    codes = {}
    out = []
    for row in rows:
        value = row[column]
        if value not in codes:
            codes[value] = f"{prefix}_{len(codes) + 1:03d}"
        out.append({**row, column: codes[value]})
    return out


def drop_columns(rows, columns):
    return [{k: v for k, v in row.items() if k not in columns} for row in rows]


def safe_to_share(text, banned_terms):
    found = find_pii(text)
    if found["emails"] or found["phones"]:
        return False
    lower = text.lower()
    return not any(term.lower() in lower for term in banned_terms)
