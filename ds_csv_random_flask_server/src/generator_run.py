import numpy as np 
import pandas as pd
from .generator_contract import generatorContract, InfoContract
import os

class generatorBuilder(generatorContract):
    def __init__(self, random: InfoContract = None):
        # Stores the configuration for random data generation (rows, cols)
        self.random = random

    def random_gen(self) -> np.ndarray:
        # Generates a 2D NumPy array with random values between 0 and 1
        data = np.random.random((self.random.rows, self.random.cols))
        return data

    def dataframe_gen(self) -> pd.DataFrame:
        data = self.random_gen() # Generate the raw random data
        col_names = [f"Column{i+1}" for i in range(self.random.cols)] # Create column names dynamically: Column1, Column2, ..., ColumnN
        df = pd.DataFrame(data, columns=col_names)
        data_path = os.path.join(os.getcwd(), "data", "random_data.csv")

        # Save the DataFrame to CSV without the index column
        df.to_csv(data_path, index=False)
        return df
