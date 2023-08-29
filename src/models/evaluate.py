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
