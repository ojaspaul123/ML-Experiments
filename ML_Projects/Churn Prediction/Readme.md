# 📉 Customer Churn Prediction — Logistic Regression

A machine learning web app built with **Scikit-learn** and **Streamlit** that predicts whether a telecom customer is likely to churn based on their account details.

---

## 🚀 Demo

> Run locally with: `streamlit run Log_regression.py`

The app provides a simple form UI where you input customer attributes and click **Predict** to get an instant churn prediction.
<img width="1430" height="840" alt="image" src="https://github.com/user-attachments/assets/17598854-32c0-497f-a8d8-89b2280af54e" />
<img width="1344" height="896" alt="image" src="https://github.com/user-attachments/assets/2a7d8efd-fce6-41ad-805e-e8077b0881ee" />

---

## 📁 Project Structure

```
├── Log_regression.py           # Streamlit app (frontend + prediction logic)
├── churn_prediction_model.pkl  # Trained model bundle (model + scaler + encoder)
├── churn_prediction.ipynb      # Jupyter notebook (data exploration & model training)
├── churn_file.csv              # Dataset used for training
└── README.md
```

---

## 🧠 Model Details

- **Algorithm:** Logistic Regression (`sklearn.linear_model.LogisticRegression`)
- **Preprocessing:** `StandardScaler` for feature normalization, `LabelEncoder` for categorical encoding
- **Saved as:** A pickle bundle containing the model, scaler, and label encoder

### Input Features

| Feature | Type | Options |
|---|---|---|
| Gender | Categorical | Male, Female |
| Senior Citizen | Binary | Yes, No |
| Partner | Binary | Yes, No |
| Dependents | Binary | Yes, No |
| Tenure | Numeric | 0–30 months |
| Phone Service | Binary | Yes, No |
| Multiple Lines | Categorical | Yes, No, No phone service |
| Contract | Categorical | Month-to-month, One year, Two year |
| Total Charges | Numeric | Float value |

### Output

- `0` → **Customer is likely to churn**
- `1` → **Customer is NOT likely to churn**

---

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/churn-prediction.git
cd churn-prediction
```

### 2. Install dependencies

```bash
pip install streamlit pandas numpy scikit-learn
```

### 3. Run the Streamlit app

```bash
streamlit run Log_regression.py
```

The app will open at `http://localhost:8501` in your browser.

---
<img width="1304" height="924" alt="image" src="https://github.com/user-attachments/assets/7f4c5c03-a26f-4dc1-8ce7-e58b0f101850" />
<img width="1306" height="924" alt="image" src="https://github.com/user-attachments/assets/a588e044-8640-41d2-8a0e-b7bb9650f551" />

## 📊 Dataset

The model was trained on telecom customer data (`churn_file.csv`) containing customer demographics, service subscriptions, and billing information.

---

## 🌐 What is Streamlit & localhost?

**Streamlit** is an open-source Python framework that turns Python scripts into interactive web apps — without writing any HTML, CSS, or JavaScript.

When you run `streamlit run Log_regression.py`, it spins up a **local web server** on your machine and opens the app in your browser at:

```
http://localhost:8501
```

- `localhost` = **your own computer** (not the internet)
- `8501` = the default **port** Streamlit listens on
- The app only runs while the terminal is active

### Purpose of This App

This Streamlit app acts as a **frontend UI for the ML model**. It:
- Lets users input customer data through dropdowns and text fields
- Passes that data to the trained logistic regression model loaded from `churn_prediction_model.pkl`
- Displays whether the customer will churn — all without writing a single line of web code

---

## ⚠️ Common VS Code + Localhost Problems & Fixes

### ❌ Problem 1: Running with `python` instead of `streamlit`

A very common mistake — running the file like a regular Python script:

```bash
# ❌ WRONG — causes "missing ScriptRunContext" warning, app won't load
python Log_regression.py
```

Streamlit's server never starts this way. Always use:

```bash
# ✅ CORRECT
streamlit run Log_regression.py
```

---

### ❌ Problem 2: Wrong Python Interpreter in VS Code

VS Code may be using a different Python environment than where Streamlit is installed, causing a `streamlit: command not found` error.

**Fix:**
- Check the bottom-left corner of VS Code for the active Python interpreter
- Make sure it matches the environment where you ran `pip install streamlit`
- Or run in terminal:
```bash
pip show streamlit   # confirm it's installed in the active env
```

---

### ❌ Problem 3: Port 8501 Already in Use

If another process is using port 8501, Streamlit will fail to start.

**Fix:** Use a different port:
```bash
streamlit run Log_regression.py --server.port 8502
```

---

### ❌ Problem 4: Blank Screen or "Connecting…" Forever

The browser opens at `localhost:8501` but the page stays blank or keeps loading. This is usually a WebSocket issue.

**Fix:** Create a `.streamlit/config.toml` file in your project folder with:
```toml
[server]
enableCORS = false
enableXsrfProtection = false
```
Then hard-refresh the browser with `Ctrl + Shift + R`.

---

### ❌ Problem 5: Firewall Blocking the Port

If you're trying to access the app from another device on the same network and get `ERR_CONNECTION_TIMED_OUT`, your firewall is likely blocking port 8501.

**Fix:** Allow port 8501 through Windows Firewall, or restrict access to `localhost` only for local development.

---

### ✅ Correct Way to Run from VS Code

```bash
# Step 1 — Open VS Code terminal and navigate to your project folder
cd "path/to/your/project"

# Step 2 — Run with streamlit (NOT python)
streamlit run Log_regression.py
```

Then open `http://localhost:8501` in your browser.

---

## 📸 Screenshots

**App Interface**

> Fill in customer details using the dropdown menus and text input, then click **Predict**.
<img width="1430" height="840" alt="image" src="https://github.com/user-attachments/assets/17598854-32c0-497f-a8d8-89b2280af54e" />
<img width="1344" height="896" alt="image" src="https://github.com/user-attachments/assets/2a7d8efd-fce6-41ad-805e-e8077b0881ee" />
---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.
⚠️ Model Accuracy Disclaimer

This model was trained on a specific telecom dataset and achieves an accuracy of approximately ~77%.

Since the model is trained on a limited and specific dataset, predictions may or may not always be accurate for every input combination. This means:

The model can sometimes misclassify a churning customer as non-churning, or vice versa
Results should be treated as indicative, not definitive
For production-level use, the model would benefit from more data, hyperparameter tuning, or trying advanced algorithms like Random Forest or XGBoost

This is a learning/demo project intended to showcase how a machine learning model can be deployed as a web app using Streamlit.

💬 A Note from @ojaspaul123
Hey! 👋 Thanks for checking out this project.
This is one of my early machine learning projects where I built a customer churn prediction system using Logistic Regression and deployed it with Streamlit. The model gives around 77% accuracy — which means it works reasonably well, but isn't perfect.
The predictions are based on patterns learned from the training data, so results may vary depending on the inputs. I'm continuously learning and plan to improve this project further.
Feel free to explore the code, raise issues, or suggest improvements. Every bit of feedback helps! 🙌
— @ojaspaul123
---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
