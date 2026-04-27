# 💳 Credit Card Fraud Detection

A Machine Learning-powered web application that detects fraudulent credit card transactions in real time using a trained classification model, built with Python and deployed via Streamlit.

---

## 📁 Project Structure

```
credit-card-fraud-detection/
│
├── creditcard_50000rows.csv          # Dataset (imbalanced — fraud cases are rare)
├── Credit_Card_Detection.ipynb       # Jupyter Notebook (EDA, preprocessing, model training)
├── credit_card_model.pkl             # Trained ML model (serialized with joblib)
└── card_detection.py                 # Streamlit web app (frontend + prediction logic)
```

---

## 🔍 What Does It Do?

This project uses a machine learning model trained on real-world credit card transaction data. Given 30 transaction features — `Time`, 28 PCA-transformed components (`V1`–`V28`), and `Amount` — it predicts whether a transaction is:

- ✅ **Legitimate** — Normal transaction
- ⚠️ **Fraudulent** — Suspicious transaction that should be flagged

The Streamlit app provides a clean UI where users can manually enter all 30 feature values and instantly get a prediction.

---

## 👥 Who Uses This?

| User | Use Case |
|------|----------|
| 🏦 Banks & Fintech companies | Real-time fraud monitoring systems |
| 🔐 Security analysts | Investigating flagged transactions |
| 📊 Data scientists | Baseline model for fraud detection research |
| 🎓 Students & learners | Learning ML + Streamlit deployment |

---

## 🧠 How It Works

1. **Dataset** — The CSV contains 50,000 transactions with anonymized PCA features (V1–V28), Time, Amount, and a `Class` label (0 = legit, 1 = fraud). The data is **highly imbalanced** (fraud cases < 1%).

2. **Notebook** — Handles:
   - Exploratory Data Analysis (EDA)
   - Handling class imbalance (SMOTE / undersampling / class weights)
   - Model training (Random Forest / Logistic Regression / XGBoost etc.)
   - Evaluation using precision, recall, F1, ROC-AUC

3. **Model** — Saved as `credit_card_model.pkl` using `joblib`, loaded at runtime by the Streamlit app.

4. **App** — User inputs feature values → model predicts → result displayed instantly.

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/your-username/credit-card-fraud-detection.git
cd credit-card-fraud-detection
```

### 2. Install dependencies
```bash
pip install streamlit pandas scikit-learn joblib
```

### 3. Run the app
```bash
python -m streamlit run card_detection.py
```

### 4. Open in browser
```
Local URL:   http://localhost:8501
Network URL: http://192.168.x.x:8501
```
<img width="1372" height="894" alt="image" src="https://github.com/user-attachments/assets/214fc284-a6dc-4c84-b97a-9adbfb5426b0" />

---

## 🌐 Live App

> **Hosted on Streamlit Community Cloud:**
> 🔗 [https://streamlit.io/cloud](http://localhost:8501/)

To deploy your own:
1. Push this repo to GitHub
2. Go to [https://streamlit.io/cloud](http://localhost:8501/)
3. Click **"New app"** → select your repo → set `card_detection.py` as the entry point
4. Click **Deploy** — your app goes live in minutes, for free!

---

<img width="1444" height="840" alt="image" src="https://github.com/user-attachments/assets/bf1c7bda-1a70-4087-91f0-a9c440369256" />
<img width="1444" height="840" alt="image" src="https://github.com/user-attachments/assets/9e50a3d9-0259-4d1f-9b59-54ddbcefb6b1" />

---

## ⚠️ Common Problems & How to Fix Them

### ❌ `ModuleNotFoundError: No module named 'streamlit'`
**Fix:**
```bash
pip install streamlit
```

---

### ❌ `FileNotFoundError: credit_card_model.pkl not found`
The app looks for the model in the **same directory** it's run from.

**Fix:** Make sure `credit_card_model.pkl` is in the same folder as `card_detection.py`, and run from that folder:
```bash
cd path/to/your/project
python -m streamlit run card_detection.py
```

---

### ❌ `ValueError: Feature names mismatch` or `ValueError: X has N features but model expects 30`
This happens when the input DataFrame column names or order don't match training data.

**Fix:** Ensure `input_data` has columns in this exact order:
```
Time, V1, V2, ..., V28, Amount
```
The current `card_detection.py` already handles this correctly via dictionary unpacking.

---

### ❌ Model always predicts "Legitimate" (never flags fraud)
This is caused by the **class imbalance** problem in the dataset. A model trained on raw imbalanced data learns to always predict the majority class.

**Fix (in notebook):**
- Use **SMOTE** (Synthetic Minority Oversampling Technique):
  ```python
  from imblearn.over_sampling import SMOTE
  sm = SMOTE(random_state=42)
  X_res, y_res = sm.fit_resample(X_train, y_train)
  ```
- Or use `class_weight='balanced'` in your classifier:
  ```python
  RandomForestClassifier(class_weight='balanced')
  ```

---

### ❌ App crashes when deployed on Streamlit Cloud (`pkl` file too large or missing)
**Fix:** Ensure `credit_card_model.pkl` is committed to your GitHub repo (check `.gitignore` — don't exclude `.pkl` files). If file size exceeds GitHub's 100MB limit, use [Git LFS](https://git-lfs.com/).

---

### ❌ `StreamlitAPIException: set_page_config() can only be called once`
**Fix:** Make sure `st.set_page_config()` is the **very first Streamlit command** in `card_detection.py`, before any other `st.*` calls.

---

## 📦 Requirements

```
streamlit
pandas
scikit-learn
joblib
```

Install all at once:
```bash
pip install streamlit pandas scikit-learn joblib
```

Or create a `requirements.txt`:
```
streamlit>=1.30.0
pandas>=2.0.0
scikit-learn>=1.3.0
joblib>=1.3.0
```

---

## 📊 Dataset Info

| Property | Detail |
|----------|--------|
| Rows | 50,000 transactions |
| Features | 30 (Time, V1–V28, Amount) |
| Target | `Class` — 0 (Legit), 1 (Fraud) |
| Imbalance | Fraud cases < 1% of total |
| Source | Adapted from the [Kaggle Credit Card Fraud Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) |

---

## 🙋 Author

**Your Name**
- GitHub: [@ojaspaul123](https://github.com/ojaspaul123)
- LinkedIn: [@ojas-paul](https://www.linkedin.com/in/ojas-paul-324aa5337/)

---

## 📄 License

This project is licensed under the MIT License — feel free to use, modify, and distribute.
