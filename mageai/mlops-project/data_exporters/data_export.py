import pandas as pd
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_predictions(data, *args, **kwargs):
    predictions = data['predictions']
    
    # Create a DataFrame from predictions
    df = pd.DataFrame(predictions, columns=['Predictions'])
    
    # Save DataFrame to a CSV file
    csv_path = '/tmp/predictions.csv'
    df.to_csv(csv_path, index=False)
    
    # Azure Blob Storage credentials
    connect_str = 'DefaultEndpointsProtocol=https;AccountName=stmlwol3bxs001;AccountKey=KbJOxSNy2zN7XIaoxk3p/jJzRHuf2xSi9qvPAs12974XE9uCxGNVCG5My1U8lhrTSEQqIzO5/W/D+AStH9NuOA==;EndpointSuffix=core.windows.net'
    container_name = 'azureml-blobstore-e2c46a71-de7e-4b08-adde-4cbb6825a7be'
    blob_name = 'predictions.csv'

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    
    # Upload the CSV file to Azure Blob Storage
    with open(csv_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    
    print(f"Predictions exported to Azure Blob Storage: {blob_name} in container {container_name}")

    return {
        'export_path': f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{blob_name}"
    }
