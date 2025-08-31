from src.core.contracts.sample_contract import SampleContract
import pandas as pd

class SampleDF(SampleContract):
    """
    Utility class to work with sample DataFrames.

    Behavior:
    - If only_sample=True → returns a sample DataFrame.
    - If only_sample=False → randomly checks values from each column 
      to ensure they match the declared dtype.
    """
    def __init__(self,df: pd.DataFrame, pct: int = 0.99, only_sample: bool = False):
        self._df: pd.DataFrame = df
        self.pct: int = pct
        self.only_sample: bool = only_sample
        
    def sample_dtype(self):
        sample = self._df.sample(frac=self.pct, random_state=42)
        if self.only_sample:
            return sample
        data = {}
        
        for col in sample.columns:
            type_counts = {}
            for val in sample[col]:
                t = type(val).__name__ # gets the actual Python type of each cell, not the general pandas dtype of the column
                type_counts[t] = type_counts.get(t, 0) + 1
                data[col] = type_counts
        dataframe = pd.DataFrame(data).reset_index(names="dtype  ->")
        return dataframe