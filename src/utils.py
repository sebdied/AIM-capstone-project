# Standard imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Distribution plotting
def plot_distributions(df: pd.DataFrame, column: str, figsize=(15, 5)):
    # Plot distributions
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()


# Analyse data distribution and neg. values of a column
def analyze_col(df: pd.DataFrame, col_name: str, convert_dtype_to_float: bool):
    print(f"# Column name: {col_name}")
    if col_name in df.columns:
        # Types in column
        print(f'Types found ({col_name}): {df[col_name].dtypes}')
        # Try to convert dtype to float to check for neg. values
        if convert_dtype_to_float is True:
            try:
                # Convert the column to numeric, handling errors
                # Replace ',' with '.' if necessary and convert to float
                col_to_float = f'{col_name}_to_float'
                df[col_to_float] = df[col_name].str.replace(',', '.', regex=False).astype(float)
                print(f'Types found ({col_to_float}): {df[col_to_float].dtypes}')
                # Count of neg. values
                print(f'Neg. values ({col_to_float}): {(df[col_to_float] < 0).sum()}')
                # Plot distribution
                plot_distributions(df, col_to_float, (15, 5))
            except Exception as ex:
                print(f"Could not convert column-dtype to float: {ex}")
        else:
            # Count of neg. values
            print(f'Neg. values ({col_name}): {(df[col_name] < 0).sum()}')
            # Plot distribution
            plot_distributions(df, [col_name], (15, 5))
