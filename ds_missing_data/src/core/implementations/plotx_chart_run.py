import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from src.core.contracts.null_report_contract import NullReportContract
from src.core.contracts.plotx_chart_contract import PlotxChartContract

# Implements a charting class based on the PlotxChartContract interface
class PlotxChart(PlotxChartContract):
    def __init__(self, df_summary: pd.DataFrame):
        # Store the summary DataFrame containing missing value info
        self.df = df_summary
        
    def pct_missing_chart(self):
        # Create a horizontal bar-style plot showing missing values per variable
        fig, ax = plt.subplots()
        
        # Define y-axis positions for each variable
        plot_range = range(1, len(self.df.index) + 1)
        # Extract the number of missing values for each variable
        xmax_values = np.array(self.df['n_missing'])

        # Draw horizontal lines from 0 to the number of missing values
        ax.hlines(y=plot_range, xmin=0, xmax=xmax_values, color="black")
        # Add circular markers at the end of each line
        ax.plot(xmax_values, plot_range, "o", color="black")

        # Label y-axis with variable names
        ax.set_yticks(plot_range)
        ax.set_yticklabels(self.df['variable'])
        # Label x and y axes
        ax.set_xlabel("Missing_values")
        ax.set_ylabel("Variables")
        # Add horizontal grid lines for readability
        ax.grid(axis="y")
        plt.show()
        
    def matrix_missing_chart(self, 
                             only_missing: bool = False, 
                             only_table: bool = False, 
                             x: str = None, y: str = None):
        if only_missing:
            df_na = self.df[self.df.isna().any(axis=1)].isna()
        else: 
            df_na = self.df.isna()
            
        df_na = df_na.replace({
            True: 'Missing',
            False: 'No_missing'
            }).add_suffix('_NA')
        
        matrix_df = pd.concat([self.df, df_na], axis='columns')
        if only_table:
            return matrix_df
        
        elif not only_table:
            matrix_df_chart = matrix_df.pipe(
                lambda df: sns.boxenplot(
                    data=df,
                    x=x,
                    y=y
                ))
            return matrix_df_chart
        

        
@pd.api.extensions.register_dataframe_accessor("plotx")
class MissingAccessor:
    def __init__(self, pandas_obj: pd.DataFrame):
        self._obj = pandas_obj
        self._impl = PlotxChart(self._obj)

    def pct_missing_chart(self, **kwargs):
        return self._impl.pct_missing_chart(**kwargs)

    def matrix_missing_chart(self, **kwargs):
        return self._impl.matrix_missing_chart(**kwargs)
