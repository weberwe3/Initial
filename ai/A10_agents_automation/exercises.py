"""
Module A10 exercises: Build an agent loop (with a fake model).   Run:  python check.py A10

The "model" is a function you're given: model_step(history) returns either
    {"tool": "<name>", "args": {...}}      to request a tool call, or
    {"final": "<answer>"}                   when it's done.
YOUR code runs tools, enforces the rules, and keeps the history.
"""


def validate_args(args, required):
    # TODO: return a list of required argument names that are missing from args
    # (in the order given in `required`).
    raise NotImplementedError


def run_tool(name, args, tools):
    # TODO: tools is {name: {"func": callable, "required": [arg names]}}.
    # Return the tool's result as a string. Never raise - return error strings:
    #   unknown tool        -> "error: unknown tool <name>"
    #   missing arguments   -> "error: missing <arg1>, <arg2>"
    #   the tool raises     -> "error: <ExceptionName>: <message>"
    raise NotImplementedError


def needs_approval(name, risky_tools):
    # TODO: True if this tool is in risky_tools (a set of names).
    raise NotImplementedError


def agent_loop(task, model_step, tools, max_steps=5, risky_tools=frozenset(), approve=None):
    # TODO: run the agent.
    # history starts as [{"role": "user", "content": task}].
    # Each step: decision = model_step(history)
    #   - "final" in decision -> return {"answer": decision["final"], "steps": <tool calls made>, "history": history}
    #   - tool request -> append {"role": "assistant", "tool": name, "args": args} to history.
    #       If needs_approval(name, risky_tools) and (approve is None or not approve(name, args)),
    #       the result is "denied: needs human approval" (don't run the tool).
    #       Otherwise result = run_tool(name, args, tools).
    #       Append {"role": "tool", "content": result} to history.
    # If max_steps tool calls happen without a final answer, return
    #   {"answer": None, "steps": max_steps, "history": history, "stopped": "max_steps"}
    raise NotImplementedError


def tool_call_log(history):
    # TODO: an audit log. Return a list of strings, one per tool call in history:
    #   "<tool>(<args as k=v, comma-separated, sorted by key>) -> <result>"
    # where result is the content of the "tool" message that follows it.
    raise NotImplementedError
