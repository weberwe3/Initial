"""Module 14 solutions."""

from urllib.parse import urlencode


def build_url(base, params):
    return f"{base}?{urlencode(params)}"


def current_temperature(weather):
    return weather["current"]["temperature_2m"]


def simplify_users(response):
    return [
        {
            "name": f"{u['name']['first']} {u['name']['last']}",
            "email": u.get("email", ""),
            "city": u["location"]["city"],
        }
        for u in response["results"]
    ]


def repo_summary(repo):
    language = repo["language"] or "unknown"
    return f"{repo['full_name']} ({language}): {repo['stargazers_count']:,} stars"


def top_repos(repos, n=3):
    ranked = sorted(repos, key=lambda r: r["stargazers_count"], reverse=True)
    return [r["full_name"] for r in ranked[:n]]


def daily_summary(forecast):
    d = forecast["daily"]
    return [
        f"{day}: {low}-{high}°C"
        for day, low, high in zip(d["time"], d["temperature_2m_min"], d["temperature_2m_max"])
    ]


def fetch_json(get, url):
    response = get(url, timeout=10)
    if response.status_code != 200:
        raise RuntimeError(f"Request failed with status {response.status_code}")
    return response.json()


def fetch_all_pages(get, url):
    items = []
    page = 1
    while True:
        batch = get(url, params={"page": page}, timeout=10).json()["items"]
        if not batch:
            break
        items.extend(batch)
        page += 1
    return items
