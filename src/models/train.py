import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from src.models.evaluate import evaluate_model
from src.utils.visualization import plot_actual_vs_predicted, plot_residual, plot_neural_network_training_history

def train_model(model, X_train, y_train, X_test):
    model.fit(X_train, y_train)

    return model, model.predict(X_test)

def train_ann_model(X_train, y_train, X_test, y_test):
    X_train = X_train.astype('float32')
    y_train = y_train.astype('float32')
    X_test = X_test.astype('float32')
    y_test = y_test.astype('float32')
    dropout_value = 0.5
    ann_model = Sequential([
        Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
        Dropout(0.2),
        Dense(64, activation='relu'),
        Dropout(0.2),
        Dense(32, activation='relu'),
        Dropout(0.2),
        Dense(1, activation='linear')
    ])

    # Compile the model
    ann_model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')

    # Train the model
    # history = ann_model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, verbose=1)
    history = ann_model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test), verbose=1)

    # Predictions
    return ann_model, ann_model.predict(X_test).flatten(), history

def train_and_evaluate_models(models, X_train, y_train, X_test, y_test, plot_charts: bool = False) -> dict:
    ann_history = {}
    results = {}
    for model_name, model in models:
        if None == model: # for ANN model
            trained_model, predictions, history = train_ann_model(X_train, y_train, X_test, y_test)
            ann_history['name'] = model_name
            ann_history['history'] = history
        else:
            trained_model, predictions = train_model(model, X_train, y_train, X_test)
        print(f'{model_name} Metrics:')
        model_metrics = evaluate_model(y_test, predictions)
        if plot_charts:
            plot_actual_vs_predicted(y_test, predictions, model_name)
            plot_residual(y_test, predictions, model_name)
            if len(ann_history) > 0:
                plot_neural_network_training_history(ann_history['history'], ann_history['name'])
        results[model_name] = trained_model
    return results

def visualise(model_results: dict, y_test):
    for model_result in model_results:
        plot_actual_vs_predicted(y_test, predictions, model_name)
        plot_residual(y_test, predictions, model_name)
        if len(ann_history) > 0:
            plot_neural_network_training_history(ann_history['history'], ann_history['name'])