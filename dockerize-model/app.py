import streamlit as st
import numpy as np
import joblib
import os

# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'model/random_forest_model.pkl')
model = joblib.load(model_path)

st.title('ML Model Prediction')

# Example input data structure
example_input = '{"X_inference": [[1.0, 2.0, 3.0, 4.0, 5.0, 6.0], [7.0, 8.0, 9.0, 10.0, 11.0, 12.0]]}'
st.write('Example input format:', example_input)

# Input data
input_data = st.text_area('Enter input data in JSON format', example_input)

if st.button('Predict'):
    try:
        # Parse input data
        data = eval(input_data)
        X_inference = np.array(data['X_inference'])
        
        # Verify the number of features
        if X_inference.shape[1] != model.n_features_in_:
            st.write(f"Error: The model expects {model.n_features_in_} features, but the input has {X_inference.shape[1]} features.")
        else:
            # Make predictions
            predictions = model.predict(X_inference)

            # Display predictions
            st.write('Predictions:', predictions.tolist())
    except Exception as e:
        st.write('Error:', e)
