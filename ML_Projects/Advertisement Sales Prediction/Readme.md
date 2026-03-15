# 📈 Advertisement Sales Prediction

A Machine Learning project that predicts product **Sales** based on advertising budgets across **TV**, **Radio**, and **Newspaper** channels using **Linear Regression**.

---

## 🚀 Live Demo

> Run locally with Streamlit — see [How to Run](#-how-to-run) below.




---

## 📁 Project Structure

```
ML_Projects/
├── Linear_regression_model.pkl   # Trained model (serialized)
├── Prediction.py                 # Streamlit web app
├── advertising_data.csv          # Dataset
└── README.md                     # This file
```

---

## 📊 Dataset

| Column       | Description                        |
|--------------|------------------------------------|
| `TV`         | TV advertising budget              |
| `Radio`      | Radio advertising budget           |
| `Newspaper`  | Newspaper advertising budget       |
| `Sales`      | Product sales (target variable)    |

---

## 🔄 Workflow

```
Google Colab  →  Train Model  →  Export .pkl  →  VS Code  →  Streamlit GUI
```

---

## 🧪 Phase 1 — Google Colab (Model Training)

Open [Google Colab](https://colab.research.google.com) and run the following:

### 1. Import Libraries
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
import pickle
```

### 2. Upload & Load Dataset
```python
from google.colab import files
uploaded = files.upload()   # upload advertising_data.csv

df = pd.read_csv('advertising_data.csv')
df.head()
```

### 3. Exploratory Data Analysis
```python
sns.pairplot(df)

plt.scatter(x=df['TV'], y=df['Sales'])
plt.xlabel('TV Budget')
plt.ylabel('Sales')
plt.show()
```

### 4. Train / Test Split
```python
X = df.iloc[:, :-1]   # TV, Radio, Newspaper
y = df.iloc[:, -1]    # Sales

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(X_train.shape, X_test.shape)
```

### 5. Train the Model
```python
lr = LinearRegression()
lr.fit(X_train, y_train)
pred = lr.predict(X_test)
```

### 6. Evaluate
```python
print("MAE   :", mean_absolute_error(y_test, pred))
print("R2    :", r2_score(y_test, pred))
```

| Metric    | Value   |
|-----------|---------|
| MAE       | ~940    |
| R2 Score  | ~0.997  |

### 7. Export Model as Pickle
```python
pickle.dump(lr, open('Linear_regression_model.pkl', 'wb'))
```

> ⬇️ Download `Linear_regression_model.pkl` from Colab to your local machine.

---

## 💻 Phase 2 — VS Code Setup

### 1. Folder Structure
```
ML_Projects/
├── Linear_regression_model.pkl   ← paste downloaded file here
└── Prediction.py                 ← create this file
```

### 2. Install Dependencies
```bash
pip install streamlit scikit-learn numpy pandas
```

### 3. Prediction.py
```python
import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('Linear_regression_model.pkl', 'rb'))

st.title("Scikit learn linear regression prediction")

tv        = st.number_input("enter tv sales...",        min_value=0.0)
radio     = st.number_input("enter radio sales...",     min_value=0.0)
newspaper = st.number_input("enter newspaper sales...", min_value=0.0)

if st.button("Predict"):
    features = np.array([[tv, radio, newspaper]])
    result   = model.predict(features)[0]
    st.subheader("Predicted Sales")
    st.write(round(result, 4))
```

---

## 🌐 Phase 3 — Run the Streamlit Web App

### Step 1 — Navigate to your project folder
```bash
cd "C:\Users\KIIT\Desktop\VS Code\Mini Project\ML_Projects"
```

### Step 2 — Launch the app
```bash
python -m streamlit run Prediction.py
```

> ✅ Use `python -m streamlit` instead of `streamlit` to avoid PATH issues on Windows.

### Step 3 — Open in browser
Streamlit will auto-open:
```
Local URL:    http://localhost:8501
Network URL:  http://10.2.0.2:8501
```

---

## 📌 Example Prediction

| TV     | Radio  | Newspaper | Predicted Sales |
|--------|--------|-----------|-----------------|
| 8,500  | 7,000  | 3,200     | **62,366.96**   |
| 23,000 | 18,500 | 9,200     | **141,647.46**  |

---

## 🛠 Troubleshooting

| Error | Fix |
|-------|-----|
| `FileNotFoundError: Linear_regression_model.pkl` | Make sure terminal is inside `ML_Projects/` folder |
| `'streamlit' is not recognized` | Use `python -m streamlit run Prediction.py` |
| `ModuleNotFoundError` | Run `pip install streamlit scikit-learn numpy pandas` |
| Port 8501 already in use | Add `--server.port 8502` to the run command |

---

## 📦 Requirements

```
streamlit
scikit-learn
numpy
pandas
matplotlib
seaborn
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## ⬆️ Push to GitHub

```bash
git init
git add .
git commit -m "Add Ad Sales Prediction ML project"
git remote add origin https://github.com/YOUR_USERNAME/Ad-Sales-Prediction.git
git branch -M main
git push -u origin main
```

---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-GUI-red?logo=streamlit)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikit-learn)
![Google Colab](https://img.shields.io/badge/Google-Colab-yellow?logo=googlecolab)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).📈 Advertisement Sales Prediction using Linear Regression
