import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("credit_card_model.pkl")

st.set_page_config(page_title="Credit Card Fraud Detection", layout="centered")
st.title("💳 Credit Card Fraud Detection App")
st.write("Enter transaction details to predict whether it's Fraud or Legit.")

# --- ALL 30 features the model was trained on ---
Time = st.number_input("Time", value=0.0)

st.subheader("PCA Features (V1 – V28)")
cols = st.columns(4)
V = {}
for i in range(1, 29):
    col = cols[(i - 1) % 4]
    V[f"V{i}"] = col.number_input(f"V{i}", value=0.0)

Amount = st.number_input("Transaction Amount", value=0.0)

# Create input dataframe with correct column order
input_data = pd.DataFrame([{
    "Time": Time,
    **V,
    "Amount": Amount
}])

# Prediction button
if st.button("Predict"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Legitimate Transaction")

# Optional: show raw input
if st.checkbox("Show Input Data"):
    st.write(input_data)