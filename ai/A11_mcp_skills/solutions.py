"""Module A11 solutions."""

import math
import re


def tools_list_result(tools):
    out = []
    for name, t in tools.items():
        out.append({
            "name": name,
            "description": t["description"],
            "inputSchema": {"type": "object",
                            "properties": {arg: {"type": typ} for arg, typ in t["params"].items()},
                            "required": list(t["params"])},
            "annotations": {"readOnlyHint": t["read_only"]},
        })
    return {"tools": out}


def handle_request(request, tools):
    base = {"jsonrpc": "2.0", "id": request["id"]}
    method = request.get("method")
    if method == "tools/list":
        return {**base, "result": tools_list_result(tools)}
    if method == "tools/call":
        params = request.get("params", {})
        name = params.get("name")
        if name not in tools:
            return {**base, "error": {"code": -32602, "message": f"Unknown tool: {name}"}}
        try:
            value = tools[name]["func"](**params.get("arguments", {}))
            return {**base, "result": {"content": [{"type": "text", "text": str(value)}], "isError": False}}
        except Exception as e:
            return {**base, "result": {"content": [{"type": "text", "text": f"{type(e).__name__}: {e}"}], "isError": True}}
    return {**base, "error": {"code": -32601, "message": "Method not found"}}


def needs_review(tools):
    return sorted(name for name, t in tools.items() if not t["read_only"])


def parse_skill(text):
    lines = text.strip().splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing frontmatter")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        raise ValueError("missing frontmatter")
    meta = {}
    for line in lines[1:end]:
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip()
    return {"name": meta.get("name", ""), "description": meta.get("description", ""),
            "body": "\n".join(lines[end + 1:]).strip()}


def validate_skill(meta):
    problems = []
    name = meta.get("name") or ""
    if not name:
        problems.append("name is required")
    else:
        if len(name) > 64:
            problems.append("name too long")
        if not re.fullmatch(r"[a-z0-9-]+", name):
            problems.append("name must be lowercase letters, numbers and hyphens")
        if "anthropic" in name or "claude" in name:
            problems.append("name uses a reserved word")
    desc = meta.get("description") or ""
    if not desc:
        problems.append("description is required")
    elif len(desc) > 1024:
        problems.append("description too long")
    return problems


def _words(text):
    return {w for w in re.findall(r"[a-z0-9]+", text.lower()) if len(w) > 3}


def select_skills(request, skills, min_overlap=2):
    req = _words(request)
    scored = [(len(req & _words(s["description"])), i, s["name"]) for i, s in enumerate(skills)]
    scored = [x for x in scored if x[0] >= min_overlap]
    scored.sort(key=lambda x: (-x[0], x[1]))
    return [name for _, _, name in scored]


def context_cost(skills, active_names):
    tokens = lambda text: math.ceil(len(text) / 4)
    always = sum(tokens(s["name"] + s["description"]) for s in skills)
    active = sum(tokens(s["body"]) for s in skills if s["name"] in active_names)
    return {"always": always, "active": active, "total": always + active}
