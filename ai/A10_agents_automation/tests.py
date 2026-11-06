METRICS = {("revenue", "2026-02"): 100.0, ("revenue", "2026-03"): 90.0}


def get_metric(name, month):
    return METRICS[(name, month)]


def make_tools(sent):
    return {
        "get_metric": {"func": get_metric, "required": ["name", "month"]},
        "send_email": {"func": lambda to, body: sent.append((to, body)) or "sent", "required": ["to", "body"]},
    }


def scripted(*decisions):
    """A fake model that returns the given decisions in order."""
    it = iter(decisions)
    return lambda history: next(it)


def test_validate_args(ex):
    assert ex.validate_args({"a": 1}, ["a", "b", "c"]) == ["b", "c"]
    assert ex.validate_args({"a": 1, "b": 2}, ["a", "b"]) == []


def test_run_tool(ex):
    tools = make_tools([])
    assert ex.run_tool("get_metric", {"name": "revenue", "month": "2026-02"}, tools) == "100.0"
    assert ex.run_tool("delete_db", {}, tools) == "error: unknown tool delete_db"
    assert ex.run_tool("get_metric", {"name": "revenue"}, tools) == "error: missing month"
    assert ex.run_tool("get_metric", {"name": "profit", "month": "2026-02"}, tools) == "error: KeyError: ('profit', '2026-02')"


def test_needs_approval(ex):
    assert ex.needs_approval("send_email", {"send_email"}) is True
    assert ex.needs_approval("get_metric", {"send_email"}) is False


def test_agent_loop_answers(ex):
    model = scripted(
        {"tool": "get_metric", "args": {"name": "revenue", "month": "2026-02"}},
        {"tool": "get_metric", "args": {"name": "revenue", "month": "2026-03"}},
        {"final": "Revenue fell 10%."},
    )
    out = ex.agent_loop("How did revenue change?", model, make_tools([]))
    assert out["answer"] == "Revenue fell 10%." and out["steps"] == 2
    assert out["history"][0] == {"role": "user", "content": "How did revenue change?"}
    assert out["history"][1] == {"role": "assistant", "tool": "get_metric", "args": {"name": "revenue", "month": "2026-02"}}
    assert out["history"][2] == {"role": "tool", "content": "100.0"}


def test_agent_loop_blocks_risky_tools(ex):
    sent = []
    model = scripted({"tool": "send_email", "args": {"to": "ceo@co.com", "body": "hi"}}, {"final": "done"})
    out = ex.agent_loop("Email the CEO", model, make_tools(sent), risky_tools={"send_email"})
    assert sent == [], "a risky tool must not run without approval"
    assert out["history"][2] == {"role": "tool", "content": "denied: needs human approval"}

    sent2 = []
    model2 = scripted({"tool": "send_email", "args": {"to": "me@co.com", "body": "hi"}}, {"final": "done"})
    ex.agent_loop("Email me", model2, make_tools(sent2), risky_tools={"send_email"}, approve=lambda n, a: a["to"] == "me@co.com")
    assert sent2 == [("me@co.com", "hi")], "an approved risky call should run"


def test_agent_loop_step_limit(ex):
    model = lambda history: {"tool": "get_metric", "args": {"name": "revenue", "month": "2026-02"}}
    out = ex.agent_loop("loop forever", model, make_tools([]), max_steps=3)
    assert out["answer"] is None and out["steps"] == 3 and out["stopped"] == "max_steps"
    assert len(out["history"]) == 1 + 3 * 2


def test_tool_call_log(ex):
    history = [
        {"role": "user", "content": "q"},
        {"role": "assistant", "tool": "get_metric", "args": {"month": "2026-02", "name": "revenue"}},
        {"role": "tool", "content": "100.0"},
    ]
    assert ex.tool_call_log(history) == ["get_metric(month=2026-02, name=revenue) -> 100.0"]
