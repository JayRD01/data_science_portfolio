from itertools import combinations
import pandas as pd
from abc import ABC, abstractmethod

class CorrColumnsContract(ABC):
    def __init__(self, df: pd.DataFrame):
        # Validation 1: Incorrect data type
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Expected a pandas DataFrame as input.")

        # Validation 2: Empty DataFrame
        if df.empty:
            raise ValueError("DataFrame is empty. Cannot compute correlations.")

        # Validation 3: Fewer than two numeric columns
        numeric_cols = df.select_dtypes(include=["number"]).columns
        if len(numeric_cols) < 2:
            raise ValueError("DataFrame must contain at least two numeric columns for correlation.")

        # Optional: store the validated DataFrame if needed in subclasses
        self._df = df

    @abstractmethod
    def correlate_pairs(self):
        # Enforces implementation in subclasses
        raise NotImplementedError("Subclasses must implement the correlate_pairs method.")
    
# 🧩 Contratos robustos con abstractismo (ABC)

# __init__ – Validaciones de entrada
# - if not isinstance(parametro, tipo_esperado) → TypeError
#   Evita tipos incorrectos desde el origen.
# - if parametro está vacío → ValueError
#   Impide instanciación con datos sin contenido.
# - if parámetro no cumple condiciones internas (ej. columnas válidas) → ValueError
#   Protege contra estructuras inválidas o insuficientes.

# Métodos decorados con @abstractmethod
# - raise NotImplementedError("Mensaje claro")
#   Obliga a implementar el método en subclases. Evita contratos incumplidos.