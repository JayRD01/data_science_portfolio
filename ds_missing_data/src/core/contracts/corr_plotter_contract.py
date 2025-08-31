from abc import ABC, abstractmethod
import pandas as pd

class CorrPlotterContract(ABC):
    """Contract for correlation plotters."""

    def __init__(self, df: pd.DataFrame):
        # Input validations
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Expected a pandas DataFrame as input.")
        if df.empty:
            raise ValueError("DataFrame is empty. Nothing to plot.")
        required_cols = {"column1", "column2", "correlation"}
        if not required_cols.issubset(df.columns):
            raise ValueError(f"DataFrame must contain columns: {required_cols}")

        self._df = df

    @abstractmethod
    def plot(self, color: str = "red", show_median: bool = True) -> pd.DataFrame:
        """
        Abstract method to generate a correlation bar plot.

        Parameters
        ----------
        color : str, optional
            Color of the bars in the plot.
        show_median : bool, optional
            Whether to display the median correlation line.

        Returns
        -------
        pd.DataFrame
            The DataFrame used for plotting.
        """
        raise NotImplementedError("Subclasses must implement the plot method.")
