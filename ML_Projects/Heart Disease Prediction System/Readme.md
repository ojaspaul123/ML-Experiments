# ❤️ Heart Disease Prediction

A machine learning web application that predicts the **10-year risk of coronary heart disease (CHD)** in patients based on clinical and lifestyle features. Built with Python, scikit-learn, and Streamlit.

---

## 🖥️ Live Demo

Run locally:
```bash
streamlit run Heart_diseases_app.py
```
| Has No Heart Diseases | Has Heart Diseases |
|---|---|
|<img width="1915" height="1113" alt="Screenshot 2026-05-06 001419" src="https://github.com/user-attachments/assets/c6cb3db4-d11a-42a3-a95a-235fca65413a" />  <img width="1910" height="1118" alt="Screenshot 2026-05-06 001438" src="https://github.com/user-attachments/assets/67436da3-4dfc-4b7c-8630-8479bb0150d9" />  | <img width="1915" height="1114" alt="Screenshot 2026-05-06 001903" src="https://github.com/user-attachments/assets/8e69a088-19fa-42f3-983b-80d696d0fd4b" />  <img width="1919" height="1120" alt="Screenshot 2026-05-06 001920" src="https://github.com/user-attachments/assets/2a7dcd92-c2c9-415a-ac92-495cabd087e5" />  |

---

## 📁 Project Structure

```
ML_Projects/
│
├── Heart_diseases_app.py          # Streamlit web application
├── Heart_Disease_Prediction.ipynb # Model training notebook
├── heart_diseases_datasets.csv    # Dataset (Framingham Heart Study)
├── rf_result.pkl                  # Saved Random Forest model
├── scaler.pkl                     # Saved StandardScaler
└── README.md
```

---

## 🔍 What Does It Do?

This application takes 14 patient health parameters as input and predicts whether the patient is at **High Risk** or **Low Risk** of developing coronary heart disease within 10 years.

### Input Features

| Feature | Description |
|---|---|
| Gender | Male / Female |
| Age | Patient age |
| Current Smoker | Yes / No |
| Cigarettes Per Day | Daily cigarette count |
| Blood Pressure Medication | Yes / No |
| Prevalent Stroke | Yes / No |
| Prevalent Hypertension | Yes / No |
| Diabetes | Yes / No |
| Total Cholesterol | Blood cholesterol level |
| Systolic BP | Upper blood pressure reading |
| Diastolic BP | Lower blood pressure reading |
| BMI | Body Mass Index |
| Heart Rate | Beats per minute |
| Glucose | Blood glucose level |

### Output
- ✅ **Low Risk** — Patient likely has No Heart Disease
- ⚠️ **High Risk** — Patient likely has Heart Disease

---

## 🤖 Models Trained & Compared

Nine classifiers were evaluated and compared using Accuracy, F1-Score, Precision, and Recall:

| Model | Notes |
|---|---|
| Random Forest ✅ | **Best model — selected for deployment** |
| XGBoost | Strong performance |
| Gradient Boosting | Good generalization |
| AdaBoost | Moderate performance |
| Logistic Regression | Baseline linear model |
| SVM | Effective but slower |
| KNN | Distance-based approach |
| Decision Tree | Interpretable but overfits |
| Naive Bayes | Probabilistic baseline |

**Final model accuracy: ~90.6%** using Random Forest Classifier.

---

## 👥 Who Uses It?

- **Doctors & Clinicians** — Quick risk screening during consultations
- **Healthcare Researchers** — Studying cardiovascular risk factors
- **Medical Students** — Learning about predictive modeling in healthcare
- **ML/Data Science Students** — Reference project for classification + deployment

---

## 🌍 Real-World Impact

Heart disease is the **#1 cause of death globally**, accounting for over 17 million deaths per year (WHO). Early prediction can:

- Enable **early intervention** before symptoms appear
- Help doctors **prioritize high-risk patients** for further testing
- Encourage **lifestyle changes** (diet, exercise, quitting smoking) before it's too late
- **Reduce healthcare costs** by preventing emergency hospitalizations
- Make risk screening accessible in **low-resource clinical settings**

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| pandas / numpy | Data preprocessing |
| scikit-learn | Model training, scaling, evaluation |
| XGBoost | Gradient boosting classifier |
| imbalanced-learn (resample) | Handling class imbalance |
| pickle | Model serialization |
| Streamlit | Web application deployment |

---

## ⚙️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction
```

### 2. Install dependencies
```bash
pip install streamlit scikit-learn xgboost pandas numpy
```

### 3. Run the app
```bash
streamlit run Heart_diseases_app.py
```
<img width="1785" height="1054" alt="Screenshot 2026-05-05 222402" src="https://github.com/user-attachments/assets/d7882587-c362-4b7b-92cf-6582052d9d5e" />

---
 Then open your browser at `http://localhost:8501/`
---

## 🐛 Problems Faced & How I Fixed Them

### Problem 1: Incorrect Predictions from the App
**Issue:** The Streamlit app was only collecting 7 input fields (Diabetes, Cholesterol, Systolic BP, Diastolic BP, BMI, Heart Rate, Glucose) but the trained model required all **14 features** in the exact order the scaler was trained on.

**Fix:** Added all missing input fields to the app — Gender, Age, Current Smoker, Cigarettes Per Day, BP Medication, Prevalent Stroke, and Prevalent Hypertension. Ensured the `np.array` feature order matches exactly what `StandardScaler` was fitted on.

---

### Problem 2: Only Last Model Saved in Results DataFrame
**Issue:** The `pd.concat()` line was placed **outside the for loop**, so it only appended the last classifier (XGBClassifier) to `results_df` instead of all 9 models.

**Fix:** Instead of using `pd.concat` inside the loop (which also caused a `FutureWarning` due to empty DataFrame initialization), replaced the approach with a plain Python list:
```python
rows = []
for clf in classifiers:
    # ... train and evaluate ...
    rows.append({...})          # append inside loop
results_df = pd.DataFrame(rows) # build once after loop
```

---

### Problem 3: FutureWarning on DataFrame Concatenation
**Issue:** Initializing `results_df = pd.DataFrame(columns=[...])` and concatenating into it triggered a pandas `FutureWarning` about concatenation with empty or all-NA entries.

**Fix:** Eliminated the empty DataFrame entirely. Using a list of dicts and building the DataFrame in one shot after the loop avoids this warning completely.

---

### Problem 4: Class Imbalance in Dataset
**Issue:** The original dataset had a heavy class imbalance — far fewer positive (CHD = 1) cases than negative (CHD = 0), causing the model to be biased toward predicting "No Heart Disease."

**Fix:** Used `sklearn.utils.resample` to upsample the minority class to match the majority class size, creating a balanced dataset before training.

---

## 📊 Dataset

Based on the **Framingham Heart Study** dataset — a landmark longitudinal cardiovascular study. The dataset contains patient records with clinical measurements and a binary target variable `TenYearCHD` (1 = developed CHD within 10 years, 0 = did not).

- Rows: ~4,240 patients
- Target: `TenYearCHD` (binary)
- Preprocessing: Dropped `education` column, filled missing values with mode/median, balanced classes via upsampling

---

## 📄 License

This project is for educational purposes. Dataset sourced from the Framingham Heart Study via Kaggle.

---

## 🙋 Author

**Your Name**  
B.Tech Student | KIIT University  
[GitHub](https://github.com/your-username) · [LinkedIn](https://linkedin.com/in/your-profile)
