from invoke import task

@task
def clean(c):
    """
    Clean temporary files and folders (e.g. __pycache__, *.pyc).
    """
    print("Cleaning project...")  # You can use c.run() here
    # Example:
    # c.run("find . -type d -name '__pycache__' -exec rm -r {} +")
    # c.run("find . -type f -name '*.pyc' -delete")

@task
def test(c):
    """
    Run unit tests located in the 'tests' folder.
    """
    print("Running tests...")
    # Example:
    # c.run("pytest tests")

@task
def lint(c):
    """
    Run linter (e.g., flake8 or pylint) on scripts and notebooks.
    """
    print("Running linting...")  
    # Example:
    # c.run("flake8 scripts")

@task
def format(c):
    """
    Format code using black or similar tool.
    """
    print("Formatting code...")  
    # Example:
    # c.run("black scripts tests notebooks")

@task
def run_notebook(c, path="notebooks/example.ipynb"):
    """
    Run a Jupyter notebook (default: example.ipynb).
    """
    print(f"Running notebook at: {path}")  
    # Example:
    # c.run(f"jupyter nbconvert --to notebook --execute {path} --inplace")

@task
def build_all(c):
    """
    Run all major steps: clean, test, lint, etc.
    """
    print("Executing full build pipeline...")  
    # You can call tasks manually if needed:
    # clean(c); test(c); lint(c); format(c)
