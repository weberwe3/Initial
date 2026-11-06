"""Module A10 solutions."""


def validate_args(args, required):
    return [name for name in required if name not in args]


def run_tool(name, args, tools):
    if name not in tools:
        return f"error: unknown tool {name}"
    missing = validate_args(args, tools[name]["required"])
    if missing:
        return "error: missing " + ", ".join(missing)
    try:
        return str(tools[name]["func"](**args))
    except Exception as e:
        return f"error: {type(e).__name__}: {e}"


def needs_approval(name, risky_tools):
    return name in risky_tools


def agent_loop(task, model_step, tools, max_steps=5, risky_tools=frozenset(), approve=None):
    history = [{"role": "user", "content": task}]
    steps = 0
    while steps < max_steps:
        decision = model_step(history)
        if "final" in decision:
            return {"answer": decision["final"], "steps": steps, "history": history}
        name, args = decision["tool"], decision.get("args", {})
        history.append({"role": "assistant", "tool": name, "args": args})
        if needs_approval(name, risky_tools) and (approve is None or not approve(name, args)):
            result = "denied: needs human approval"
        else:
            result = run_tool(name, args, tools)
        history.append({"role": "tool", "content": result})
        steps += 1
    return {"answer": None, "steps": steps, "history": history, "stopped": "max_steps"}


def tool_call_log(history):
    log = []
    for i, msg in enumerate(history):
        if msg.get("role") == "assistant" and "tool" in msg:
            args = ", ".join(f"{k}={v}" for k, v in sorted(msg["args"].items()))
            result = history[i + 1]["content"] if i + 1 < len(history) else "(no result)"
            log.append(f"{msg['tool']}({args}) -> {result}")
    return log
