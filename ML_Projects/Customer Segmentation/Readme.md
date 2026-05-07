# 🛍️ Customer Segmentation System with KMeans Clustering - Unsupervised learning

A Machine Learning web application that segments customers into meaningful groups using **RFM Analysis** (Recency, Frequency, Monetary) and **K-Means Clustering**, deployed with Streamlit.

🌐 **Live App:** [https://your-app-name.streamlit.app](http://localhost:8501/) 

---
|<img width="1439" height="840" alt="image" src="https://github.com/user-attachments/assets/590ab5d6-1006-4bf9-8e01-9eaccd364310" /> <img width="1448" height="840" alt="image" src="https://github.com/user-attachments/assets/4eeea3a8-7836-4e59-92ad-d58f0cc5a7db" /> | <img width="1437" height="840" alt="image" src="https://github.com/user-attachments/assets/7e1ad453-7365-40f3-a932-56d4de37724a" /> <img width="1316" height="921" alt="image" src="https://github.com/user-attachments/assets/a49d535e-04d4-4189-96c7-9f86df72d584" />  |




---
## 📁 Project Structure

```
ML_Projects/
│
├── Customer_app.py                # Streamlit web application
├── Customer_Segmentation.pkl      # Trained KMeans model + scaler (bundled)
├── Customer_Segmentation.ipynb    # Jupyter notebook (EDA, training, evaluation)
├── Online_Retail.xlsx             # Raw dataset (UCI Online Retail)
└── README.md                      # Project documentation
```

---

## 🤔 What Does It Do?

This app takes three simple inputs about a customer:

| Input | Description |
|---|---|
| **Recency** | How many days ago did they last purchase? |
| **Frequency** | How many orders have they placed? |
| **Monetary** | How much have they spent in total (£)? |

It then predicts which of **4 customer segments** they belong to and gives a business recommendation:

| Cluster | Segment | Action |
|---|---|---|
| 0 | 🟡 Low Value Customer | Send discount coupons to increase engagement |
| 1 | 🟢 VIP Customer | Offer loyalty rewards and premium products |
| 2 | 🔵 Regular Customer | Recommend related products and upsell offers |
| 3 | 🔴 Churn Risk Customer | Launch retention campaigns and personalised emails |

---

## ⚙️ How It Works

```
Raw Data (541,909 transactions)
        ↓
Data Cleaning & Preprocessing
        ↓
RFM Feature Engineering
        ↓
Log Transform + StandardScaler
        ↓
K-Means Clustering (k=4)
        ↓
Streamlit Web App → Predict Segment
```

**Tech stack:** Python · Pandas · NumPy · Scikit-learn · Streamlit · Pickle

---

## 👥 Who Uses This?

- **E-commerce businesses** wanting to personalise marketing campaigns
- **CRM & marketing teams** looking to prioritise customer outreach
- **Data analysts** building customer intelligence dashboards
- **Students & researchers** learning RFM-based segmentation

---

## 🌍 Real-World Impact

| Business Problem | How This Helps |
|---|---|
| Wasted marketing budget | Target the right customers with the right message |
| High churn rate | Identify at-risk customers early and retain them |
| Low VIP engagement | Recognise high-value customers and reward them |
| Generic campaigns | Replace one-size-fits-all emails with personalised ones |

**Example:** A retailer using this system can reduce churn by up to 25% by identifying Cluster 3 customers early and sending them a win-back offer before they leave permanently.

---
<img width="1316" height="921" alt="image" src="https://github.com/user-attachments/assets/015d4023-ca16-4105-8501-f61eec55d9fb" />

---
## 🚀 Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/your-username/customer-segmentation.git
cd customer-segmentation
```

**2. Install dependencies**
```bash
pip install streamlit pandas numpy scikit-learn openpyxl
```

**3. Run the app**
```bash
streamlit run Customer_app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📊 Dataset

- **Source:** [UCI Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/Online+Retail)
- **Size:** 541,909 transactions · 8 columns
- **Period:** Dec 2010 – Dec 2011
- **Scope:** UK-based online retail store

---

## 📈 Model Performance

- **Algorithm:** K-Means Clustering (k=4)
- **Features:** Log-transformed + StandardScaled RFM values
- **Evaluation:** Elbow Method + Silhouette Score

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@your-username](https://github.com/ojaspaul123)
---

## 📄 License

This project is open source under the [MIT License](LICENSE).
