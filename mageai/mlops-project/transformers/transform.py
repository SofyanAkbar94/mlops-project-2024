import os
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

@transformer
def train_and_log_model(data, *args, **kwargs):
    import numpy as np
    X_train = np.array(data['X_train'])
    X_test = np.array(data['X_test'])
    y_train = np.array(data['y_train'])
    y_test = np.array(data['y_test'])

    try:
        mlflow.start_run()
        
        # Train the model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Make predictions
        predictions = model.predict(X_test)

        # Log metrics
        mse = mean_squared_error(y_test, predictions)
        mlflow.log_metric('mse', mse)

        # Log model
        model_path = 'random_forest_model'
        mlflow.sklearn.log_model(model, model_path)

        # Verify if the MLmodel file exists
        model_uri = mlflow.get_artifact_uri(model_path)
        model_local_dir = model_uri.replace("file://", "")
        mlmodel_file_path = os.path.join(model_local_dir, "MLmodel")
        
        if not os.path.exists(mlmodel_file_path):
            raise FileNotFoundError(f"Could not find MLmodel file at {mlmodel_file_path}")

        model_file_path = os.path.join(model_local_dir, "model.pkl")

        # Azure Blob Storage credentials
        connect_str = 'DefaultEndpointsProtocol=https;AccountName=stmlwol3bxs001;AccountKey=KbJOxSNy2zN7XIaoxk3p/jJzRHuf2xSi9qvPAs12974XE9uCxGNVCG5My1U8lhrTSEQqIzO5/W/D+AStH9NuOA==;EndpointSuffix=core.windows.net'
        container_name = 'azureml-blobstore-e2c46a71-de7e-4b08-adde-4cbb6825a7be'
        blob_name = 'random_forest_model/model.pkl'

        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        with open(model_file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        print(f"Model exported to Azure Blob Storage: {blob_name} in container {container_name}")

    finally:
        mlflow.end_run()

    return {
        'model_path': mlflow.get_artifact_uri(model_path)
    }
