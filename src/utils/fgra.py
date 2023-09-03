import numpy as np
import pandas as pd
import skfuzzy as fuzz

def fuzzyfication(data):
    # Define fuzzy membership functions.
    mfunc = fuzz.membership.gaussmf(data, np.mean(data), np.std(data))
    return mfunc

def rank_features(data, target):
    fuzzy_data = fuzzyfication(data)
    coefficients = grey_relational_coefficient(fuzzy_data, target)

    # Rank features based on coefficients
    ranked_features = np.argsort(-coefficients)
    return ranked_features


def grey_relational_coefficient(series, ref, rho=0.5):
    # rho is a distinguishing coefficient typically set between [0, 1]
    delta = abs(series - ref)
    max_delta = delta.max()
    min_delta = delta.min()

    return (min_delta + rho * max_delta) / (delta + rho * max_delta)

def grey_relational_coefficientz(fuzzy_data, target):
    # Compute the difference between each fuzzy data point and the target
    delta = np.abs(fuzzy_data - target)

    # Compute the grey relational coefficient
    coef = (np.min(delta) + np.min(delta) * 0.5) / (delta + np.min(delta) * 0.5)
    return coef

def normalize_data(data: pd.DataFrame):
    return (data - data.min()) / (data.max() - data.min())
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

def rank_featuresx(coefficients: pd.DataFrame):
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


# # from src.utils.fgra import rank_features
# #
# # ranked_features = rank_features(numeric_data.drop(columns=['Story_Point']), numeric_data['Story_Point'])
# # print(ranked_features)
#
# def c_grey_relational_coefficient(data, ref_seq, rho=0.5):
#     """
#     Compute the Grey Relational Coefficient for data against a reference sequence.
#     """
#     min_diff = np.min(np.abs(data - ref_seq))
#     max_diff = np.max(np.abs(data - ref_seq))
#     GRC = (min_diff + rho * max_diff) / (np.abs(data - ref_seq) + rho * max_diff)
#     return GRC
#
# # Normalize the data
# normalized_data = (numeric_data - numeric_data.min()) / (numeric_data.max() - numeric_data.min())
# ref_seq = normalized_data['Story_Point'].values
#
# # Calculate Grey Relational Coefficients for each feature
# grc_values = {}
# for column in normalized_data.columns:
#     if column != 'Story_Point':
#         grc_values[column] = np.mean(c_grey_relational_coefficient(normalized_data[column].values, ref_seq))
#
# # Sort features by Grey Relational Grade
# sorted_grc_values = dict(sorted(grc_values.items(), key=lambda item: item[1], reverse=True))
# # print(sorted(grc_values.items(), key=lambda item: item[1], reverse=True))
# sorted_grc_values
