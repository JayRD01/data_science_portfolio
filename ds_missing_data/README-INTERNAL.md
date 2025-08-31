# ds_missing_data — Missing Values Toolkit (pandas-first, pattern-driven)

**Goal**: Build a modular, docker-ready (later), pandas-first toolkit to **inspect, visualize, impute, and validate** missing values with clear software design patterns and a compact, extensible API.

---

## Why this project?
- Real datasets always have **missingness**; handling it cleanly matters more than any model.
- We favor **clarity over cleverness**, and **composition over one-off notebooks**.
- The code is organized so you can reuse components in other projects without copying large chunks of notebook code.

---

## What’s included (today)
- **Missing-data accessor** for pandas: `df.missing.summary()` and `df.missing.impute(...)`.
- **Correlation workflow**: build, filter (proxy), and plot top pairwise correlations.
- **Sampling utilities**: quick random slices for iterative exploration.
- **NA normalization on load**: consistent treatment of sentinels and odd strings before analysis.

> Docker, SQL (SQLite/MySQL) and API integrations are intentionally scoped for a later project phase.

---

## Architecture Overview

```
Notebook / main.py
   ├─ src/core/implementations/
   │   ├─ null_report_run.py         # pandas accessor: df.missing.summary(), df.missing.impute(...)
   │   ├─ correlation_columns_run.py # build long-form pairwise correlations
   │   ├─ corr_filterproxy_run.py    # proxy: validate + filter + deduplicate correlation pairs
   │   ├─ corr_plotter_run.py        # plotting of top correlations
   │   └─ sample_run.py              # sampling utilities for rapid inspection
   └─ data/
      └─ ocean.csv                   # example dataset (loaded with NA normalization)
```

**Data flow (minimal loop)**

```
read_csv (with NA normalization)
  → df.missing.summary()
  → correlations → filter(proxy) → plot
  → df.missing.impute(strategy, columns)
  → sample / validate
```

---

## Design Patterns Used (and why)

### 1) Template Method (new)
We define a base workflow that handles a column or a list of columns uniformly. Subclasses implement the specific column transformation (e.g., fill-then-normalize, median-impute, forward-fill). This yields **consistent handling**, **lower duplication**, and easy **extension**.

**Skeleton**:
```python
class NullHandlerTemplate(ABC):
    def run(self, df, columns):
        cols = [columns] if isinstance(columns, str) else list(columns)
        for col in cols:
            if col not in df.columns:
                raise ValueError(f"Column '{col}' not found.")
            df = self._handle_column(df, col)
        return df

    @abstractmethod
    def _handle_column(self, df, col): ...
```

### 2) Factory Method (new)
Map a **string strategy** to a **concrete handler class** so the user selects behavior without coupling to implementations.

**Skeleton**:
```python
class NullHandlerFactory:
    _registry = {
        "normalize_mean": NormalizeWithMean,
        "median": ReplaceWithMedian,
        "ffill": ForwardFill,
    }
    @staticmethod
    def create(handler_type: str):
        try:
            return NullHandlerFactory._registry[handler_type]()
        except KeyError:
            raise ValueError(f"Unknown strategy '{handler_type}'")
```

### 3) Proxy (applied in correlations)
`CorrFilterProxy` guards the plotter. It **validates** schema, **filters by threshold**, **deduplicates** symmetric pairs, and returns a clean, ordered slice for visualization.

### 4) pandas Accessor (API extension)
Not a GoF pattern, but a powerful extension technique. We register `df.missing` so the workflow reads naturally and remains discoverable (`df.missing.?`). This keeps transformations close to the data while preserving separation of concerns in code.

---

## Missing-Data API (pandas accessor)

### `summary()`
Returns a column-wise overview: datatype, missing count/%, unique count, zeros (if numeric).

```python
summary = df.missing.summary()
```

**Typical output**

| column | dtype   | n_missing | pct_missing | n_unique | n_zeros |
|-------:|:--------|----------:|------------:|---------:|--------:|
| …      | float64 |       123 |       12.34 |      456 |      10 |

### `impute(strategy, columns)`
Dispatches to the factory-backed handler. Works with a **single column** or a **list** of columns.

```python
df2 = df.missing.impute("normalize_mean", ["sea_temp_c", "salinity"])
df3 = df.missing.impute("median", "chlorophyll")
```

**Included strategies (MVP)**
- `normalize_mean` → fill NaN with column mean, then z-normalize
- `median` → fill NaN with column median
- `ffill` → forward-fill (useful for time-like series)

> Add more by subclassing `NullHandlerTemplate` and registering in `NullHandlerFactory._registry`.

---

## Correlation Workflow (pairs → proxy → plot)

1. **Build pairs** (`CorrColumns`): numeric-only, long-form `col_a, col_b, corr`.
2. **Filter/clean** (`CorrFilterProxy`): threshold on |corr|, deduplicate A–B vs B–A, sort by magnitude.
3. **Plot** (`CorrPlotter`): visualize top-N correlations for quick hypotheses.

This split improves **composability** (you can reuse steps 1–2 without plotting), **testability**, and **clarity**.

---

## NA Normalization on Load

We normalize both **string sentinels** and **numeric codes** at read time (e.g., `"NA"`, `"N/A"`, `"missing"`, `-99`, `-999`, etc.) so downstream logic sees **real NaN** early. Benefits:
- Simpler branching (one representation for “missing”)
- More accurate summaries
- Cleaner imputations

> Keep the normalization dictionary close to the data; it’s part of your dataset’s **provenance**.

---

## Quick Start (minimal)

```python
# 1) Load
df = pd.read_csv("data/ocean.csv", na_filter=True, na_values=[
    "missing","NA","N/A","n/a","", "?", "*",".", -9,-99,-999,-9999,9999,66,77,88,-1
])

# 2) Overview
df.missing.summary()

# 3) Correlations → filter → plot
df_pairs = CorrColumns(df=df).correlate_pairs()
df_top = CorrFilterProxy(df=df_pairs).filter(pct_filter_col=0.50)  # |corr| > 0.5
CorrPlotter(df=df_top).plot(color="red", show_median=False)

# 4) Impute
df2 = df.missing.impute("normalize_mean", ["sea_temp_c", "salinity"])
```

---

## Extending the System

- **New imputers**: subclass `NullHandlerTemplate`, register in the factory.
- **New correlation methods**: add `method="pearson|spearman|kendall"` in `CorrColumns`.
- **Reports**: export `summary`/correlation outputs to `outputs/reports/` with timestamps.
- **Types**: consider `Int64` (nullable) and `string[pyarrow]` to keep NA fidelity.

---

## What’s next (deferred on purpose)
- **Docker & Compose**: isolate runtime and dependencies.
- **Data sources**: `requests` for microservices; SQLite/MySQL with SQLAlchemy for storage.
- **Validation suite**: column contracts, drift checks, acceptance thresholds for post-imputation quality.

---

## One-line rationale
Small, composable pieces with clear responsibilities beat large, monolithic notebooks—**especially** for missing-data work.

-----------------------
