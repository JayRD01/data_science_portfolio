# Strategy Pattern Overview (Models + Main)

This project uses the **Strategy** design pattern to decouple *what we do* (list directory entries and return typed objects) from *how we do it* (OS, Pathlib, FS backends).

## Scope of this document
Focus only on:
- The `models/` folder (interfaces, context, concrete strategies)
- The `main.py` at the project root

## Minimal folder tree
```text
.
├── main.py
└── models/
    ├── interfaces.py          # FileInfo (Pydantic) + StrategyMethod (abstract interface)
    ├── context.py             # StrategyManager (context that delegates to a StrategyMethod)
    ├── os_strategy.py         # StrategyOs: implementation using os.scandir
    ├── pathlib_strategy.py    # StrategyPathlib: implementation using pathlib.Path.iterdir
    └── fs_strategy.py         # StrategyFS: implementation using PyFilesystem2 (optional)
```

> **Note:** Class names are suggestions; use the names you actually implemented (e.g., `StrategyOs`, `StrategyPathlib`).

---

## Participants
- **FileInfo (model)**: Immutable, validated data object (Pydantic BaseModel) holding `name: str` and `size: int`.
- **StrategyMethod (strategy interface)**: Declares the operation all strategies must implement:
  - `explorer_strat(root: str) -> list[FileInfo]`
- **StrategyManager (context)**: Holds a reference to a `StrategyMethod` and delegates calls to it:
  - `set_strategy(strategy)` to switch at runtime
  - `explorer_strat(root)` to execute the current strategy
- **Concrete Strategies**:
  - **StrategyOs** (os.scandir)
  - **StrategyPathlib** (pathlib.Path.iterdir)
  - **StrategyFS** (PyFilesystem2; optional)

---

## Collaboration and data flow
1. **Client code** creates a `StrategyManager` with a chosen strategy (e.g., `StrategyOs()`).
2. Client calls `manager.explorer_strat(root)`.  
3. **StrategyManager** delegates to the injected **Strategy**.
4. **Concrete Strategy** scans `root`, creates **FileInfo** objects, returns `list[FileInfo]`.
5. Client receives a uniform, typed result regardless of the backend used.

This keeps the public API stable while allowing you to plug in new backends without changing calling code.

---

## Why Strategy here?
- **Open/Closed**: Add new backends without modifying the context or existing strategies.
- **Single Responsibility**: Each strategy owns only one concern: *how* to read entries from a backend.
- **Liskov Substitution**: Any `StrategyMethod` implementation can replace another transparently.
- **Dependency Inversion**: The context depends on an abstraction (`StrategyMethod`), not concrete modules.

---

## Minimal usage example (pseudo-code)
```python
# main.py (minimal)
from models.context import StrategyManager
from models.os_strategy import StrategyOs
# from models.pathlib_strategy import StrategyPathlib

if __name__ == "__main__":
    manager = StrategyManager(StrategyOs())
    entries = manager.explorer_strat(".")
    for fi in entries[:10]:
        print(f"{fi.name} - {fi.size} bytes")

    # Switch strategy at runtime (same interface, same return type)
    # manager.set_strategy(StrategyPathlib())
    # entries = manager.explorer_strat(".")
```

---

## Extending the system
- Create a new class implementing `StrategyMethod` (e.g., `StrategyS3`, `StrategyZip`).
- Ensure it returns `list[FileInfo]` with the same semantics (size=0 for directories, etc.).
- No changes required in `StrategyManager` or client code.
