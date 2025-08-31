from abc import ABC, abstractmethod
import pandas as pd


class NullReportContract(ABC):
    """Contract for missing values reporting classes."""

    def __init__(self, dataframe: pd.DataFrame):
        self._df = dataframe

    @abstractmethod
    def summary(self) -> pd.DataFrame:
        """Return a DataFrame with a missing values report."""
        pass
