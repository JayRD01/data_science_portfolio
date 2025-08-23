import os
from src.generator_run import generatorBuilder
from src.generator_contract import InfoContract
from src.server_run import ServerFlask

def main() -> None:
    # STEP 1: Define file path
    file_path: str = os.path.join(os.getcwd(), "data", "random_data.csv")

    # STEP 2: Attempt to delete old file (avoid TOCTOU vulnerability)
    try:
        os.remove(file_path)
        print("🗑️  Old CSV file has been removed.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"⚠️  File cleanup skipped: {e}")

    # STEP 3: Create data generator config
    config: InfoContract = InfoContract(rows=100_000, cols=6, missingdata=0.2)

    # STEP 4: Generate new CSV data
    generator = generatorBuilder(random=config)
    generator.dataframe_gen()
    print(f"✅ Data successfully generated at: {file_path}")

    # STEP 5: Launch the singleton server to serve the file
    folder: str = os.path.dirname(file_path)
    filename: str = os.path.basename(file_path)
    server = ServerFlask(folder, filename)
    server.run()  # blocks execution until server is shut down

if __name__ == "__main__":
    main()
