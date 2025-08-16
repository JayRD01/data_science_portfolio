# 🧠 Data Science Portfolio

Welcome to **JayRD's Data Science Portfolio**. This repository presents a professional template for data science projects, focused on modularity, thematic organization, and clean architecture based on **SOLID principles** and **design patterns**.

## 📂 Project Structure

```
data_science_portfolio/
├── ds_explorer/
│   ├── main.py
│   ├── models/
│   │   ├── os_strategy.py
│   │   ├── pathlib_strategy.py
│   │   ├── fs_strategy.py
│   │   ├── interfaces.py
│   │   └── root_path.py
│   ├── .here
│   └── README.md
├── notebooks/
├── outputs/
├── scripts/
│   └── merge_branches.sh
├── tests/
├── STRATEGY.md
├── environment.yml
├── docker-compose.yml
├── install.md
├── LICENSE
└── setup.py
```

## 🧩 General Architecture

This project revolves around a single central software that:

- Reads directories.
- Extracts file metadata.
- Analyzes the data using tools like **pandas** and **numpy**.
- Implements **SOLID** principles and the **Strategy** pattern.

Includes three interchangeable strategies:

- `os.scandir`
- `pathlib.Path`
- `pyfilesystem (fs)`

And a helper `RootPath` class that dynamically detects the root of the project.

## 🚀 How to Run

```bash
cd ds_explorer
python main.py
```

⚠️ You must execute the script from a directory that contains the `.here` marker file.

---

## 📚 More Info

Check out [`STRATEGY.md`](./STRATEGY.md) to understand how the strategy pattern was implemented and extended.