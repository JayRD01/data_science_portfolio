import pandas as pd
from src.core.contracts.null_report_contract import NullReportContract
from src.core.implementations.correlation_columns_run import CorrColumns

print(">>> registering accessor 'missing'")

class NullReportImpl(NullReportContract):
    """Concrete implementation of the missing values report."""

    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)

    def summary(self) -> pd.DataFrame:
        df = self._df

        # Instantiate correlation helper
        correlation = CorrColumns(df=df)
        df_pairs = correlation.correlate_pairs()
        df_top5 = correlation.corr_top(top_n=5)

        # Build summary table with enriched column-level statistics
        summary = (
            df.isna()
            .sum()
            .reset_index(name="n_missing")
            .rename(columns={"index": "variable"})
            .assign(
                missing=lambda s: s["n_missing"].map(lambda col: 1 if col > 0 else 0),
                n_cases=lambda s: s["variable"].map(lambda col: df[col].size),
                n_unique=lambda s: s["variable"].map(lambda col: df[col].nunique()),

                # Round most common value if it's numeric
                common_value=lambda s: s["variable"].map(
                    lambda col: round(df[col].value_counts().idxmax(), 4)
                    if df[col].notna().any() and isinstance(df[col].value_counts().idxmax(), (int, float))
                    else df[col].value_counts().idxmax() if df[col].notna().any()
                    else None
                ),

                max_n=lambda s: s["variable"].map(lambda col: df[col].max()).round(4),
                median=lambda s: s["variable"].map(lambda col: df[col].mean()).round(4),
                min_n=lambda s: s["variable"].map(lambda col: df[col].min()).round(4),
                range_n=lambda s: s["variable"].map(lambda col: df[col].max() - df[col].min()).round(4),

                # Percentage of missing values
                pct_missing=lambda s: ((s["n_missing"] / s["n_cases"]) * 100).round(4),

                is_const=lambda s: s["n_unique"].map(lambda x: x == 1),
                is_numeric=lambda s: s["variable"].map(lambda col: pd.api.types.is_numeric_dtype(df[col])),

                # Flag if variable is among top correlated columns
                high_correlation=lambda s: s["variable"].map(
                    lambda col: col in df_top5.columns.to_list()
                ),

                dtype=lambda s: s["variable"].map(lambda col: df[col].dtype)
            )
        )

        print("To visualize correlation plots, refer to:")
        print("correlation_columns_run.py, corr_filterproxy_run.py, and corr_plotter_run.py")
        print("If you're using a Jupyter notebook, run this with display(summary)")

        return summary


@pd.api.extensions.register_dataframe_accessor("missing")
class MissingAccessor:
    """Pandas accessor exposing the NullReportImpl via df.missing."""

    def __init__(self, pandas_obj: pd.DataFrame):
        self._impl = NullReportImpl(pandas_obj)

    def summary(self) -> pd.DataFrame:
        return self._impl.summary()