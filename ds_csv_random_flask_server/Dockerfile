FROM python:3.11-slim

WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir \
    flask \
    numpy \
    pandas \
    pydantic \
    typing-extensions

# Expose the port used by Flask
EXPOSE 5000

CMD ["python", "main.py"]
