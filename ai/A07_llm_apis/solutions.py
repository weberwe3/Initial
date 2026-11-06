"""Module A07 solutions."""

import json
import math
import re
import time


def build_request(system, user_text, model="claude-opus-5-5", max_tokens=1000):
    return {"model": model, "max_tokens": max_tokens, "system": system,
            "messages": [{"role": "user", "content": user_text}]}


def extract_text(response):
    return "\n".join(b["text"] for b in response["content"] if b.get("type") == "text")


def parse_json_reply(text):
    try:
        return json.loads(text)
    except ValueError:
        pass
    fence = re.search(r"```(?:json)?\s*(.*?)```", text, re.S)
    if fence:
        try:
            return json.loads(fence.group(1))
        except ValueError:
            pass
    starts = [i for i in (text.find("{"), text.find("[")) if i >= 0]
    if starts:
        start = min(starts)
        end = max(text.rfind("}"), text.rfind("]"))
        if end > start:
            try:
                return json.loads(text[start:end + 1])
            except ValueError:
                pass
    raise ValueError("no JSON found")


def validate_record(data, schema):
    problems = []
    for field, allowed in schema.items():
        if field not in data:
            problems.append(f"missing: {field}")
        elif isinstance(allowed, list):
            if data[field] not in allowed:
                problems.append(f"not allowed: {field}={data[field]}")
        elif not isinstance(data[field], allowed):
            problems.append(f"bad type: {field}")
    return problems


def with_retry(func, retries=3, base_delay=1.0, sleep=None):
    sleep = sleep or time.sleep
    for attempt in range(retries):
        try:
            return func()
        except Exception:
            if attempt == retries - 1:
                raise
            sleep(base_delay * 2 ** attempt)


def classify_rows(rows, text_field, call_model, allowed_labels):
    out = []
    for row in rows:
        try:
            label = call_model(row[text_field])
        except Exception as e:
            out.append({**row, "label": None, "status": f"error: {type(e).__name__}"})
            continue
        if label in allowed_labels:
            out.append({**row, "label": label, "status": "ok"})
        else:
            out.append({**row, "label": None, "status": f"invalid label: {label}"})
    return out


def batch_cost(rows, text_field, prompt_overhead_tokens, output_tokens_per_row,
               input_price_per_million, output_price_per_million):
    tokens_in = sum(prompt_overhead_tokens + math.ceil(len(r[text_field]) / 4) for r in rows)
    tokens_out = output_tokens_per_row * len(rows)
    cost = tokens_in / 1e6 * input_price_per_million + tokens_out / 1e6 * output_price_per_million
    return round(cost, 4)
