import pandas as pd
from src.core.contracts.null_report_contract import NullReportContract

print(">>> registering accessor 'missing'")


class NullReportImpl(NullReportContract):
    """Concrete implementation of the missing values report."""

    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)

    def summary(self) -> pd.DataFrame:
        df = self._df
        summary = (
            df.isna()
            .sum()
            .reset_index(name="n_missing")
            .rename(columns={"index": "variable"})
            .assign(
                missing_flag=lambda s: s["n_missing"].map(lambda col: 1 if col > 0 else 0),
                n_cases=lambda s: s["variable"].map(lambda col: df[col].size),
                n_unique=lambda s: s["variable"].map(lambda col: df[col].nunique()),
                most_common_value=lambda s: s["variable"].map(
                    lambda col: df[col].value_counts().idxmax() if df[col].notna().any() else None
                ),
                pct_missing=lambda s: (s["n_missing"] / s["n_cases"]) * 100,
                dtype=lambda s: s["variable"].map(lambda col: df[col].dtype),
            )
        )
        return summary


@pd.api.extensions.register_dataframe_accessor("missing")
class MissingAccessor:
    """Pandas accessor exposing the NullReportImpl via df.missing."""

    def __init__(self, pandas_obj: pd.DataFrame):
        self._impl = NullReportImpl(pandas_obj)

    def summary(self) -> pd.DataFrame:
        return self._impl.summary()
