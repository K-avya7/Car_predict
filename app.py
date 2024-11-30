
# app.py

from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd


# Load the trained model
model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

scaler_path = 'scaler.pkl'
with open(scaler_path, 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form data
        age = int(request.form.get('age', 0))  # 'age' matches the name attribute
        estimated_salary = float(request.form.get('salary', 0))  # 'salary' matches the name attribute
        gender = int(request.form.get('gender', 0))  # 'gender' matches the name attribute

        # Create a DataFrame with the correct column order
        input_data = pd.DataFrame([[age, estimated_salary, gender]], columns=["Age", "EstimatedSalary", "Gender"])

        # Scale the input data using the pre-trained scaler
        scaled_features = scaler.transform(input_data)

        # Predict using the trained model
        prediction = model.predict(scaled_features)

        # Return the prediction result
        output = 'Will Purchase' if prediction[0] == 1 else 'Will Not Purchase'
    except ValueError:
        output = 'Invalid input. Please ensure all fields are filled with valid numeric values.'

    return render_template('index.html', prediction_text='Prediction: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
