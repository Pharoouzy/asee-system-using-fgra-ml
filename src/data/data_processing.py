import pandas as pd
import numpy as np
def missing_value_statistics(data: pd.DataFrame) -> pd.DataFrame:
    # Identify columns with missing values and their respective percentages
    missing_data = data.isnull().sum()
    missing_percentage = (data.isnull().sum() / len(data)) * 100

    missing_df = pd.DataFrame({'Missing Values': missing_data, 'Percentage': missing_percentage})
    return missing_df[missing_df['Missing Values'] > 0].sort_values(by='Percentage', ascending=False)

def log_transform_outliers(data: pd.DataFrame, columns: list) -> pd.DataFrame:
    for col in columns:
        # Add a small constant to ensure all values are positive
        data[col] = data[col] + 1

        # Apply logarithmic transformation
        data[col] = np.log(data[col])

        return data
def save_processed_data(data: pd.DataFrame, filename: str) -> None:
    data.to_csv(filename, index=False)