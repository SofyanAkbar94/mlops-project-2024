from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
import mlflow

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def load_data(*args, **kwargs):
    subscription_id = 'a9a8a68b-6192-48c1-ba65-1994b763579d'
    resource_group = 'mlops'
    workspace_name = 'mlwol3bxs001'

    ml_client = MLClient(credential=DefaultAzureCredential(),
                        subscription_id=subscription_id, 
                        resource_group_name=resource_group,
                        workspace_name=workspace_name)

    # Set MLflow tracking URI and experiment
    mlflow_tracking_uri = ml_client.workspaces.get(ml_client.workspace_name)
    mlflow.set_experiment("gold-pred-experiment")