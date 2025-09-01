**Surgical precision, architect’s vision, and value-first data products.**  
I design modular systems that turn raw data into decisions — fast, reproducible, and business-oriented.

> 🔗 GitHub: [JayRD01](https://github.com/JayRD01)

![me](https://github.com/user-attachments/assets/f2ebbbb1-cfa8-44c3-97ce-39640dad55b7)

---

## 🧠 Overview

This portfolio is a **single, coherent framework** for building data products that scale across teams and timelines.  
It focuses on three pillars: **Design Patterns**, **Analytical Rigor**, and **Operational Excellence** (environments & automation).  
The mission is simple: **translate code into time saved, risk reduced, and value delivered** — in the language stakeholders understand.

> Where others see tables, I see **living structures**; where others ship notebooks, I ship **decisions**. 🏛️📊

---
## 🧾 Stakeholder Lens (what you get)

- **Time**: automated checks & clear contracts cut iteration cycles.  
- **Clarity**: patterns make intent obvious; onboarding is faster.  
- **Reliability**: environments are predictable; results are reproducible.  
- **Leverage**: microservices expose insights where they’re needed (dashboards, apps, notebooks).

> I combine patterns, analysis, and vision to create what others only imagine — and ship value without wasting anyone’s time. 🗽

---

## 🧩 Patterns Roadmap (toward 24 distinct patterns)

Each module explores **different patterns** so the whole portfolio converges to **24+**. The set includes (non‑exhaustive):  
**Strategy, Template Method, Adapter, Decorator, Builder, Singleton, Proxy, Facade, Observer, Factory Method, Abstract Factory, Command, Composite, Iterator, State, Mediator, Memento, Prototype, Flyweight, Chain of Responsibility, Interpreter, Visitor, Bridge**, plus pragmatic patterns (e.g., **Repository/Specification/Service Locator**) when they better serve data workflows.

- **Why patterns?** They compress experience into structure: fewer surprises, faster onboarding, safer changes.  
- **How they help data science?** They separate **analysis** from **plumbing**, enabling reliable EDA, feature work, and production hand‑off without rewrites.

---

## 🧪 Engineering Tenets

- **SOLID** by design: contracts vs. implementations, single-responsibility classes, small composable units.  
- **Typed, immutable models** for clarity and safer refactors.  
- **Explicit errors & guardrails**: traceable failures over silent bugs.  
- **Reproducibility first**: deterministic seeds, pinned envs, Docker parity.  
- **Docs that explain *why*** (trade-offs & impact), not just *what*.

---

## 🧭 Repository Layout (core idea)

```
src/
  core/
    contracts/         # Protocols / ABCs: the *what*
    implementations/   # Concrete classes: the *how*
  utils/               # Cross-cutting helpers (e.g., root path, logging, io)
  app/                 # Microservices (Flask/FastAPI) for demos & orchestration
tests/                 # Lives on a dedicated testing branch to avoid team friction
```

- `core/` enforces the boundary: **contracts define behavior; implementations plug in**.
- `utils/` hosts reusables shared by any module.
- `app/` is the gateway to **microservices** that expose analyses & pipelines via HTTP.

> **Testing policy:** The `tests/` tree is maintained in a **dedicated branch** focused on experimentation and CI, so day‑to‑day changes in main don’t block teammates.

---

## 🧰 Environments & Reproducibility

- **py-venv** for lightweight local work.  
- **Conda/Mamba** for scientific stacks and env locking.  
- **Docker** for environment parity; **Docker Compose** to run multiple services in parallel (e.g., API + generator + store).

**Example (concept) – docker-compose.yml**

```yaml
version: "3.9"
services:
  api:
    build: ./src/app/api
    command: uvicorn main:app --host 0.0.0.0 --port 8000
    ports: ["8000:8000"]
    depends_on: [generator]
  generator:
    build: ./src/app/generator
    command: python run.py
  store:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: example
    ports: ["5432:5432"]
```

> Swap **Flask** or **FastAPI** freely inside `app/`; patterns insulate the rest.

---

## 🧪 Reusable Proxy Example (RootPath)

A tiny, practical **Proxy** that centralizes *where the project root is* so the rest of the code stays ignorant of the filesystem.  
Drop it into `src/utils/` and import it anywhere — the code never hardcodes paths.

```python
from pathlib import Path
import os

class RootPath:
    def __init__(self, marker=".here", root="."):
        self.root = self.resolve(Path(root), marker)
        print(f"Now you are here: {self.root}")

    def resolve(self, start_path: Path, marker: str) -> str:
        search_path = start_path.resolve()
        for directory in [search_path] + list(search_path.parents):
            marker_path = directory / marker
            if marker_path.exists():
                return str(directory)

        raise FileNotFoundError(
            f"Marker file '{marker}' not found.\n"
            f"Please create a '{marker}' file at the project root.\n"
            f"Search started from: {search_path}\n"
        )

    def __str__(self):
        return self.root

# Create instance -> finds the project root
project_root = RootPath()
root_path = Path(str(project_root))

# Change the current working directory to the project root
os.chdir(root_path)

# Confirm current working directory
print("Current working directory:", Path.cwd())
```

**Why this is a Proxy:** it stands in front of the filesystem and **controls access** to the “real” root, enforcing a single, consistent source of truth. Benefits: no hardcoded paths, easier testing, safer scripts, simpler Docker mounts.

---

## ⚙️ Operating Modes (quick start)

### Local (py-venv)
```bash
python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
```

### Conda / Mamba
```bash
mamba env create -f environment.yml  # or: conda env create -f environment.yml
mamba activate dsp                   # or: conda activate dsp
```

### Docker
```bash
docker build -t dsp:latest .
docker run --rm -it -p 8000:8000 dsp:latest
```

### Docker Compose (parallel services)
```bash
docker compose up --build
```

---

## 📬 Contact

Issues & collab → [@JayRD01](https://github.com/JayRD01)
