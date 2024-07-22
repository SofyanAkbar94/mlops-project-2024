import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

@transformer
def train_and_log_model(data, *args, **kwargs):
    X_train = data['X_train']
    X_test = data['X_test']
    y_train = data['y_train']
    y_test = data['y_test']

    with mlflow.start_run():
        # Train the model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Make predictions
        predictions = model.predict(X_test)

        # Log metrics
        mse = mean_squared_error(y_test, predictions)
        mlflow.log_metric('mse', mse)

        # Log model
        mlflow.sklearn.log_model(model, 'random_forest_model')

    return model, mse
