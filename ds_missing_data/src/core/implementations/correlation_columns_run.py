from itertools import combinations
import pandas as pd
from src.core.contracts.correlation_columns_contract import CorrColumnsContract

class CorrColumns(CorrColumnsContract):
    def __init__(self, df: pd.DataFrame):
        """
        Initialize with a DataFrame.
        """
        self._df: pd.DataFrame = df
        self.output: list = []

    def correlate_pairs(self) -> pd.DataFrame:
        """
        Compute pairwise correlations between numeric columns.
        """
        self.output = []  # Reset to avoid accumulation
        cols = self._df.select_dtypes(include=["number"]).columns

        for c1, c2 in combinations(cols, 2):
            corr = self._df[c1].corr(self._df[c2])
            self.output.append([c1, c2, corr])
            
        dataframe = pd.DataFrame(self.output, columns=["column1", "column2", "correlation"])

        return dataframe

    def corr_top(self, top_n: int = 5) -> pd.DataFrame:
        """
        Return a DataFrame with the top N most correlated column pairs.
        """
        df_top = self.correlate_pairs()
        df_copy = self._df.copy()

        # Get top N pairs by correlation value
        top_pairs = df_top.sort_values(by="correlation", ascending=False).head(top_n).sort_index()

        # Flatten and deduplicate column names
        top = pd.concat([top_pairs["column1"], top_pairs["column2"]], axis=0)
        cols = [col for i, col in enumerate(top) if col not in top[:i].values]

        return df_copy[cols].copy()