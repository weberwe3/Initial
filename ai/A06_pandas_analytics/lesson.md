# Module A06: pandas for Business Analytics

**Goal:** do everyday analyst work in pandas (load, clean, reshape, summarise, chart and export) and know it well enough to check AI-written pandas code.
**Time:** 4–5 hours (on your own computer).

pandas is the Python library for tables. It's what AI assistants reach for
when you ask for analysis code, and what the Alteryx Python tool hands you.
After A05 you know what each operation *means*; now you'll learn the one-liners.

> **Run this module's code on your computer.** pandas isn't available in this
> app's in-browser Python. Set up once:
> ```bash
> python -m venv .venv
> source .venv/bin/activate          # Windows: .venv\Scripts\activate
> pip install pandas matplotlib openpyxl jupyter
> jupyter notebook                   # an interactive notebook in your browser
> ```
> Jupyter notebooks run code cell by cell and show tables and charts inline,
> the most comfortable way to explore data in Python.

---

## 1. DataFrames in 60 seconds

```python
import pandas as pd

df = pd.read_csv("sales.csv", parse_dates=["order_date"])
df.head()          # first 5 rows
df.shape           # (rows, columns)
df.info()          # columns, types, missing counts
df.describe()      # quick statistics for numeric columns
df["region"].value_counts()   # frequency table
```

A DataFrame is a table; each column is a **Series**. Operations apply to whole
columns at once, so there's no loop needed (that's why pandas is fast).

---

## 2. The Alteryx → pandas cheat sheet

| Alteryx | pandas |
|---------|--------|
| Input Data | `pd.read_csv(...)`, `pd.read_excel("f.xlsx", sheet_name="Data")` |
| Select (keep/rename) | `df[["a", "b"]]`, `df.rename(columns={"a": "A"})`, `df.drop(columns=["c"])` |
| Filter | `df[df["amount"] > 100]`, `df.query("region == 'North' and amount > 100")` |
| Formula | `df["margin"] = (df["price"] - df["cost"]) / df["price"]` |
| Conditional formula | `df["size"] = np.where(df["amount"] > 1000, "Large", "Small")` |
| Sort | `df.sort_values(["region", "amount"], ascending=[True, False])` |
| Unique | `df.drop_duplicates(subset=["customer_id"])` |
| Join | `pd.merge(orders, products, on="product_id", how="left", indicator=True)` |
| Union | `pd.concat([df1, df2], ignore_index=True)` |
| Summarize | `df.groupby("region").agg(total=("amount", "sum"), orders=("order_id", "count"))` |
| Cross Tab | `df.pivot_table(index="region", columns="quarter", values="amount", aggfunc="sum", fill_value=0)` |
| Transpose | `df.melt(id_vars=["region"], var_name="quarter", value_name="amount")` |
| Multi-Row Formula | `df["prev"] = df["amount"].shift(1)`; `df["running"] = df["amount"].cumsum()` |
| Data Cleansing | `df["name"].str.strip().str.title()`, `df.fillna({"amount": 0})` |
| Sample | `df.head(100)`, `df.sample(100, random_state=1)` |
| Output Data | `df.to_csv("out.csv", index=False)`, `df.to_excel("out.xlsx", index=False)` |

`how="left", indicator=True` on a merge adds a `_merge` column showing
`both` / `left_only`: the J and L anchors in one table.

---

## 3. Cleaning: where analysts spend their time

```python
df["customer"] = df["customer"].str.strip().str.title()
df["amount"] = pd.to_numeric(df["amount"].str.replace("[$,]", "", regex=True), errors="coerce")
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

print(df.isna().sum())                                   # missing per column
print(df[df["amount"].isna()].head())                    # inspect the bad rows
df = df.dropna(subset=["amount", "order_date"])
df = df.drop_duplicates()
```

`errors="coerce"` turns unparseable values into missing values instead of
crashing. **Always inspect what got coerced before dropping it.**

---

## 4. Dates and time series

```python
df["month"] = df["order_date"].dt.to_period("M")
monthly = df.groupby("month")["amount"].sum()

monthly_pct = monthly.pct_change() * 100        # month-over-month growth
rolling = monthly.rolling(3).mean()             # 3-month moving average
by_weekday = df.groupby(df["order_date"].dt.day_name())["amount"].mean()
```

---

## 5. Summaries that answer business questions

```python
summary = (
    df.groupby(["region", "channel"])
      .agg(revenue=("amount", "sum"),
           orders=("order_id", "nunique"),
           avg_order=("amount", "mean"))
      .reset_index()
      .sort_values("revenue", ascending=False)
)
summary["share_pct"] = summary["revenue"] / summary["revenue"].sum() * 100
```

Read it as a pipeline: group, aggregate, flatten, sort, add a share column.
The same shape as a chain of Alteryx tools.

---

## 6. Charts

```python
import matplotlib.pyplot as plt

ax = monthly.plot(kind="line", marker="o", title="Revenue by month")
ax.set_ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("revenue_by_month.png", dpi=150)
```

For exploration, `df.plot(...)` is enough. For polished dashboards, most teams
keep using Tableau or Power BI, fed by your clean output files.

---

## 7. Reading AI-written pandas critically

AI writes pandas well, but check for these:

| Watch for | Why |
|-----------|-----|
| `merge` without `how=` | Defaults to `inner`, silently dropping unmatched rows |
| Row counts not checked after merges | Duplicate keys multiply rows |
| `mean()` of a rate column | The average-of-averages mistake (A04) |
| `inplace=True` everywhere | Harder to follow; prefer reassigning `df = ...` |
| Chained indexing `df[df.a > 1]["b"] = ...` | May not modify `df` at all (a `SettingWithCopyWarning`) |
| Hard-coded file paths and dates | Breaks next month |

A great prompt add-on: *"Print the row count and the sum of revenue after every
step."* It turns AI code into self-checking code.

---

## 8. A complete mini-pipeline

```python
import pandas as pd

orders = pd.read_csv("orders.csv", parse_dates=["order_date"])
products = pd.read_csv("products.csv")
print("orders:", len(orders))

orders = orders[orders["status"] != "Test"]
print("after filter:", len(orders))

merged = pd.merge(orders, products, on="product_id", how="left", indicator=True)
print(merged["_merge"].value_counts())          # check unmatched products!

merged["margin"] = (merged["price"] - merged["cost"]) / merged["price"]
report = (merged.groupby("category")
                .agg(revenue=("price", "sum"), avg_margin=("margin", "mean"))
                .round(2)
                .sort_values("revenue", ascending=False))
report.to_excel("category_report.xlsx")
print(report)
```

---

## Key takeaways
- Every Alteryx tool has a pandas one-liner; groupby/agg, merge and pivot_table cover most work.
- Clean deliberately: coerce, inspect, then drop.
- Check AI pandas code for silent inner joins, duplicated rows and averaged rates.
- Ask for row counts and totals at every step.

**Continue reading:** [Python for Data Analysis, 3rd edition](https://wesmckinney.com/book/) (Wes McKinney, the creator of pandas). The definitive guide, free to read online, covering pandas, data cleaning, time series and plotting with business-style examples.

**Next:** [Module A07: Calling AI from Python](../A07_llm_apis/lesson.md)
