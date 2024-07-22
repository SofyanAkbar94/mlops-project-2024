import mlflow
import mlflow.sklearn
import numpy as np

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

@transformer
def load_model_and_predict(data, *args, **kwargs):
    X_inference = np.array(data['X_inference'])
    
    # Load the trained model
    model_path = kwargs['model_path']
    model = mlflow.sklearn.load_model(model_path)

    # Make predictions
    predictions = model.predict(X_inference)

    return {
        'predictions': predictions.tolist()
    }
