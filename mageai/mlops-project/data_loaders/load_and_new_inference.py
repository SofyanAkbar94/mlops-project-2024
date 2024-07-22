from sklearn.preprocessing import StandardScaler
import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

@data_loader
def load_and_preprocess_inference_data(*args, **kwargs):
    # Load the data
    gold = pd.read_csv('https://stmlwol3bxs001.blob.core.windows.net/azureml-blobstore-e2c46a71-de7e-4b08-adde-4cbb6825a7be/UI/2024-07-20_105220_UTC/gold2024_07_19.csv')

    # Select relevant features
    features = gold.drop(columns=['Date', 'Adj Close'])

    # Standardize the data
    scaler = StandardScaler()
    X_inference = scaler.fit_transform(features)

    return {
        'X_inference': X_inference.tolist()
    }
