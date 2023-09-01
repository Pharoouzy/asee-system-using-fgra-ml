import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
def evaluate_model(actual, predicted):
    mse = mean_squared_error(actual, predicted)
    rmse = mean_squared_error(actual, predicted, squared=False)
    mae = mean_absolute_error(actual, predicted)

    print("MSE:", mse)
    print("RMSE:", rmse)
    print("MAE:", mae)

    return {'mse': mse, 'rmse': rmse, 'mae': mae}
