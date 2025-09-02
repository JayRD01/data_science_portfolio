# ds_bi_dashboards

**Status:** 🚧 Work in Progress (under construction).  
This repository is focused on **data visualization and dashboards** using **Power BI** and **Tableau**.  
Python is used mainly for **lightweight scripts** to prepare/refresh datasets and for **quick plots with Matplotlib**.

---

## 📂 Structure

```text
ds_bi_dashboards/
├─ README.md
├─ requirements.txt          # pandas, numpy, SQL, requests, jupyter, matplotlib
├─ .gitignore
├─ .gitattributes            # Git LFS for .pbix / .twbx / .hyper
│
├─ data/                     # Data
│  ├─ raw/                   # Original sources (CSV, Excel, JSON)
│  └─ processed/             # Cleaned data ready for BI tools
│
├─ notebooks/                # Jupyter notebooks (EDA, cleaning, transformations)
│
├─ scripts/                  # Utility scripts (ETL / exports)
│  └─ export_for_bi.py
│
├─ reports/                  # Final outputs
│  ├─ powerbi/               # Power BI (.pbix / .pbit)
│  ├─ tableau/               # Tableau (.twbx / .hyper)
│  ├─ pdf/                   # Exported PDFs
│  └─ images/                # Static images (e.g., Matplotlib PNGs)
│
└─ docs/                     # Minimal documentation
   ├─ OVERVIEW.md
   └─ images/
```

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

**Key dependencies:**  
- `pandas`, `numpy`  
- `SQLAlchemy`, `requests`  
- `matplotlib` (quick plots)  
- `jupyterlab`, `ipykernel`  

> Tip: Use a virtual environment (e.g., `python -m venv .venv && source .venv/bin/activate` or on Windows `.\.venv\Scriptsctivate`).

---

## 🚀 Usage

- Place original files in `data/raw/`.  
- Clean/transform with notebooks in `notebooks/` or scripts in `scripts/`.  
- Export BI-ready tables to `data/processed/`.  
- Keep **Power BI** files in `reports/powerbi/` and **Tableau** files in `reports/tableau/`.  
- Save static charts (e.g., Matplotlib PNGs) in `reports/images/`.  

---

## 🔒 Large Files & Binaries

Use **Git LFS** for BI binaries. Suggested `.gitattributes` entries:

```
*.pbix  filter=lfs diff=lfs merge=lfs -text
*.pbit  filter=lfs diff=lfs merge=lfs -text
*.twbx  filter=lfs diff=lfs merge=lfs -text
*.twb   filter=lfs diff=lfs merge=lfs -text
*.hyper filter=lfs diff=lfs merge=lfs -text
```

---

## 📌 Notes

- Keep secrets out of the repo. If you use environment variables, prefer a local `.env` not tracked by Git.  
- This project is intentionally **simple** to avoid overwhelming readers while still covering end-to-end BI workflows.
