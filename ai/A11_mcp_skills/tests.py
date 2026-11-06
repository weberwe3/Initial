METRICS = {("revenue", "2026-03"): 412300}


def get_metric(name, month):
    return METRICS[(name, month)]


def make_tools(log):
    return {
        "get_metric": {"description": "Get a KPI for a month.", "params": {"name": "string", "month": "string"},
                       "func": get_metric, "read_only": True},
        "create_ticket": {"description": "Open a ticket.", "params": {"title": "string"},
                          "func": lambda title: log.append(title) or "TCK-1", "read_only": False},
        "delete_rows": {"description": "Delete rows.", "params": {"table": "string"},
                        "func": lambda table: "deleted", "read_only": False},
    }


SKILL = """---
name: monthly-variance-report
description: Builds the monthly budget versus actual variance report with commentary. Use for variance reports or month-end commentary.
---

# Monthly variance report

1. Get actuals and budget.
2. Run scripts/variance.py.
"""

SKILLS = [
    {"name": "monthly-variance-report", "description": "Builds the monthly budget versus actual variance report with commentary. Use for variance reports or month-end commentary.", "body": "x" * 400},
    {"name": "workflow-docs", "description": "Documents an Alteryx workflow tool by tool for non-technical readers. Use when asked to explain or document a workflow.", "body": "y" * 800},
    {"name": "user-stories", "description": "Turns stakeholder notes into user stories with acceptance criteria.", "body": "z" * 200},
]


def test_tools_list_result(ex):
    got = ex.tools_list_result(make_tools([]))
    first = got["tools"][0]
    assert first == {"name": "get_metric", "description": "Get a KPI for a month.",
                     "inputSchema": {"type": "object", "properties": {"name": {"type": "string"}, "month": {"type": "string"}},
                                     "required": ["name", "month"]},
                     "annotations": {"readOnlyHint": True}}, f"got {first!r}"
    assert [t["name"] for t in got["tools"]] == ["get_metric", "create_ticket", "delete_rows"]


def test_handle_tools_list(ex):
    resp = ex.handle_request({"jsonrpc": "2.0", "id": 1, "method": "tools/list"}, make_tools([]))
    assert resp["jsonrpc"] == "2.0" and resp["id"] == 1
    assert len(resp["result"]["tools"]) == 3


def test_handle_tools_call(ex):
    log = []
    tools = make_tools(log)
    ok = ex.handle_request({"jsonrpc": "2.0", "id": 2, "method": "tools/call",
                            "params": {"name": "get_metric", "arguments": {"name": "revenue", "month": "2026-03"}}}, tools)
    assert ok == {"jsonrpc": "2.0", "id": 2, "result": {"content": [{"type": "text", "text": "412300"}], "isError": False}}, f"got {ok!r}"
    bad = ex.handle_request({"jsonrpc": "2.0", "id": 3, "method": "tools/call",
                             "params": {"name": "get_metric", "arguments": {"name": "profit", "month": "2026-03"}}}, tools)
    assert bad["result"]["isError"] is True and bad["result"]["content"][0]["text"].startswith("KeyError"), f"got {bad!r}"


def test_handle_errors(ex):
    tools = make_tools([])
    unknown = ex.handle_request({"jsonrpc": "2.0", "id": 4, "method": "tools/call",
                                 "params": {"name": "drop_db", "arguments": {}}}, tools)
    assert unknown == {"jsonrpc": "2.0", "id": 4, "error": {"code": -32602, "message": "Unknown tool: drop_db"}}
    nomethod = ex.handle_request({"jsonrpc": "2.0", "id": 5, "method": "files/delete"}, tools)
    assert nomethod == {"jsonrpc": "2.0", "id": 5, "error": {"code": -32601, "message": "Method not found"}}


def test_needs_review(ex):
    assert ex.needs_review(make_tools([])) == ["create_ticket", "delete_rows"]


def test_parse_skill(ex):
    got = ex.parse_skill(SKILL)
    assert got["name"] == "monthly-variance-report"
    assert got["description"].startswith("Builds the monthly budget")
    assert got["body"].startswith("# Monthly variance report") and got["body"].endswith("variance.py.")
    try:
        ex.parse_skill("# No frontmatter here")
    except ValueError:
        pass
    else:
        raise AssertionError("text without frontmatter should raise ValueError")


def test_validate_skill(ex):
    assert ex.validate_skill({"name": "monthly-variance-report", "description": "Does X. Use when Y."}) == []
    assert ex.validate_skill({"name": "Monthly Report", "description": ""}) == [
        "name must be lowercase letters, numbers and hyphens", "description is required"]
    assert ex.validate_skill({"name": "claude-helper", "description": "d"}) == ["name uses a reserved word"]
    assert ex.validate_skill({"name": "a" * 65, "description": "d" * 1025}) == ["name too long", "description too long"]
    assert ex.validate_skill({"description": "d"}) == ["name is required"]


def test_select_skills(ex):
    assert ex.select_skills("Can you write the variance commentary for March?", SKILLS) == ["monthly-variance-report"]
    assert ex.select_skills("Please document this Alteryx workflow", SKILLS) == ["workflow-docs"]
    assert ex.select_skills("What's the weather?", SKILLS) == []


def test_context_cost(ex):
    got = ex.context_cost(SKILLS, ["workflow-docs"])
    always = sum(-(-len(s["name"] + s["description"]) // 4) for s in SKILLS)
    assert got == {"always": always, "active": 200, "total": always + 200}, f"got {got!r}"
    assert ex.context_cost(SKILLS, [])["active"] == 0
