# Data Science Template

Welcome to the **Data Science Template**, a highly structured and professional data science template scaffolded by Jay.

This template aims to boost productivity and maintain clarity in your projects by following best practices in modularity, environment management, and project documentation.

---

## 📁 Project Structure

```text
data_science_template
├── data/                  # Main data folder (do not upload large datasets to Git)
│   ├── raw/               # Original, immutable data dumps
│   ├── processed/         # Cleaned and feature-engineered datasets
│   └── external/          # Third-party or external data sources
│
├── models/                # Trained and serialized model objects (.pkl, .joblib, etc.)
│
├── notebooks/             # Jupyter notebooks for exploration and analysis
│
├── outputs/               # Final outputs, reports, visualizations, etc.
│   ├── reports/
│   │   └── visualization/ # Exported visual plots or report components
│
├── scripts/               # Reusable Python scripts (ETL, model training, etc.)
│
├── tests/                 # Unit and integration tests
│
├── environment.yml        # Conda environment specification
├── .gitignore             # Git ignore rules (auto-ignore models, datasets, etc.)
├── LICENSE                # Open source license (MIT)
├── README.md              # Project overview and usage instructions
├── setup.py               # For packaging and pip installation (optional)
├── tasks.py               # Optional automation (e.g., invoke or doit)
├── install.md             # Optional guide for environment and dependency setup
├── .here                  # Root marker used by scripts to find project root
