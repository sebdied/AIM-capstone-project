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

def get_threshold(col_name: str) -> int | None:
    # Thresholds for each toxin by 'WHO Air Quality Guidlines (AQG)' or 'European Environment Agency (EEA)' - 'None' if no threshold is defined yet
    # Source of comment behind each toxin: https://archive.ics.uci.edu/dataset/360/air+quality
    thresholds: dict = {
        'CO(GT)': 4,            # True hourly averaged concentration CO in mg/m^3                                   - WHO AQG page: 134
        'NMHC(GT)': None,       # True hourly averaged overall Non Metanic HydroCarbons concentration in microg/m^3 - No threshold defined yet
        'C6H6(GT)': 5,          # True hourly averaged Benzene concentration in microg/m^3                          - EEA homepage
        'NOx(GT)': None,        # True hourly averaged NOx concentration in ppb                                     - No threshold defined yet
        'NO2(GT)': 10,          # True hourly averaged NO2 concentration in microg/m^3                              - WHO AQG page: 116
        'PT08.S5(O3)': 60      # Hourly averaged sensor response (nominally O3 targeted)                            - WHO AQG page: 136
    }
    if col_name in thresholds:
        return thresholds[col_name]
    else:
        return None

def get_label(col_name: str) -> int | None:
    # Feature labels
    labels: dict = {
        'Date': 'Date (dd/mm/yyyy)',
        'Time': 'Time (hh.mm.ss)',
        'CO(GT)': 'CO concencration in mg/m^3',
        'PT08.S1(CO)': 'Hourly averaged sensor response (nominally CO targeted)',
        'NMHC(GT)': 'Non Metanic HydroCarbons concentration in microg/m^3',
        'C6H6(GT)': 'Benzene concentration in microg/m^3',
        'PT08.S2(NMHC)': 'Hourly averaged sensor response (nominally NMHC targeted)',
        'NOx(GT)': 'NOx concentration in ppb ',
        'PT08.S3(NOx)': 'Hourly averaged sensor response (nominally NOx targeted)',
        'NO2(GT)': 'NO2 concentration in microg/m^3 ',
        'PT08.S4(NO2)': 'Hourly averaged sensor response (nominally NO2 targeted)',
        'PT08.S5(O3)': 'Ozon (O3)',
        'T': 'Temperature (°C)',
        'RH': 'Relative Humidity (%)',
        'AH': 'Absolute Humidity',
        'Month': 'Month',
        'HourOfDay': 'Hour of the day'
    }
    if col_name in labels:
        return labels[col_name]
    else:
        return None

def get_label_short(col_name: str) -> int | None:
    # Feature labels for graphs (shorter vesions)
    labels_short: dict = {
        'Date': 'Date',
        'Time': 'Time',
        'CO(GT)': 'CO',
        'PT08.S1(CO)': 'CO',
        'NMHC(GT)': 'Non Metanic HydroCarbons',
        'C6H6(GT)': 'Benzene',
        'PT08.S2(NMHC)':'Non Metanic HydroCarbons',
        'NOx(GT)': 'NOx',
        'PT08.S3(NOx)': 'NOx',
        'NO2(GT)': 'NO2',
        'PT08.S4(NO2)': 'NO2',
        'PT08.S5(O3)': 'Ozon',
        'T': '°C',
        'RH': 'Humidity (%)',
        'AH': 'Abs. Humidity',
        'HourOfDay': 'Hour'
    }
    if col_name in labels_short:
        return labels_short[col_name]
    else:
        return None
