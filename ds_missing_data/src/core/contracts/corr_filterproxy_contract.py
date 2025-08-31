from abc import ABC, abstractmethod
import pandas as pd

class CorrFilterProxyContract(ABC):
    """Contract for correlation filter proxies."""

    def __init__(self, df: pd.DataFrame):
        # Input validations
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Expected a pandas DataFrame as input.")
        if df.empty:
            raise ValueError("DataFrame is empty. Cannot filter correlations.")
        required_cols = {"column1", "column2", "correlation"}
        if not required_cols.issubset(df.columns):
            raise ValueError(f"DataFrame must contain columns: {required_cols}")

        self._df = df

    @abstractmethod
    def filter(self, pct_filter_col: float = None) -> pd.DataFrame:
        """
        Returns a validated correlation DataFrame.

        Parameters
        ----------
        pct_filter_col : float, optional
            Minimum correlation expressed as a percentage (e.g., 70 = 0.70).
            If None, no percentage filter is applied.

        Returns
        -------
        pd.DataFrame
            The correlation DataFrame, optionally filtered.
        """
        raise NotImplementedError("Subclasses must implement the filter method.")
