import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd
from src.core.contracts.corr_plotter_contract import CorrPlotterContract

class CorrPlotter(CorrPlotterContract):
    """Concrete implementation of CorrPlotterContract."""

    def __init__(self, df: pd.DataFrame):
        super().__init__(df)

    def plot(self, color: str = "red", show_median: bool = True) -> pd.DataFrame:
        """
        Generate a bar plot of correlations.

        Parameters
        ----------
        color : str, optional
            Color of the bars in the plot (default = 'red').
        show_median : bool, optional
            Whether to draw a horizontal line for the median correlation (default = True).

        Returns
        -------
        pd.DataFrame
            The DataFrame used for plotting.
        """
        df_plot = self._df.set_index(self._df["column1"] + self._df["column2"])

        ax = df_plot["correlation"].plot(kind="bar", figsize=(9, 3), color=color)

        if show_median:
            median = self._df["correlation"].median()
            ax.axhline(median, color="black", ls="--", label=f"Median: {median:.3f}")
            ax.legend(loc="upper right")

        ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.3f"))
        ax.set_xticklabels(df_plot.index, rotation=45, ha="right")
        ax.set_xlabel("")

        plt.tight_layout()
        plt.show()

        return self._df
