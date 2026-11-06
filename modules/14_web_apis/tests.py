class FakeResponse:
    def __init__(self, data, status_code=200):
        self._data = data
        self.status_code = status_code

    def json(self):
        return self._data


USERS = {
    "results": [
        {"name": {"first": "Ada", "last": "Lovelace"}, "email": "ada@example.com",
         "location": {"city": "London", "country": "UK"}},
        {"name": {"first": "Alan", "last": "Turing"},
         "location": {"city": "Wilmslow", "country": "UK"}},
    ]
}

REPOS = [
    {"full_name": "a/one", "stargazers_count": 10, "language": "Python", "description": ""},
    {"full_name": "b/two", "stargazers_count": 500, "language": None, "description": ""},
    {"full_name": "c/three", "stargazers_count": 60123, "language": "Python", "description": ""},
    {"full_name": "d/four", "stargazers_count": 99, "language": "Go", "description": ""},
]


def test_build_url(ex):
    got = ex.build_url("https://api.example.com/search", {"q": "python docs", "page": 2})
    assert got == "https://api.example.com/search?q=python+docs&page=2", f"got {got!r}"


def test_current_temperature(ex):
    assert ex.current_temperature({"current": {"temperature_2m": 12.3, "wind_speed_10m": 9.1}}) == 12.3


def test_simplify_users(ex):
    got = ex.simplify_users(USERS)
    assert got == [
        {"name": "Ada Lovelace", "email": "ada@example.com", "city": "London"},
        {"name": "Alan Turing", "email": "", "city": "Wilmslow"},
    ], f"got {got!r}"


def test_repo_summary(ex):
    assert ex.repo_summary(REPOS[2]) == "c/three (Python): 60,123 stars"
    assert ex.repo_summary(REPOS[1]) == "b/two (unknown): 500 stars"


def test_top_repos(ex):
    assert ex.top_repos(REPOS) == ["c/three", "b/two", "d/four"]
    assert ex.top_repos(REPOS, 1) == ["c/three"]


def test_daily_summary(ex):
    forecast = {"daily": {"time": ["2026-11-06", "2026-11-07"],
                          "temperature_2m_max": [14.2, 11.0],
                          "temperature_2m_min": [6.1, 4.3]}}
    assert ex.daily_summary(forecast) == ["2026-11-06: 6.1-14.2°C", "2026-11-07: 4.3-11.0°C"]


def test_fetch_json(ex):
    calls = []

    def ok_get(url, timeout=None):
        calls.append((url, timeout))
        return FakeResponse({"hello": "world"})

    assert ex.fetch_json(ok_get, "https://x.test") == {"hello": "world"}
    assert calls[0][1] is not None, "always pass a timeout"

    def bad_get(url, timeout=None):
        return FakeResponse(None, 404)

    try:
        ex.fetch_json(bad_get, "https://x.test")
    except RuntimeError as e:
        assert "404" in str(e)
    else:
        raise AssertionError("a 404 should raise RuntimeError")


def test_fetch_all_pages(ex):
    pages = {1: ["a", "b"], 2: ["c"], 3: []}
    requested = []

    def fake_get(url, params=None, timeout=None):
        requested.append(params["page"])
        return FakeResponse({"items": pages.get(params["page"], [])})

    assert ex.fetch_all_pages(fake_get, "https://x.test") == ["a", "b", "c"]
    assert requested == [1, 2, 3], f"pages requested: {requested}"
