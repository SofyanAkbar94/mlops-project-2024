import json
import numpy as np
import joblib
import os
from azureml.core.model import Model

def init():
    global model
    # Get the path to the model file using the model name
    model_path = Model.get_model_path('random_forest_model.pkl')
    # Load the model from the file
    model = joblib.load(model_path)

def run(raw_data):
    try:
        # Parse the input data
        data = json.loads(raw_data)
        X_inference = np.array(data['X_inference'])

        # Make predictions
        predictions = model.predict(X_inference)

        # Return predictions as a JSON object
        return json.dumps({'predictions': predictions.tolist()})
    except Exception as e:
        error = str(e)
        return json.dumps({'error': error})
