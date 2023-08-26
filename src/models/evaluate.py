import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
def evaluate_model(actual, predicted):
    mse = mean_squared_error(actual, predicted)
    rmse = mean_squared_error(actual, predicted, squared=False)
    mae = mean_absolute_error(actual, predicted)
    r2 = r2_score(actual, predicted)

    print("MSE:", mse)
    print("RMSE:", rmse)
    print("MAE:", mae)
    print("R2:", r2)

    return {'mse': mse, 'rmse': rmse, 'mae': mae, 'r2': r2}

def MRE(actual, predicted):
    return abs((actual - predicted) / actual)

def MMRE(actual, predicted):
    return np.mean(abs((actual - predicted) / actual))

def PRED(actual, predicted, k):
    mre_values = MRE(actual, predicted)
    return np.mean(mre_values <= (k / 100.0))

def SA(actual, predicted):
    mae = np.mean(abs(actual - predicted))
    return 1 - (mae / np.std(actual))

def MBRE(actual, predicted):
    return np.median(abs((actual - predicted) / actual))

def MIBRE(actual, predicted):
    return np.mean(abs((actual - predicted) / (actual + predicted)))

def MAPE(actual, predicted):
    return np.mean(np.abs((actual - predicted) / y_test)) * 100