import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def missing_value_statistics(data: pd.DataFrame) -> pd.DataFrame:
    # Identify columns with missing values and their respective percentages
    missing_data = data.isnull().sum()
    missing_percentage = (data.isnull().sum() / len(data)) * 100

    missing_df = pd.DataFrame({'Missing Values': missing_data, 'Percentage': missing_percentage})
    return missing_df[missing_df['Missing Values'] > 0].sort_values(by='Percentage', ascending=False)

def log_transform_outliers(data: pd.DataFrame, columns: list) -> pd.DataFrame:
    for column in columns:
        # Add a small constant to ensure all values are positive
        data[column] = data[column] + 1

        # Apply logarithmic transformation
        data[column] = np.log(data[column])
        data[column] = np.log(data[column])

        return data
def save_processed_data(data: pd.DataFrame, filename: str) -> None:
    data.to_csv(filename, index=False)

def remove_duplicates(data: pd.DataFrame) -> None:
    # Check for duplicates before removal
    initial_length = len(data)

    # Remove duplicate rows
    data.drop_duplicates(inplace=True)

    # Check how many duplicate rows were removed
    removed_duplicates = initial_length - len(data)
    print(f'Duplicate rows: {removed_duplicates}')

def identify_outliers(data: pd.DataFrame, columns: list) -> dict:
    outliers_stats = {}
    for column in columns:
        # Identify outliers for each column using the IQR method
        # Calculate Q1 and Q3
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)

        # Compute IQR
        IQR = Q3 - Q1

        # Determine bounds for outliers
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Identify the outliers
        outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]

        # Percentage of data that are outliers
        outliers_percentage = (len(outliers) / len(data)) * 100
        outliers_stats[column] = outliers_percentage
        print(f'{column}: {outliers_percentage}')

    return outliers_stats

def assess_unique_values(data: pd.DataFrame, columns: list) -> pd.DataFrame:
    # Check the number of unique values in potential categorical columns
    unique_values = data[columns].nunique()

    return unique_values

def encode_labels(data: pd.DataFrame, columns_to_encode: list) -> dict:
    # Apply label encoding
    label_encoders = {}
    encoded_data = {}
    for col in columns_to_encode:
        le = LabelEncoder()
        encoded_data[col] = le.fit_transform(data[col])
        label_encoders[col] = le  # store the encoder for potential use later

    return encoded_data