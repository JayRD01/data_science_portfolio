# ds_explorer — Reliable FS exploration with TDD 🧪

A compact, test-driven file system explorer. The goal is **reliable, portable** exploration across **OS / Pathlib / PyFilesystem** strategies with clear contracts and predictable error handling.

> Snapshot: **unittest + coverage**; small, readable tests; strategy pattern; protocol-based contracts.

---

## 🚀 Features

- **Strategy pattern**: interchangeable backends (OS, Pathlib, FS).
- **Contracts first**: `Protocols/ABCs` define behavior; implementations stay swappable.
- **Deterministic tests**: focus on error paths (non-string roots, missing/permission cases).
- **Coverage-aware**: track gaps and raise confidence over time.
- **Clean imports**: `__init__.py` maintained in `src/` and `tests/` for smooth discovery.

---

## 📦 Project layout (short)
```text
ds_sync_store/
├─ src/
│  ├─ __init__.py
│  ├─ app/
│  │  └─ __init__.py
│  ├─ core/
│  │  ├─ __init__.py
│  │  ├─ contracts/           # Protocols / ABCs
│  │  │  └─ __init__.py
│  │  └─ implementations/     # Concrete strategies
│  │     └─ __init__.py
│  └─ utils/
│     └─ __init__.py
├─ tests/
│  ├─ __init__.py
│  ├─ test_strategies.py
│  ├─ test_strategy_fs_behavior.py
│  └─ test_*.py
└─ README.md
```

> Keep `__init__.py` in both `src/` and `tests/` so `unittest` discovery and imports work seamlessly.

---

## ⚙️ Setup

```bash
# Using pip
python -m venv .venv && source .venv/bin/activate   # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt

# Or using conda
conda env create -f environment.yml && conda activate ds_explorer
```

---

## 🧪 Run tests (unittest)

Verbose and readable:
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

Quiet, buffered (good for CI):
```bash
python -W ignore -m unittest discover -s tests -p "test_*.py" -b -q
```

Flags you’ll actually use:
- `-W ignore` → silence Python warnings
- `-b` → buffer stdout/stderr; only show on failure
- `-v` / `-q` → verbose / quiet (use one)

---

## 📈 Coverage

Run the suite under coverage:
```bash
coverage run -m unittest discover -s tests -p "test_*.py"
```

See missing lines:
```bash
coverage report -m
```

Generate an HTML report:
```bash
coverage html
# open htmlcov/index.html
```

---

## ✅ Naming conventions

Tests:
```text
test_<method>_<scenario>_<expected>()
# Example:
test_deposit_positive_amount_increases_balance
```

Files:
```text
test_<area>.py   # e.g., test_strategies.py, test_fs.py
```

Keep names short and meaningful — readability > verbosity.

---

## 🧩 Custom suites (optional)

```python
import unittest
from tests.test_strategies import TestStrategies

def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestStrategies))
    return s

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())
```

---

## Roadmap

- Lift utility coverage to 90%+.
- Add property-based tests (Hypothesis) for path edge cases.
- CI gates for coverage thresholds and linting.

---

## License

This project is licensed under the **MIT License**. See `LICENSE` for details.
