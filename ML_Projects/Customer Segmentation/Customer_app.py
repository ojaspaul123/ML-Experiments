import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
 
st.set_page_config(page_title='Customer Segmentation', page_icon='🛍️')
 
# Load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pkl_path = os.path.join(BASE_DIR, 'Customer_Segmentation.pkl')
 
with open(pkl_path, 'rb') as f:
    bundle = pickle.load(f)
 
model  = bundle['kmeans']
scaler = bundle['scaler']
 
# UI
st.title('🛍️ Customer Segmentation')
 
recency   = st.number_input('Recency (days since last purchase)', min_value=0,   max_value=1000,      value=30)
frequency = st.number_input('Frequency (number of orders)',       min_value=1,   max_value=1000,      value=5)
monetary  = st.number_input('Monetary (total amount spent £)',    min_value=0.0, max_value=1000000.0, value=1000.0)
 
if st.button('Predict Segment'):
    data    = pd.DataFrame({'Recency': [recency], 'Frequency': [frequency], 'Monetary': [monetary]})
    scaled  = scaler.transform(np.log1p(data))
    cluster = model.predict(scaled)[0]
 
    labels = {0: 'Low Value Customer', 1: 'VIP Customer', 2: 'Regular Customer', 3: 'Churn Risk Customer'}
    tips   = {
        'VIP Customer':        'Offer loyalty rewards and premium products.',
        'Regular Customer':    'Recommend related products and upsell offers.',
        'Low Value Customer':  'Send discount coupons to increase engagement.',
        'Churn Risk Customer': 'Launch retention campaigns and personalised emails.'
    }
 
    name = labels[cluster]
    st.success(f'Cluster {cluster} — {name}')
    st.info(tips[name])