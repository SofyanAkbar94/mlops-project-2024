import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load data
data = pd.read_csv("https://stmlwol3bxs001.blob.core.windows.net/azureml-blobstore-e2c46a71-de7e-4b08-adde-4cbb6825a7be/UI/2024-07-20_105220_UTC/gold2024_07_19.csv")

# Convert the 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Drop the 'Date' column as it's not a feature
features = data.drop(columns=["Date", "Adj Close"])

# Handle missing values and convert integer columns to float
features = features.astype(float)  # Convert all columns to float
features = features.fillna(features.mean())  # Fill missing values with column mean

# Target variable
target = data["Adj Close"]

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)

print(f"Mean Squared Error: {mse}")
