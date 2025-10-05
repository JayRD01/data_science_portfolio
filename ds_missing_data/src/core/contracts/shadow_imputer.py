import pandas as pd
import numpy as np
from abc import ABC, abstractmethod

class ShadowImputerContract(ABC):
    """
    Abstract base class for imputing missing values using synthetic data
    generated below the minimum observed value with added jitter.

    Parameters:
    ----------
    column : pd.Series
        The input data column containing missing values.
    proportion_below : float
        Proportion below the minimum value to shift synthetic values.
    jitter : float
        Amount of random noise to add to synthetic values.
    seed : int
        Random seed for reproducibility.
    """

    def __init__(self, column: pd.Series, 
                 proportion_below: float,
                 jitter: float,
                 seed: int):
        self._validate_inputs(column, proportion_below)
        self.column = column.copy(deep=True)
        self.proportion_below = proportion_below
        self.jitter = jitter
        self.seed = seed

    def _validate_inputs(self, column, proportion_below):
        # Type checks
        if not isinstance(column, pd.Series):
            raise TypeError("Expected a pandas Series as input.")
        if not isinstance(proportion_below, float):
            raise TypeError("Expected a float for 'proportion_below'.")
        
        # Content checks
        if column.empty:
            raise ValueError("Input Series cannot be empty.")

    @abstractmethod
    def fill_with_dummies(self) -> pd.Series:
        """
        Abstract method to be implemented by subclasses.
        Should return a Series with missing values imputed.
        """
        pass