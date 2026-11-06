"""
Module A11 exercises: Look inside MCP and Skills.   Run:  python check.py A11

Part A builds a mini MCP request handler (the JSON-RPC messages an AI app sends
to a server). Part B parses, validates and selects Skills, including the token
budget that makes "progressive disclosure" work.
"""

import math
import re

# ---------------------------------------------------------------- Part A: MCP


def tools_list_result(tools):
    # TODO: tools is {name: {"description": str, "params": {arg: "string"|"number"|...},
    #                        "func": callable, "read_only": bool}}
    # Return the MCP "tools/list" result:
    #   {"tools": [{"name": n, "description": d,
    #               "inputSchema": {"type": "object",
    #                               "properties": {arg: {"type": t}, ...},
    #                               "required": [args in order]},
    #               "annotations": {"readOnlyHint": read_only}}, ...]}
    # Tools in the dict's order.
    raise NotImplementedError


def handle_request(request, tools):
    # TODO: answer one JSON-RPC 2.0 request dict like an MCP server.
    # Every response is {"jsonrpc": "2.0", "id": request["id"], ...} plus either
    #   "result": ...   or   "error": {"code": int, "message": str}
    #
    # method "tools/list" -> result = tools_list_result(tools)
    # method "tools/call" -> params {"name": ..., "arguments": {...}}
    #     unknown tool        -> error code -32602, message "Unknown tool: <name>"
    #     tool runs fine      -> result {"content": [{"type": "text", "text": str(value)}], "isError": False}
    #     tool raises         -> result {"content": [{"type": "text", "text": "<ExceptionName>: <msg>"}], "isError": True}
    #     (a failing TOOL is a normal result with isError True, not a protocol error)
    # any other method    -> error code -32601, message "Method not found"
    raise NotImplementedError


def needs_review(tools):
    # TODO: governance check. Return the sorted names of tools that are NOT
    # marked read_only - the ones an admin must review and gate with approval.
    raise NotImplementedError


# ---------------------------------------------------------------- Part B: Skills


def parse_skill(text):
    # TODO: parse a SKILL.md. It starts with a line "---", then "key: value"
    # lines, then a line "---", then the Markdown body.
    # Return {"name": ..., "description": ..., "body": <body stripped>}.
    # Values are stripped. Raise ValueError("missing frontmatter") if the text
    # doesn't start with a "---" line or has no closing "---" line.
    raise NotImplementedError


def validate_skill(meta):
    # TODO: return a list of problems (empty if valid), checked in this order:
    #   "name is required"                    name missing or empty
    #   "name too long"                       more than 64 characters
    #   "name must be lowercase letters, numbers and hyphens"
    #   "name uses a reserved word"           contains "anthropic" or "claude"
    #   "description is required"             missing or empty
    #   "description too long"                more than 1024 characters
    # (Skip the other name checks if the name is missing.)
    raise NotImplementedError


def select_skills(request, skills, min_overlap=2):
    # TODO: simulate how an assistant picks skills from DESCRIPTIONS ONLY.
    # Words = lowercase runs of letters/digits (re.findall(r"[a-z0-9]+", ...)),
    # ignoring words of 3 letters or fewer. Score = number of distinct request
    # words that appear in the skill's description words.
    # Return names with score >= min_overlap, best first (ties: original order).
    raise NotImplementedError


def context_cost(skills, active_names):
    # TODO: estimate tokens used (ceil(len(text) / 4) for each piece):
    #   every skill's name + description (always loaded), plus
    #   the full body of each skill in active_names.
    # Return {"always": <tokens>, "active": <tokens>, "total": <tokens>}.
    raise NotImplementedError
