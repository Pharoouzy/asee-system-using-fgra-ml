import numpy as np
import pandas as pd
import skfuzzy as fuzz

def fuzzification(data: pd.DataFrame):
    # Define fuzzy membership functions.
    mfunc = fuzz.membership.gaussmf(data, np.mean(data), np.std(data))
    return mfunc

def rank_features(data: pd.DataFrame, target: str):
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

def normalize_data(data: pd.DataFrame):
    # Exclude date columns for GRA
    data_for_gra = data.select_dtypes(include=[float, int])

    # Normalize the Data
    normalized_data = (data_for_gra - data_for_gra.min()) / (data_for_gra.max() - data_for_gra.min())
    target_col = 'Story_Point'
    # Calculate the Difference Sequence
    delta = np.abs(normalized_data.subtract(normalized_data[target_col], axis=0))

    return delta
