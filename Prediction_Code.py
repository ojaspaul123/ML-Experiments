import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle
model = pickle.load(open('Linear_regression_model.pkl','rb'))
st.title("Scikit learn linear regression prediction")
tv = st.text_input("enter tv sales...")
radio= st.text_input("enter radio sales...")
newspaper = st.text_input("enter newspaper sales...")
if st.button("Predict"):
    features = np.array([[tv,radio,newspaper]],dtype=np.float64)
    results = model.predict(features).reshape(1,-1)
    st.write("Predicted Sales ",results[0])