import pandas as pd
from src.core.contracts.corr_filterproxy_contract import CorrFilterProxyContract

class CorrFilterProxy(CorrFilterProxyContract): 
    def filter(self, pct_filter_col: float = None) -> pd.DataFrame:
        """
        Returns the correlation DataFrame, optionally filtering by a minimum percentage.
        
        Parameters
        ----------
        pct_filter_col : float, optional
            Minimum correlation expressed as percentage (e.g., 70 = 0.70).
        """
        df_filtered = self._df.copy()

        if pct_filter_col:
            min_corr = pct_filter_col / 100
            df_filtered = df_filtered[df_filtered["correlation"] > min_corr]

        return df_filtered.reset_index(drop=True)
