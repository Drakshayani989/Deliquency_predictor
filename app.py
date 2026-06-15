import pickle
model = pickle.load(open("model.pkl", "rb"))
import streamlit as st
import numpy as np
import pickle

# Load trained model (save your model first using pickle)
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Delinquency Predictor", layout="centered")

st.title("💳 Delinquency Risk Prediction App")
st.write("Enter customer details to predict delinquency risk")

# Input fields
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=650)
dti = st.number_input("Debt-to-Income Ratio", min_value=0.0, max_value=1.0, value=0.3)
missed_payments = st.number_input("Missed Payments", min_value=0, max_value=10, value=1)
credit_util = st.number_input("Credit Utilization", min_value=0.0, max_value=1.0, value=0.4)
age = st.number_input("Age", min_value=18, max_value=100, value=30)
# Predict button
if st.button("Predict Risk"):
    features = np.array([[credit_score, dti, missed_payments, credit_util,age]])
    
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]
    
    if prediction == 1:
        st.error(f"⚠️ High Risk of Delinquency\nRisk Score: {probability:.2f}")
    else:
        st.success(f"✅ Low Risk\nRisk Score: {probability:.2f}")