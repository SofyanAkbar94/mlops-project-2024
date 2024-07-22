from flask import Flask, request, jsonify
import numpy as np
import joblib
import os

app = Flask(__name__)

# Load the model
model_path = os.path.join(os.path.dirname(__file__), '../model/random_forest_model.pkl')
model = joblib.load(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    X_inference = np.array(data['X_inference'])

    # Make predictions
    predictions = model.predict(X_inference)

    return jsonify({'predictions': predictions.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
