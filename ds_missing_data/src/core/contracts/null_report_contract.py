from abc import ABC, abstractmethod
import pandas as pd

class NullReportContract(ABC):
    def __init__(self, dataframe: pd.DataFrame):
        self._df = dataframe

    @abstractmethod
    def summary(self) -> pd.DataFrame:
        """Return a report with missing data"""
        pass