# 🧪 DS CSV Generator with Flask

This project is a simple and professional demonstration of how to generate synthetic CSV datasets using `NumPy` and `Pandas`, then serve them via a lightweight `Flask` API. It uses clean software architecture patterns including **Singleton** and **Decorator** to maintain modularity and production-readiness.

---

## 🧠 Tech Stack

- **Python 3.12+**
- **NumPy / Pandas** for data generation
- **Flask** as the micro web framework
- **Pydantic** for type-safe configuration
- **Docker** ready setup
- **Design Patterns**: Singleton + Decorator

---

## 📁 Project Structure

```
ds_csv_generator_with_flask/
├── Dockerfile
├── environment.yml
├── main.py
├── data/
│   └── random_data.csv         # Auto-generated on startup
├── src/
│   ├── generator_contract.py   # Abstract contract for data generation
│   ├── generator_run.py        # Random CSV generator logic
│   ├── server_run.py           # Flask server (Singleton)
│   └── singleton_contract.py   # Thread-safe Singleton decorator class
```

---

## ⚙️ How it Works

1. `main.py` starts by **deleting any old CSV** (safely).
2. Uses `generatorBuilder` to **create a random DataFrame**.
3. The DataFrame is saved to `data/random_data.csv`.
4. A singleton `ServerFlask` instance is created to **serve the CSV** via `/csv`.

---

## 🧩 Design Patterns Used

### ✅ Singleton
Ensures only one instance of `ServerFlask` or any other singleton-enabled class exists, even in multithreaded scenarios.

### ✅ Decorator
The `SingletonContract` is implemented as a **class-based decorator** that checks for type safety and thread safety.

---

## 🚀 Running Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Or use conda
conda env create -f environment.yml
conda activate ds-csv-flask

# Run the app
python main.py
```

Then visit: [http://localhost:8080/csv](http://localhost:8080/csv)

---

## 🐳 Running with Docker

```bash
docker build -t ds-csv-server .
docker run -p 8080:8080 ds-csv-server
```

---

## 🤝 Author

**JayRD01** - [GitHub](https://github.com/JayRD01)

This repository is part of the `data_science_portfolio` project.