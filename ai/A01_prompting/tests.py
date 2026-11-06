def test_wrap_in_tags(ex):
    assert ex.wrap_in_tags("data", "a,b") == "<data>\na,b\n</data>"


def test_few_shot_block(ex):
    got = ex.few_shot_block([("hi", "Praise"), ("why??", "Question")])
    assert got == "Example 1:\nInput: hi\nOutput: Praise\n\nExample 2:\nInput: why??\nOutput: Question", f"got {got!r}"
    assert ex.few_shot_block([]) == ""


def test_build_prompt_full(ex):
    got = ex.build_prompt("You help finance.", "Summarize.", data="x,y", output_format="3 bullets",
                          examples=[("a", "b")])
    expected = ("You help finance.\n\nSummarize.\n\nExample 1:\nInput: a\nOutput: b\n\nFormat: 3 bullets\n\n"
                "If the information needed is missing or you are unsure, say so instead of guessing.\n\n<data>\nx,y\n</data>")
    assert got == expected, f"got:\n{got}"


def test_build_prompt_minimal(ex):
    assert ex.build_prompt("Role.", "Task.", allow_unsure=False) == "Role.\n\nTask.", "skip parts that are None/empty"


def test_fill_template(ex):
    assert ex.fill_template("Hi {name}, your {metric} is up", {"name": "Ada", "metric": "NPS"}) == "Hi Ada, your NPS is up"
    try:
        ex.fill_template("Hi {name}", {})
    except KeyError as e:
        assert "name" in str(e)
    else:
        raise AssertionError("a missing placeholder should raise KeyError")


def test_placeholders(ex):
    assert ex.placeholders("{b} and {a} and {b}") == ["a", "b"]
    assert ex.placeholders("no fields") == []


def test_prompt_checklist(ex):
    assert ex.prompt_checklist("Summarize this.") == ["audience", "format", "escape hatch"]
    good = "You're helping sales. Give 3 bullets. If unsure, say so."
    assert ex.prompt_checklist(good) == []
    assert ex.prompt_checklist("Write a table for the CFO.") == ["escape hatch"]
