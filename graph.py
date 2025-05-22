import pickle
import numpy as np
import matplotlib.pyplot as plt

# Load the model
with open('diabetes_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Feature names (as per your model)
features = ['gender', 'age', 'hypertension', 'heart_disease', 'smoking_history', 'bmi', 'HbA1c_level', 'blood_glucose_level']

# Get coefficients
coefs = model.coef_[0]

# Plot
plt.figure(figsize=(8,4))
plt.barh(features, coefs)
plt.xlabel('Coefficient Value')
plt.title('Feature Importance for Diabetes Prediction')
plt.show()