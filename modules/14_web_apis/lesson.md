# Module 14: Working with the Web

**Goal:** fetch data from web APIs, handle the JSON that comes back, and deal
with things going wrong.
**Time:** 3–4 hours.

---

## 1. What's an API?

A web **API** is a URL that returns *data* (usually JSON) instead of a web page.
Weather, exchange rates, GitHub, Spotify, your bank, your company's internal
tools: most services have one. If you can call APIs, you can connect almost
anything to anything.

The basic exchange:
1. Your program sends an HTTP **request** to a URL (usually a `GET` to read data).
2. The server sends back a **response** with a **status code** and a **body**.

| Status | Meaning |
|--------|---------|
| 200 | OK |
| 201 | Created |
| 400 | Bad request (your input was wrong) |
| 401 / 403 | Not logged in / not allowed |
| 404 | Not found |
| 429 | Too many requests: slow down |
| 500+ | The server broke |

---

## 2. `requests`

```bash
pip install requests
```

```python
import requests

response = requests.get("https://api.github.com/repos/python/cpython", timeout=10)
print(response.status_code)        # 200
data = response.json()             # JSON body → Python dict
print(data["stargazers_count"])
print(data["description"])
```

**Always set `timeout=`.** Without it, a slow server can hang your program forever.

### Query parameters
Don't build `?a=1&b=2` by hand. Let `requests` do it (it handles escaping):

```python
params = {"latitude": 51.5, "longitude": -0.12, "current": "temperature_2m"}
r = requests.get("https://api.open-meteo.com/v1/forecast", params=params, timeout=10)
print(r.url)     # the full URL it built
print(r.json()["current"]["temperature_2m"])
```

(Open-Meteo is free and needs no key, which makes it great for practice.)

### Sending data
```python
r = requests.post("https://httpbin.org/post", json={"name": "Ada"}, timeout=10)
```

---

## 3. Handling errors properly

Networks fail. Servers return errors. Your code should cope:

```python
import requests

def get_json(url, params=None):
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()          # turns 4xx/5xx into an exception
        return r.json()
    except requests.Timeout:
        print("The server took too long.")
    except requests.HTTPError as e:
        print(f"Server said no: {e.response.status_code}")
    except requests.RequestException as e:   # any other network problem
        print(f"Network problem: {e}")
    return None
```

---

## 4. Digging into JSON responses

Real API responses are nested dicts and lists. Explore them step by step:

```python
data = r.json()
print(type(data))            # dict or list?
print(data.keys())           # what's at the top?
import json
print(json.dumps(data, indent=2)[:1000])   # pretty-print the first part
```

Then extract only what you need into simple structures:

```python
# A typical shape
response = {
    "results": [
        {"name": {"first": "Ada", "last": "Lovelace"}, "location": {"city": "London"}},
        {"name": {"first": "Alan", "last": "Turing"}, "location": {"city": "Wilmslow"}},
    ],
    "info": {"page": 1},
}

people = [
    {"name": f"{r['name']['first']} {r['name']['last']}", "city": r["location"]["city"]}
    for r in response["results"]
]
```

Use `.get()` for fields that may be missing: `r.get("email", "")`.

---

## 5. API keys and secrets

Many APIs need a key. **Never put keys directly in your code**, especially
code you'll share or put on GitHub. Use an environment variable:

```python
import os
API_KEY = os.environ.get("WEATHER_API_KEY")
if not API_KEY:
    raise SystemExit("Set the WEATHER_API_KEY environment variable first.")

headers = {"Authorization": f"Bearer {API_KEY}"}
r = requests.get(url, headers=headers, timeout=10)
```

Set it in the terminal: `export WEATHER_API_KEY=...` (Mac/Linux) or
`$env:WEATHER_API_KEY="..."` (PowerShell). Or use a `.env` file with the
`python-dotenv` package, and **add `.env` to `.gitignore`**.

---

## 6. Being a good API citizen

- Read the API's documentation: endpoints, parameters, rate limits.
- Respect rate limits: add `time.sleep(1)` between many calls.
- Cache results you've already fetched (save to a JSON file) instead of
  re-downloading.
- Handle **pagination**: many APIs return results in pages. Keep requesting
  the next page until there are no more:

```python
def fetch_all(url):
    items, page = [], 1
    while True:
        data = requests.get(url, params={"page": page}, timeout=10).json()
        if not data["items"]:
            break
        items.extend(data["items"])
        page += 1
    return items
```

---

## 7. Design tip: separate fetching from processing

```python
def fetch_weather(lat, lon):          # talks to the network
    ...

def summarise_weather(data):          # pure: dict in, text out
    ...
```

The processing function can be tested without the internet, by passing in a
saved example response. This module's exercises work exactly this way, so
they run offline.

---

## Key takeaways
- `requests.get(url, params=..., timeout=10)` then `.raise_for_status()` and `.json()`.
- Handle `Timeout`, `HTTPError`, and `RequestException`.
- Explore nested JSON step by step; extract only what you need.
- Keys go in environment variables, never in code.
- Keep network code separate from processing code so it's testable.

**Next:** [Module 15: Intermediate power tools](../15_power_tools/lesson.md)
