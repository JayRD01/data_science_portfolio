# 🧠 Data Science Portfolio

Welcome to **JayRD's Data Science Portfolio**.  
This repository is a **professional template for data science projects**, with emphasis on:

- 🧩 **Clean architecture** and modular design.  
- 📐 **SOLID principles**.  
- 🎯 **Design patterns** for flexibility and maintainability.  

---

## 📂 Project Structure

```bash
data_science_portfolio/
├── ds_explorer/               # Core package (strategies, main engine)
│   ├── main.py
│   ├── models/
│   ├── notebooks/
│   ├── outputs/
│   ├── scripts/
│   ├── tests/
│   ├── STRATEGY.md
│   ├── environment.yml
│   ├── requirements.txt
│   ├── docker-compose.yml
│   ├── install.md
│   ├── tasks.py
│   └── setup.py
├── LICENSE
└── README.md   <-- this file
```

### 🔑 Main folders
- **`ds_explorer/`** → Core implementation (strategies, entrypoint, utilities).  
- **`notebooks/`** → Jupyter notebooks (exploration, visualization templates).  
- **`outputs/`** → Generated reports, visualizations, and analysis results.  
- **`scripts/`** → Helper scripts (e.g. branch merge automation).  
- **`tests/`** → Unit tests for strategies and helpers.  

---

## 🛠 Environments Available

- **Conda** → `environment.yml`  
- **pip/venv** → `requirements.txt`  
- **Docker** → `docker-compose.yml`  

Each setup provides a reproducible environment for data exploration, visualization, and running the project.

---

## 🚀 How to Run

```bash
cd ds_explorer
python main.py
```

⚠️ Must be executed from a directory containing the `.here` marker file.

---

## 📚 More Information

For detailed insights into the **Strategy Pattern** and the **RootPath helper**, see [ds_explorer/STRATEGY.md](./ds_explorer/STRATEGY.md).
