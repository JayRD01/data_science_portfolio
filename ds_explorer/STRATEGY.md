# 🧩 ds_explorer — Core Engine

This package contains the **core engine** of the Data Science Portfolio project.  
It focuses on exploring directories, extracting metadata, and applying **design patterns** for flexibility and extensibility.

---

## 📂 Key Components

- **`main.py`** → Entry point of the project. Runs the selected exploration strategy and coordinates data processing.  
- **`src/core/implementations/`** → Implements the **Strategy Pattern** and related helpers:  
  - `os_strategy.py` → Uses `os.scandir`.  
  - `pathlib_strategy.py` → Uses `pathlib.Path`.  
  - `fs_strategy.py` → Uses **pyfilesystem2**.  
  - `root_path.py` → Dynamic resolver for project root (via `.here` marker).  
  - `context_manager.py` → Manages execution context for strategies.  
  - `strategy_contract` → Typed contracts that define expected behavior.  

---

## 🧩 Design Patterns in Use

### 🎯 Strategy Pattern
Core logic for exploring filesystems is abstracted as interchangeable strategies:  
- OS strategy (`os.scandir`)  
- Pathlib strategy (`pathlib.Path`)  
- FS strategy (`pyfilesystem2`)  

This ensures the system can **swap implementations easily** while maintaining the same interface.

### 📐 Template Method (RootPath)
`RootPath` acts as a **pre-processor** before strategy execution:  
- Looks for a `.here` marker file to resolve the real root path.  
- Falls back to the provided path if not found.  
- Passes the resolved root to the active strategy.  

It behaves like a **template method**, adding logic before delegating to the selected strategy.  

---

## 🛠 Usage Example

```python
from src.utils.root_path import RootPath
from src.core.implementations.os_strategy_run import StrategyOs
from src.core.implementations.context_manager import StrategyManager

rootpath = RootPath(root=".", marker=".here")
manager = StrategyManager(StrategyOs(), rootpath)
result = manager.explorer_strat(".")
```

---

## ✅ Benefits
- 🔄 Flexible and extensible architecture.  
- 🧼 Clean separation of concerns.  
- 📌 Dynamic root detection with `.here`.  
- 🚀 Easy to extend with new strategies.  

---

## 📝 Requirements
A `.here` file must exist at the intended project root:

```bash
touch ds_explorer/.here
```
