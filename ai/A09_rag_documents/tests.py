CHUNKS = [
    "Refunds are available within 30 days of purchase with a receipt.",
    "Shipping is free for orders over 50 dollars. Standard shipping takes 3 to 5 days.",
    "Our office is closed on public holidays.",
    "Refund requests after 30 days need manager approval.",
]


def test_chunk_words(ex):
    assert ex.chunk_words("a b c d e", 2, 1) == ["a b", "b c", "c d", "d e"]
    assert ex.chunk_words("a b c d e", 2) == ["a b", "c d", "e"]
    assert ex.chunk_words("a b c", 5) == ["a b c"]
    try:
        ex.chunk_words("a b c", 2, 2)
    except ValueError:
        pass
    else:
        raise AssertionError("overlap >= size should raise ValueError")


def test_tokenize(ex):
    assert ex.tokenize("What is the Refund policy?") == ["refund", "policy"]


def test_vectorize(ex):
    assert ex.vectorize("Refund the refund, now!") == {"refund": 2, "now": 1}


def test_cosine(ex):
    assert ex.cosine({"a": 1}, {"a": 3}) == 1.0
    assert ex.cosine({"a": 1}, {"b": 1}) == 0.0
    assert ex.cosine({"refund": 2, "policy": 1}, {"refund": 1, "window": 1}) == 0.6325
    assert ex.cosine({}, {"a": 1}) == 0.0


def test_retrieve(ex):
    assert ex.retrieve("How long do refunds take after purchase?", CHUNKS, k=2)[0] == 0
    got = ex.retrieve("refund after 30 days", CHUNKS, k=3)
    assert set(got[:2]) == {0, 3} and 2 not in got, f"got {got}"
    assert ex.retrieve("free shipping", CHUNKS, k=1) == [1]
    assert ex.retrieve("parking garage", CHUNKS) == [], "no overlap means no results"


def test_grounded_prompt(ex):
    got = ex.grounded_prompt("Is shipping free?", ["Shipping is free over $50.", "Returns take 5 days."])
    expected = ("Answer the question using ONLY the numbered sources below. Cite sources like [1].\n"
                "If the sources don't contain the answer, say you couldn't find it.\n\n"
                "<sources>\n[1] Shipping is free over $50.\n[2] Returns take 5 days.\n</sources>\n\n"
                "Question: Is shipping free?")
    assert got == expected, f"got:\n{got}"


def test_citations(ex):
    assert ex.citations("Yes [2]. Also see [1] and [2].") == [1, 2]
    assert ex.citations("See [1][3].") == [1, 3]
    assert ex.citations("No sources.") == []


def test_unsupported_citations(ex):
    assert ex.unsupported_citations("True [1], also [4] and [0].", 3) == [0, 4]
    assert ex.unsupported_citations("Fine [2].", 3) == []
