"""Module A01 solutions."""

import string


def wrap_in_tags(tag, text):
    return f"<{tag}>\n{text}\n</{tag}>"


def few_shot_block(examples):
    blocks = [f"Example {i}:\nInput: {inp}\nOutput: {out}" for i, (inp, out) in enumerate(examples, start=1)]
    return "\n\n".join(blocks)


def build_prompt(role, task, data=None, output_format=None, examples=None, allow_unsure=True):
    parts = [role, task]
    if examples:
        parts.append(few_shot_block(examples))
    if output_format:
        parts.append("Format: " + output_format)
    if allow_unsure:
        parts.append("If the information needed is missing or you are unsure, say so instead of guessing.")
    if data:
        parts.append(wrap_in_tags("data", data))
    return "\n\n".join(p for p in parts if p)


def fill_template(template, values):
    return template.format(**values)


def placeholders(template):
    names = {field for _, field, _, _ in string.Formatter().parse(template) if field}
    return sorted(names)


def prompt_checklist(prompt):
    p = prompt.lower()
    checks = [
        ("audience", ["you're", "you are", "audience", " for "]),
        ("format", ["format", "bullet", "table", "json", "words"]),
        ("escape hatch", ["unsure", "not sure", "say so", "don't know"]),
    ]
    return [name for name, cues in checks if not any(c in p for c in cues)]
