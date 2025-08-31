import pandas as pd
from src.core.contracts.null_report_contract import NullReportContract


class NullReport(NullReportContract):
    def __init__(self, pandas_obj: pd.DataFrame):
        self._df = pandas_obj

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
                n_unique=lambda s: s["variable"].map(lambda col: df[col].nunique()), #unique() -> array. nunique() -> sum of uniques
                common_variables=lambda s: s["variable"].map(lambda col: df[col].value_counts().idxmax()),
                pct_missing=lambda s: (s["n_missing"] / s["n_cases"]) * 100,
                dtype=lambda s: s["variable"].map(lambda col: df[col].dtype)
            )
        )
        return summary