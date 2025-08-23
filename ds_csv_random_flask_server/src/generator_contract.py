import numpy as np 
import pandas as pd
from pydantic import BaseModel
from typing import Union
from abc import ABC, abstractmethod

# Immutable configuration model for data generation
class InfoContract(BaseModel):
    rows: int
    cols: int
    missingdata: Union[int, float]  # Percentage or count of missing values

    class Config():
        frozen = True             # Makes the model immutable (read-only)

class generatorContract(ABC):

    @abstractmethod
    def random_gen(self) -> np.ndarray:
        # Should return a NumPy array with random data
        pass

    @abstractmethod
    def dataframe_gen(self) -> pd.DataFrame:
        # Should return a Pandas DataFrame and optionally handle saving
        pass
