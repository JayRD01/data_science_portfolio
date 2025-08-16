# Data Science Template — Installation Guide

## 📦 Prerequisites

- [Miniconda/Anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)
- (Optional) [Mamba](https://mamba.readthedocs.io/en/latest/) for faster environment creation

---

## 🛠️ Create and activate the environment

Using **conda**:
```bash
conda env create -f environment.yml
conda activate data_science_template
```

Or with **mamba**:
```bash
mamba env create -f environment.yml
mamba activate data_science_template
```

The environment now includes all dependencies required to run the project.

---

## 🧱 Install project module (editable mode)

To move beyond notebook prototyping, install the project module in editable mode:

```bash
pip install --editable .
```

Now you can import your local modules directly from the `data_science_template/` folder.

Enable autoreload in Jupyter for smooth development:
```python
%load_ext autoreload
%autoreload 2
```

Example usage:
```python
from data_science_template.utils.paths import data_dir
data_dir()
```

---

## 🧪 Enable Git diff support for notebooks

We recommend using [nbdime](https://nbdime.readthedocs.io/en/stable/index.html) to manage notebook diffs.

Quick setup:
```bash
nbdime config-git --enable
```

Optional: enable notebook and lab extensions
```bash
nbdime extensions --enable --sys-prefix

# or do it manually:
jupyter serverextension enable --py nbdime --sys-prefix
jupyter nbextension install --py nbdime --sys-prefix
jupyter nbextension enable --py nbdime --sys-prefix
jupyter labextension install nbdime-jupyterlab
jupyter lab build
```

---

## 📊 Plotly support in JupyterLab

To enable Plotly's interactive visualizations in JupyterLab, run:

```bash
jupyter labextension install @jupyter-widgets/jupyterlab-manager@0.36 --no-build
jupyter labextension install plotlywidget@0.2.1 --no-build
jupyter labextension install @jupyterlab/plotly-extension@0.16 --no-build
jupyter lab build
```

Always check the [Plotly README](https://github.com/plotly/plotly.py#jupyterlab-support) for updated instructions.

---

## ⚙️ Invoke tasks automation

We use [Invoke](http://www.pyinvoke.org/) to manage project tasks.

List all available tasks:
```bash
invoke -l
```

Help for a specific task:
```bash
invoke --help lab
```

Example:
```
Usage: inv[oke] [--core-opts] lab [--options]

Docstring:
  Launch Jupyter Lab

Options:
  -i STRING, --ip=STRING   IP to listen on, defaults to *
  -p INT, --port=INT       Port to listen on, defaults to 8888
```

All tasks are defined in `tasks.py`. You can create your own custom commands to automate repetitive actions.
