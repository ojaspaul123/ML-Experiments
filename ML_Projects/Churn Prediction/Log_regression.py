import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle
from sklearn.preprocessing import StandardScaler,LabelEncoder
label_encoder = LabelEncoder()
scaler = StandardScaler()

bundle = pickle.load(open('churn_prediction_model.pkl', 'rb'))
model = bundle['model']
scaler = bundle['scaler']
label_encoder = bundle['label_encoder']


st.title("Scikit learn logistic regression prediction")
gender = st.selectbox("SELECT GENDER",options=["Male", "Female"])
SeniorCitizen = st.selectbox("ARE YOU A SENIOR CITIZEN",options=["Yes", "No"])
Partner = st.selectbox("SELECT PARTNER",options=["Yes", "No"])
Dependents = st.selectbox("SELECT DEPENDENTS",options=["Yes", "No"])
tenure = st.selectbox("SELECT TENURE",options = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
PhoneService = st.selectbox("SELECT PHONE SERVICE",options=["Yes", "No"])
MultipleLines = st.selectbox("SELECT MULTIPLE LINES",options=["Yes", "No","No phone service"])
Contract = st.selectbox("SELECT CONTRACT",options=["Month-to-month", "One year", "Two year"])
TotalCharges = st.text_input("ENTER TOTAL CHARGES...")



def prediction(gender, Seniorcitizen, Partner, Dependents, tenure,
               Phoneservice, multiline, contact, totalcharge):
    
    # ✅ Manually map categories to numbers (same as LabelEncoder would do)
    gender_map     = {'Female': 0, 'Male': 1}
    yesno_map      = {'No': 0, 'Yes': 1}
    multiline_map  = {'No': 0, 'No phone service': 1, 'Yes': 2}
    contract_map   = {'Month-to-month': 0, 'One year': 1, 'Two year': 2}

    data = {
        'gender':        [gender_map[gender]],
        'SeniorCitizen': [Seniorcitizen],        # already 0 or 1
        'Partner':       [yesno_map[Partner]],
        'Dependents':    [yesno_map[Dependents]],
        'tenure':        [int(tenure)],
        'PhoneService':  [yesno_map[Phoneservice]],
        'MultipleLines': [multiline_map[multiline]],
        'Contract':      [contract_map[contact]],
        'TotalCharges':  [float(totalcharge)]
    }

    df = pd.DataFrame(data)
    df_scaled = scaler.transform(df)
    result = model.predict(df_scaled).reshape(1, -1)
    return result[0]    

if st.button("Predict"):
    result = prediction(gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,MultipleLines,Contract,TotalCharges)

    if result==0:
        st.write('The customer is likely to churn.')
    else:
        st.write('The customer is not likely to churn.')