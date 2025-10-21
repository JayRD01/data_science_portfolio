import threading
import logging
from src.core.implementations.run_insert import run_insert
from src.core.implementations.run_get_all import run_get_all
from src.core.implementations.run_update import run_update
from src.core.implementations.run_delete import run_delete


# 🔧 Configure logging globally
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | %(threadName)s | %(message)s"
)


if __name__ == "__main__":
    logging.info("🚀 Launching concurrent database operations...")

    # 🧵 Create one thread for each DB task
    threads = [
        threading.Thread(target=run_insert, name="InsertThread"),
        threading.Thread(target=run_get_all, name="GetAllThread"),
        threading.Thread(target=run_update, name="UpdateThread"),
        threading.Thread(target=run_delete, name="DeleteThread"),
    ]

    # ▶️ Start all threads
    for t in threads:
        t.start()

    # ⏳ Wait for all threads to complete
    for t in threads:
        t.join()

    logging.info("🎯 All concurrent tasks completed.")
