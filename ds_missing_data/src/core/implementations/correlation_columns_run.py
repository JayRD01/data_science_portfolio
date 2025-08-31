from itertools import combinations
import pandas as pd
from src.core.contracts.correlation_columns_contract import CorrColumnsContract

class CorrColumns(CorrColumnsContract):
    def __init__(self, df: pd.DataFrame):
        self._df: pd.DataFrame = df
        self.output: list = []
        
    def correlate_pairs(self):
        cols = self._df.select_dtypes(include=["number"]).columns

        for c1, c2 in combinations(cols, 2):
            corr = (self._df[c1].corr(self._df[c2]))
            self.output.append([c1, c2, corr])
    
        dataframe = pd.DataFrame(self.output, columns=["column1", "column2", "correlation"])
        return dataframe