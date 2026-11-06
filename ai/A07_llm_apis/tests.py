def test_build_request(ex):
    got = ex.build_request("Be brief.", "Hi")
    assert got == {"model": "claude-opus-5-5", "max_tokens": 1000, "system": "Be brief.",
                   "messages": [{"role": "user", "content": "Hi"}]}, f"got {got!r}"
    assert ex.build_request("s", "u", model="m", max_tokens=5)["max_tokens"] == 5


def test_extract_text(ex):
    resp = {"content": [{"type": "thinking", "thinking": ""}, {"type": "text", "text": "Line 1"},
                        {"type": "text", "text": "Line 2"}]}
    assert ex.extract_text(resp) == "Line 1\nLine 2"
    assert ex.extract_text({"content": []}) == ""


def test_parse_json_reply(ex):
    assert ex.parse_json_reply('{"a": 1}') == {"a": 1}
    assert ex.parse_json_reply('Sure! Here it is:\n```json\n{"label": "price"}\n```\nAnything else?') == {"label": "price"}
    assert ex.parse_json_reply('The result is [1, 2, 3] as requested.') == [1, 2, 3]
    assert ex.parse_json_reply('Answer: {"x": {"y": 2}} done') == {"x": {"y": 2}}
    try:
        ex.parse_json_reply("no json here")
    except ValueError:
        pass
    else:
        raise AssertionError("should raise ValueError when there's no JSON")


def test_validate_record(ex):
    schema = {"sentiment": ["positive", "neutral", "negative"], "score": int, "summary": str}
    assert ex.validate_record({"sentiment": "positive", "score": 4, "summary": "ok"}, schema) == []
    assert ex.validate_record({"sentiment": "angry", "score": "4"}, schema) == [
        "not allowed: sentiment=angry", "bad type: score", "missing: summary"]


def test_with_retry_succeeds_eventually(ex):
    calls, waits = [], []

    def flaky():
        calls.append(1)
        if len(calls) < 3:
            raise TimeoutError("slow")
        return "ok"

    assert ex.with_retry(flaky, retries=3, base_delay=1.0, sleep=waits.append) == "ok"
    assert waits == [1.0, 2.0], f"delays should double: got {waits}"


def test_with_retry_gives_up(ex):
    waits = []

    def broken():
        raise ConnectionError("down")

    try:
        ex.with_retry(broken, retries=2, base_delay=0.5, sleep=waits.append)
    except ConnectionError:
        pass
    else:
        raise AssertionError("should re-raise after the last attempt")
    assert waits == [0.5], "2 attempts means only 1 wait"


def test_classify_rows(ex):
    rows = [{"id": 1, "text": "too pricey"}, {"id": 2, "text": "boom"}, {"id": 3, "text": "late box"},
            {"id": 4, "text": "meh"}]

    def fake_model(text):
        if text == "boom":
            raise RuntimeError("API error")
        return {"too pricey": "price", "late box": "delivery", "meh": "vibes"}[text]

    got = ex.classify_rows(rows, "text", fake_model, ["price", "quality", "delivery"])
    assert [r["label"] for r in got] == ["price", None, "delivery", None]
    assert [r["status"] for r in got] == ["ok", "error: RuntimeError", "ok", "invalid label: vibes"]
    assert "label" not in rows[0], "don't modify the input rows"


def test_batch_cost(ex):
    rows = [{"t": "x" * 400}, {"t": "y" * 40}]
    # row 1: 200 + 100 = 300 in; row 2: 200 + 10 = 210 in; 2 x 50 out
    got = ex.batch_cost(rows, "t", 200, 50, 3.0, 15.0)
    assert got == 0.0030, f"(510 x $3 + 100 x $15) / 1M = $0.00303 → 0.003, got {got!r}"
