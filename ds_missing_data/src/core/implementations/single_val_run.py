import pandas as pd
from src.core.contracts.single_val_contract import SingleValuesContract

class SingleValues(SingleValuesContract):
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe
        
    def extract_rare_values(self) -> pd.DataFrame:
        # Count all values (including NaNs) for each column
        df_counts = [self.df[col].value_counts(dropna=False) for col in self.df.columns]
        
        # Extract values that appear only once per column
        df_uniques = [df_unq[df_unq == 1].index.tolist() for df_unq in df_counts]
        
        # Build a list of dictionaries with column name and its rare values
        df_final = [
            {
                "column": col,
                "unique": val,
            }
            for col, uniques in zip(self.df.columns, df_uniques)
            for val in uniques
        ]
        cols = [col for col, vals in zip(self.df.columns, df_uniques) if vals]
        print("🔍 Rare value extraction complete.")
        print("🧹 Columns with at least one unique (non-repeating) value:")
        print(f"--->>>{cols}\n")
        print("📎 Reminder: Some columns may be omitted if no rare values were found.")
        print("🧪 For better visibility in Jupyter, use: display(dataframe)")
        dataframe = pd.DataFrame(df_final)
        
        """
        # Equivalent logic using traditional loops:
        rows = []
        for col in self.df.columns:
            df_counts = self.df[col].value_counts(dropna=False)
            df_uniques = df_counts[df_counts == 1].index.tolist()
            
            for val in df_uniques:
                rows.append({
                    "column": col,
                    "unique": val,
                })
                
        dataframe = pd.DataFrame(rows)
        """
        
        return dataframe