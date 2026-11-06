"""
Module 14 exercises: Working with API data.   Run:  python check.py 14

These run OFFLINE: you're given responses that look exactly like what real
APIs return. Functions that "fetch" receive a `get` function as a parameter
so the checker can pass in a fake one. (In real code you'd pass requests.get.)
"""

from urllib.parse import urlencode


def build_url(base, params):
    # TODO: return base + "?" + the encoded params.
    # build_url("https://api.example.com/search", {"q": "python docs", "page": 2})
    #   -> "https://api.example.com/search?q=python+docs&page=2"
    # Hint: urllib.parse.urlencode does the encoding.
    raise NotImplementedError


def current_temperature(weather):
    # TODO: weather looks like the Open-Meteo response:
    #   {"current": {"temperature_2m": 12.3, "wind_speed_10m": 9.1}, ...}
    # Return the temperature.
    raise NotImplementedError


def simplify_users(response):
    # TODO: response looks like:
    #   {"results": [{"name": {"first": "Ada", "last": "Lovelace"},
    #                 "email": "ada@example.com",
    #                 "location": {"city": "London", "country": "UK"}}, ...]}
    # Return [{"name": "Ada Lovelace", "email": "...", "city": "London"}, ...]
    # Some users may have no "email" key - use "" for them.
    raise NotImplementedError


def repo_summary(repo):
    # TODO: repo looks like a GitHub API response with keys
    #   "full_name", "stargazers_count", "language", "description"
    # Return e.g. "python/cpython (Python): 60,123 stars"
    # If language is None, show "unknown".
    raise NotImplementedError


def top_repos(repos, n=3):
    # TODO: repos is a list of repo dicts (as above). Return the full_names of
    # the n repos with the most stars, most first.
    raise NotImplementedError


def daily_summary(forecast):
    # TODO: forecast looks like:
    #   {"daily": {"time": ["2026-11-06", "2026-11-07"],
    #              "temperature_2m_max": [14.2, 11.0],
    #              "temperature_2m_min": [6.1, 4.3]}}
    # Return ["2026-11-06: 6.1-14.2°C", "2026-11-07: 4.3-11.0°C"]
    # Hint: zip() the three lists together.
    raise NotImplementedError


def fetch_json(get, url):
    # TODO: call get(url, timeout=10). The returned object has:
    #   .status_code (int) and .json() (method returning the data).
    # If status_code is 200, return the data. Otherwise raise
    # RuntimeError(f"Request failed with status {status_code}").
    raise NotImplementedError


def fetch_all_pages(get, url):
    # TODO: call get(url, params={"page": p}, timeout=10) for p = 1, 2, 3, ...
    # Each response's .json() is {"items": [...]}. Keep going until a page
    # has an EMPTY items list. Return all items in one list.
    raise NotImplementedError
