import streamlit as st
import numpy as np
import pickle

# Load model and scaler
with open("rf_result.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

st.title("❤️ Heart Disease Prediction")
st.markdown("---")


male         = st.selectbox("Gender", ["Male", "Female"])
age          = st.number_input("Age", min_value=1, max_value=120, value=50)
currentSmoker = st.selectbox("Current Smoker?", ["No", "Yes"])
cigsPerDay   = st.number_input("Cigarettes Per Day", min_value=0.0, max_value=100.0, value=0.0)
BPMeds       = st.selectbox("On Blood Pressure Medication?", ["No", "Yes"])
prevalentStroke = st.selectbox("Prevalent Stroke?", ["No", "Yes"])
prevalentHyp = st.selectbox("Prevalent Hypertension?", ["No", "Yes"])
diabetes     = st.selectbox("Diabetes? (1 = Yes, 0 = No)", [0, 1])
totChol      = st.number_input("Total Cholesterol", min_value=100.0, max_value=600.0, value=200.0)
sysBP        = st.number_input("Systolic BP", min_value=80.0, max_value=300.0, value=120.0)
diaBP        = st.number_input("Diastolic BP", min_value=40.0, max_value=200.0, value=80.0)
BMI          = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
heartRate    = st.number_input("Heart Rate", min_value=30.0, max_value=200.0, value=75.0)
glucose      = st.number_input("Glucose", min_value=40.0, max_value=400.0, value=85.0)

if st.button("Predict"):
    
    male_enc            = 1 if male == "Male" else 0
    currentSmoker_enc   = 1 if currentSmoker == "Yes" else 0
    BPMeds_enc          = 1 if BPMeds == "Yes" else 0
    prevalentStroke_enc = 1 if prevalentStroke == "Yes" else 0
    prevalentHyp_enc    = 1 if prevalentHyp == "Yes" else 0


    features = np.array([[
        male_enc, age, currentSmoker_enc, cigsPerDay,
        BPMeds_enc, prevalentStroke_enc, prevalentHyp_enc,
        diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose
    ]])

    scaled = scaler.transform(features)
    result = model.predict(scaled)[0]

    if result == 1:
        st.error("⚠️ High Risk — Patient likely has Heart Disease")
    else:
        st.success("✅ Low Risk — Patient likely has No Heart Disease")