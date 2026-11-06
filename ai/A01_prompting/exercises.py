"""
Module A01 exercises: Prompts as code.   Run:  python check.py A1

Good prompts become templates your whole team can reuse. Here you'll build the
small toolkit that assembles them reliably.
"""


def wrap_in_tags(tag, text):
    # TODO: return "<tag>\n" + text + "\n</tag>"
    # wrap_in_tags("data", "a,b") -> "<data>\na,b\n</data>"
    raise NotImplementedError


def few_shot_block(examples):
    # TODO: examples is a list of (input, output) tuples. Return them as text:
    # "Example 1:\nInput: <input>\nOutput: <output>\n\nExample 2:\n..."
    # Blocks are separated by ONE blank line; no trailing newline.
    # Return "" for an empty list.
    raise NotImplementedError


def build_prompt(role, task, data=None, output_format=None, examples=None, allow_unsure=True):
    # TODO: assemble a prompt from parts, in this order, separated by blank lines
    # ("\n\n"), skipping any part that is None or empty:
    #   1. role
    #   2. task
    #   3. few_shot_block(examples)                     (if examples)
    #   4. "Format: " + output_format                   (if output_format)
    #   5. "If the information needed is missing or you are unsure, say so instead of guessing."
    #                                                   (if allow_unsure)
    #   6. wrap_in_tags("data", data)                   (if data)
    raise NotImplementedError


def fill_template(template, values):
    # TODO: replace {placeholders} in template with values from the dict.
    # If a placeholder is missing from values, raise KeyError whose message
    # names the missing placeholder.
    # fill_template("Hi {name}", {"name": "Ada"}) -> "Hi Ada"
    # Hint: str.format(**values) already raises KeyError('name') - you can just use it.
    raise NotImplementedError


def placeholders(template):
    # TODO: return a SORTED list of unique placeholder names in a template.
    # placeholders("{b} and {a} and {b}") -> ["a", "b"]
    # Hint: string.Formatter().parse(template) yields (text, field_name, spec, conversion).
    raise NotImplementedError


def prompt_checklist(prompt):
    # TODO: a quick "newcomer test". Return a list of missing elements, in this
    # order, from these checks (case-insensitive):
    #   "audience"  - none of: "you're", "you are", "audience", " for "
    #   "format"    - none of: "format", "bullet", "table", "json", "words"
    #   "escape hatch" - none of: "unsure", "not sure", "say so", "don't know"
    # Return [] if nothing is missing.
    raise NotImplementedError
