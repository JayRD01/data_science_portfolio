import pandas as pd
from abc import ABC, abstractmethod

class SingleValuesContract(ABC):
    def __init__(self, dataframe: pd.DataFrame):
        # Validation 1: Incorrect data type
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("Expected a pandas DataFrame as input.")

        # Validation 2: Empty DataFrame
        if dataframe.empty:
            raise ValueError("DataFrame is empty. Cannot compute correlations.")
        
        self.df = dataframe
        
    @abstractmethod
    def extract_rare_values(self) -> pd.DataFrame:
        raise NotImplementedError("Subclasses must implement the correlate_pairs method.")
        