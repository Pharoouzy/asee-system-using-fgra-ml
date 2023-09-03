from sklearn.model_selection import GridSearchCV
from src.utils.visualization import plot_actual_vs_predicted, plot_residual

def optimize_model(model_name, model, X_train, y_train, X_test, y_test):
    # Define the hyperparameters and their possible values
    param_grid = {
        'n_estimators': [50, 100, 150],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }

    # Initialize the Random Forest Regressor
    # model = RandomForestRegressor(random_state=42)

    # Initialize GridSearchCV
    grid_search = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        cv=3,
        n_jobs=-1,
        verbose=2,
        scoring='neg_mean_squared_error'
    )

    # Fit to the data
    grid_search.fit(X_train, y_train)

    # Get the best parameters
    best_params = grid_search.best_params_

    print("Best parameters:")
    print(best_params)

    # Evaluate the model with the best parameters
    best = grid_search.best_estimator_
    y_pred_best = best.predict(X_test)

    print(f'Optimized {model_name} Metrics:')
    optimized_model_metrics = evaluate_model(y_test, y_pred_best)

    plot_actual_vs_predicted(y_test_selected, y_pred_best, optimized_model_name)
    plot_residual(y_test_selected, y_pred_best, optimized_model_name)

    return best, y_pred_best, optimized_model_metrics