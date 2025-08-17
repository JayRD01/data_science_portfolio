🚀 ds_explorer

**Modular File System Explorer built with Python**  
Designed for extensibility, clarity, and real-world applications in data science workflows.

> 🔗 GitHub: [JayRD01](https://github.com/JayRD01)

---

## 🧠 Overview

`ds_explorer` is a **strategy-based system** for exploring files and directories using interchangeable backends. It allows seamless switching between file system access methods like `os`, `pathlib`, and `PyFilesystem2`—all without altering the core execution logic.

This architecture demonstrates clean code practices and SOLID principles, with a particular focus on the **Strategy Design Pattern**.

---

## ⚙️ Architecture

### Core Components

| Component        | Responsibility                                      |
|------------------|-----------------------------------------------------|
| `StrategyManager`| Orchestrates strategy injection and execution       |
| `StrategyMethod` | Protocol defining the required strategy interface   |
| `FileInfo`       | Immutable data model representing file metadata     |
| `RootPath`       | Locates the project root dynamically using a `.here` marker file |

---

## 🛠️ Strategies Implemented

Each strategy implements the `explorer_strat(root: str) -> list[FileInfo]` method.

| Strategy Class     | Backend Used             | Description                                       |
|--------------------|--------------------------|---------------------------------------------------|
| `StrategyOs`       | `os.scandir()`           | Low-level system scan, efficient for large dirs   |
| `StrategyPathlib`  | `pathlib.Path.iterdir()` | High-level Pythonic interface for path handling   |
| `StrategyFS`       | `PyFilesystem2` (`fs`)   | Virtual file systems: memory, FTP, S3, etc.       |

---

## 📁 Root Path Resolution

`RootPath` recursively searches for a `.here` marker starting from the current working directory up to the filesystem root.  
If the file is not found, the program will raise a clear exception with instructions.

> 📌 To use this system, **create a `.here` file** in the root directory of your project:
>
> ```bash
> touch /your/project/path/.here
> ```

---

## ✅ Key Features

- 🔄 **Pluggable Strategy System**  
  Easily add new file exploration strategies without modifying existing code.

- 🧪 **Testable & Modular Design**  
  Clear separation of concerns and reusable components.

- 🧩 **Cross-platform & Portable**  
  No hardcoded paths; root detection adapts to the environment.

- 🔐 **Robust Error Handling**  
  Clean exceptions with user-friendly guidance.

---

## 🔍 Example Use Case

```python
from models.context_manager import StrategyManager
from models.os_strategy import StrategyOs
from models.root_path import RootPath

# Resolve the project root dynamically
root_path = RootPath(marker=".here", root=".")  

# Use OS strategy to explore
manager = StrategyManager(strategy=StrategyOs(), rootpath=root_path)
files = manager.explorer_strat()

for file in files[:5]:
    print(f"{file.name} — {file.size} bytes")
```

---

## 📦 Dependencies

- Python 3.10+
- `pydantic`
- `fs` (PyFilesystem2)

Install dependencies via:

```bash
pip install -r requirements.txt
```

---

## 📚 License

This project is released under the [MIT License](LICENSE).

---