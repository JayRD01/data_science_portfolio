# ds_missing_data

Welcome to **ds_missing_data**, a professional and well-structured data science template scaffolded by JayRD.

This template aims to improve productivity and maintain clarity in your projects by following best practices in modularity, environment management, and project documentation.

---

## 📁 Project Structure

```text
ds_missing_data/
├── Dockerfile                # Container build instructions
├── docker-compose.yml        # Multi-container orchestration (optional)
├── environment.yml           # Conda environment specification
├── install.md                # Setup/installation notes
├── LICENSE                   # Project license
├── README.md                 # Project overview and usage instructions
├── requirements.txt          # pip-based dependency list (if not using conda)
├── scripts/                  # Utility scripts (ETL, automation, etc.)
│
├── models/                   # Trained and serialized ML models
│
├── notebooks/                # Jupyter notebooks for exploration and prototyping
│
├── outputs/                  # Generated outputs of the project
│   └── reports/              # Reports generated during experiments
│       └── visualization/    # Exported plots, charts, figures
│
├── src/                      # Source code (main package)
│   ├── app/                  # Application layer: orchestrates pipelines, CLI
│   ├── core/                 # Core domain logic
│   │   ├── contracts/        # Interfaces/ABCs/Protocols
│   │   └── implementations/  # Concrete classes implementing contracts
│   └── utils/                # Utility helpers (logging, validation, etc.)
│
├── tests/                    # Unit and integration tests
│
├── setup.py                  # Install configuration (classic setuptools)
└── tasks.py                  # Automation tasks (invoke/doit)
```

---

## ⚙️ Setup Instructions

1. **Install dependencies**  
   - Using Conda:  
     ```bash
     conda env create -f environment.yml
     conda activate ds_missing_data
     ```  
   - Using venv:  
     ```bash
     python -m venv .venv
     source .venv/bin/activate
     pip install -r requirements.txt
     ```  

2. **Install project in editable mode**  
   ```bash
   pip install --editable .
   ```

3. **Run notebooks or pipelines** using Jupyter or directly from the `src/app` layer.

---

## 🧪 Tests

Run the unit tests with:

```bash
pytest tests/
```

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for full details.
