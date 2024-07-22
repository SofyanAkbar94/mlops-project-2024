import io
import numpy as np
import pandas as pd
import requests
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

@data_loader
def load_data(*args, **kwargs):
    # Load the data
    gold = pd.read_csv('https://stmlwol3bxs001.blob.core.windows.net/azureml-blobstore-e2c46a71-de7e-4b08-adde-4cbb6825a7be/UI/2024-07-20_105220_UTC/gold2024_07_19.csv')

    # Check for missing values
    missing_values = gold.isnull().sum()
    print(missing_values[missing_values > 0])

    # Select relevant features and the target variable
    features = gold.drop(columns=['Date', 'Adj Close'])
    target = gold['Adj Close']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Standardize the data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return {
        'X_train': X_train.tolist(),
        'X_test': X_test.tolist(),
        'y_train': y_train.tolist(),
        'y_test': y_test.tolist()
    }