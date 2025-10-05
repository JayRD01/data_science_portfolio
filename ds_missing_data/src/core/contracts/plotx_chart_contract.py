from src.core.contracts.null_report_contract import NullReportContract
from abc import ABC, abstractmethod
import pandas as pd

class PlotxChartContract(ABC):
    def __init__(self, df_summary: NullReportContract):
        # Validation 1: Incorrect data type
        if not isinstance(df_summary, pd.DataFrame):
            raise TypeError("Expected a pandas DataFrame as input.")

        # Validation 2: Empty DataFrame
        if df_summary.empty:
            raise ValueError("DataFrame is empty. Cannot compute correlations.")

        # Optional: store the validated DataFrame if needed in subclasses
        self._df = df_summary
        
    @abstractmethod
    def pct_missing_chart(self):
        # Enforces implementation in subclasses
        raise NotImplementedError("Subclasses must implement the correlate_pairs method.")
    
    @abstractmethod
    def matrix_missing_chart(self):
        raise NotImplementedError("Subclasses must implement the matrix_missing_chart method.")
    
       
