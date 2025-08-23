# Use Python 3.12 to match conda env
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libatlas-base-dev \
    gfortran \
    libhdf5-dev \
    libgl1 \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Install Python packages
RUN pip install --no-cache-dir \
    ipykernel \
    jupyterlab \
    notebook \
    ipywidgets \
    numpy \
    pandas \
    xarray \
    pyjanitor \
    tables \
    scipy \
    statsmodels \
    sympy \
    scikit-learn \
    matplotlib \
    seaborn \
    plotly \
    missingno \
    pandas-flavor \
    fs \
    pyprojroot \
    sweetviz \
    ydata-profiling \
    tqdm \
    loguru \
    rich
