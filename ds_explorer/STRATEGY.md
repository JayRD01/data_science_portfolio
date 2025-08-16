# 🧩 RootPath Strategy — Dynamic Root Resolver

## ✨ Introduction

The `RootPath` class acts as an **intelligent extension** to the Strategy pattern in this project, whose mission is to **automatically resolve the project root** using a `.here` marker file.

## 🧠 What Problem Does It Solve?

In multi-layered project structures, manually setting a root path (like `"."` or `"/home/user/project"`) can be fragile. This module:

- Detects the project root from any subdirectory.
- Ensures consistent paths for strategies like `os`, `pathlib`, or `fs`.

---

## ⚙️ How It Works

1. **Searches** for the `.here` file starting from the given `root`'s parent.
2. If found, **resolves** that path as the true root.
3. If not found, **falls back** to the original root.
4. Then, it **calls the assigned strategy**.

---

## 🧩 Design Pattern Used

### 📐 Template Method Pattern

`RootPath` behaves like a template that executes a preliminary step (resolving the root) before invoking `explorer_strat()`.

### 🎁 Light Decorator

It doesn't alter the original strategies. It simply adjusts the `root` value passed to them.

---

## 🛠 Usage Example

```python
from models.root_path import RootPath
from models.os_strategy import StrategyOs
from models.interfaces import StrategyManager

rootpath = RootPath(root=".", marker=".here")
manager = StrategyManager(StrategyOs(), rootpath)
result = manager.explorer_strat(".")
```

---

## ✅ Benefits

- 🔄 Flexible and extensible.
- 🧼 Follows the Single Responsibility Principle (SRP).
- 📌 Useful in deployments where working paths change dynamically.

---

## 📝 Requirements

You must have a `.here` file at the intended project root:

```bash
touch ds_explorer/.here
```