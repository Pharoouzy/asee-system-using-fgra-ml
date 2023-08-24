import numpy as np
import pandas as pd

def advanced_normalization(X):
    """
    Normalize the data to the range [0, 1]. If a feature/column has zero variance (i.e., max = min),
    set it to 0.5 (midway between 0 and 1) as it doesn't provide any informative power.
    """
    X_min = np.min(X, axis=0)
    X_max = np.max(X, axis=0)
    X_range = X_max - X_min

    # Identify columns with zero variance and set their range to 1 to avoid division by zero.
    zero_variance_cols = X_range == 0
    X_range[zero_variance_cols] = 1

    normalized_X = (X - X_min) / X_range

    # Set columns with zero variance to 0.5
    normalized_X[:, zero_variance_cols] = 0.5
    return normalized_X

def normalize_data(data: pd.DataFrame, target_col: str):
    # Exclude date columns for GRA
    data_for_gra = data.select_dtypes(include=[float, int])

    # Normalize the Data
    normalized_data = (data_for_gra - data_for_gra.min()) / (data_for_gra.max() - data_for_gra.min())

    # Calculate the Difference Sequence
    delta = np.abs(normalized_data.subtract(normalized_data[target_col], axis=0))

    return delta

def compute_grey_relational_coefficients(data, target_col, zeta=0.5):
    # Compute the Grey Relational Coefficients
    min_delta = delta.min()
    max_delta = delta.max()
    coefficients = (min_delta + zeta * max_delta) / (delta + zeta * max_delta)

    # Drop the target column as we don't need its relational coefficient with itself
    coefficients = coefficients.drop(columns=[target_col])

    return coefficients

def rank_features(coefficients: pd.DataFrame):
    # 4. Rank the Features based on average coefficient
    ranked_features = coefficients.mean().sort_values(ascending=False)

    return ranked_features
def grey_relational_analysis(data, target_col, zeta=0.5):
    """
    Perform Grey Relational Analysis on the dataset with respect to the target column.

    Parameters:
    - data: DataFrame containing the features and target.
    - target_col: Name of the target column.
    - zeta: Distinguishing coefficient, default is 0.5.

    Returns:
    - A Series containing the average grey relational coefficient for each feature, sorted in descending order.
    """
    # Exclude date columns for GRA
    data_for_gra = data.select_dtypes(include=[float, int])

    # 1. Normalize the Dataset
    normalized_data = (data_for_gra - data_for_gra.min()) / (data_for_gra.max() - data_for_gra.min())

    # 2. Calculate the Difference Sequence
    delta = np.abs(normalized_data.subtract(normalized_data[target_col], axis=0))

    # 3. Compute the Grey Relational Coefficients
    min_delta = delta.min()
    max_delta = delta.max()
    coefficients = (min_delta + zeta * max_delta) / (delta + zeta * max_delta)

    # Drop the target column as we don't need its relational coefficient with itself
    coefficients = coefficients.drop(columns=[target_col])

    # 4. Rank the Features based on average coefficient
    ranked_features = coefficients.mean().sort_values(ascending=False)

    return ranked_features
