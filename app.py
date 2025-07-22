from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__,
            template_folder=".",
            static_folder=".")

# Load model and scaler
model = joblib.load(open('model.pkl', 'rb'))
scaler = joblib.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form
    features = [float(x) for x in request.form.values()]
    input_data = np.array([features])
    input_scaled = scaler.transform(input_data)
    
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]  # probability of death

    result = 'Patient is likely to SURVIVE' if prediction == 0 else 'Patient is likely to DIE'

    return render_template('index.html', prediction_text=result,
                           prob_text=f"Probability of Death: {probability:.2f}")

if __name__ == "__main__":
    app.run(debug=True)
