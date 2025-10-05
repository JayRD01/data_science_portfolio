import pandas as pd
import numpy as np
from src.core.contracts.shadow_imputer import ShadowImputerContract

class ShadowImputer(ShadowImputerContract):
    def __init__(self, column: pd.Series, 
                 proportion_below: float = 0.10,
                 jitter: float = 0.070,
                 seed: int = 42):
        self.column = column
        self.proportion_below = proportion_below
        self.jitter = jitter
        self.seed = seed
    
    def fill_with_dummies(self):
        data = self.column.copy(deep=True)
        mask = data.isna()
        n_missing = mask.sum()
        
        np.random.seed(self.seed)
        col_range = data.max() - data.min()
        col_shift = data.min() - (data.min() * self.proportion_below)
        col_jitter = (np.random.random(n_missing)-2) * col_range * self.jitter
        
        data[mask] = col_shift + col_jitter
        
        return data
        
    