import inspect
import itertools


def test_countdown(ex):
    gen = ex.countdown(3)
    assert inspect.isgenerator(gen), "use `yield` to make a generator"
    assert list(gen) == [3, 2, 1]


def test_fibonacci(ex):
    gen = ex.fibonacci()
    assert inspect.isgenerator(gen), "use `yield` to make a generator"
    assert list(itertools.islice(gen, 8)) == [0, 1, 1, 2, 3, 5, 8, 13]


def test_only_errors(ex):
    lines = ["INFO ok\n", "ERROR disk full\n", "  ERROR timeout  \n", "WARN slow\n"]
    gen = ex.only_errors(lines)
    assert inspect.isgenerator(gen)
    assert list(gen) == ["ERROR disk full", "ERROR timeout"]


def test_batched(ex):
    assert list(ex.batched([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]
    assert list(ex.batched([], 3)) == []


def test_count_calls(ex):
    @ex.count_calls
    def hello(name):
        """Say hi."""
        return f"hi {name}"

    assert hello("a") == "hi a"
    hello("b")
    assert hello.calls == 2
    assert hello.__name__ == "hello", "use functools.wraps"


def test_uppercase_result(ex):
    @ex.uppercase_result
    def greet(name):
        return f"hello {name}"

    assert greet("ada") == "HELLO ADA"


def test_retry(ex):
    attempts = []

    @ex.retry(3)
    def flaky():
        attempts.append(1)
        if len(attempts) < 3:
            raise ConnectionError("nope")
        return "ok"

    assert flaky() == "ok"
    assert len(attempts) == 3

    tries = []

    @ex.retry(2)
    def always_fails():
        tries.append(1)
        raise ValueError("broken")

    try:
        always_fails()
    except ValueError:
        pass
    else:
        raise AssertionError("after the last attempt the exception should propagate")
    assert len(tries) == 2


def test_recorder(ex):
    log = []
    with ex.recorder(log):
        log.append("middle")
    assert log == ["start", "middle", "end"]

    log2 = []
    try:
        with ex.recorder(log2):
            raise KeyError("boom")
    except KeyError:
        pass
    assert log2 == ["start", "end"], "cleanup must run even when the block raises (try/finally)"


def test_word_frequencies(ex):
    assert ex.word_frequencies(["a", "b", "a"]) == {"a": 2, "b": 1}
    hints = ex.word_frequencies.__annotations__
    assert "words" in hints and "return" in hints, "add type hints for the parameter and the return value"
