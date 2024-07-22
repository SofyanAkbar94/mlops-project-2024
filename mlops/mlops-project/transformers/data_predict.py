import joblib
import numpy as np

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

@transformer
def load_model_and_predict(data, *args, **kwargs):
    X_inference = np.array(data['X_inference'])
    
    # Manually load the trained model
    model_path = "/home/src/mlruns/0/b1f1c18c4d274fe1840059e9c290fe96/random_forest_model.pkl"
    model = joblib.load(model_path)

    # Make predictions
    predictions = model.predict(X_inference)

    return {
        'predictions': predictions.tolist()
    }
