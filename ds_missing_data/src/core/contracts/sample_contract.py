from abc import ABC, abstractmethod
import pandas as pd


class SampleContract(ABC):
    def __init__(self,df: pd.DataFrame, pct: int, only_sample: bool = False):
        self.df: pd.DataFrame = df
        self.pct: int = pct
        self.only_sample: bool = only_sample
        
    @abstractmethod       
    def sample_dtype(self):
        """
        Utility class to work with sample DataFrames.

        Behavior:
        - If only_sample=True → returns a sample DataFrame.
        - If only_sample=False → randomly checks values from each column 
            to ensure they match the declared dtype.
        """
        pass