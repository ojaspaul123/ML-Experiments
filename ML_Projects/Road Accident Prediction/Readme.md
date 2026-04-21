# 🚗 Accident Severity Prediction - Machine Learning Pipeline

A machine learning web application that predicts the severity of road accidents — **Slight Injury**, **Serious Injury**, or **Fatal Injury** — based on real-world accident features using a Random Forest Classifier served through a Streamlit interface.

---

## 🖥️ App Preview

<img width="1918" height="1113" alt="Screenshot 2026-04-21 134110" src="https://github.com/user-attachments/assets/5a5f66c4-0c32-4ed7-88da-4443f7a26695" />
<img width="1918" height="1117" alt="Screenshot 2026-04-21 134134" src="https://github.com/user-attachments/assets/78464e9a-007e-4bef-9ba1-c94598f9cee4" />
<img width="1917" height="1111" alt="Screenshot 2026-04-21 134152" src="https://github.com/user-attachments/assets/9aae11c8-2c93-47a6-a103-e14ab08bde18" />



> The app provides a sidebar with 31 input fields. Fill in the accident details and click **Predict** to see the result instantly.

---

## 🔍 What I Built

A full end-to-end ML pipeline that:

- Loads and preprocesses a road accident dataset (`pipe_dataset.csv`)
- Engineers a time-based feature (`Hour_of_day`) from timestamp data
- Handles class imbalance using **RandomOverSampler**
- Fills missing values using **SimpleImputer** with column-specific strategies
- Encodes categorical features using **OneHotEncoder**
- Selects the top 50 features using **Chi-squared (χ²) feature selection**
- Trains a **Random Forest Classifier**
- Saves the entire pipeline as a **pickle file** (`pipe_file.pkl`)
- Serves predictions via a **Streamlit web app**

---

## 🗂️ Project Structure

```
ML_Projects/
│
├── Accident_Prediction.ipynb   # Model training notebook
├── Accident_predict.py         # Streamlit web app
├── pipe_dataset.csv            # Dataset
├── pipe_file.pkl               # Trained model pipeline (pickle)
├── car_accident.png            # App banner image
└── README.md                   # Project documentation
```

---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas & NumPy | Data processing |
| Scikit-learn | ML pipeline, model, preprocessing |
| Imbalanced-learn | Oversampling (RandomOverSampler) |
| Pickle | Model serialization |
| Streamlit | Web app UI |
| PIL (Pillow) | Image display |

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/your-username/accident-severity-prediction.git
cd accident-severity-prediction
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app
```bash
streamlit run Accident_predict.py
```
> The app will open at **http://localhost:8501**

---

## 📦 Requirements

```
streamlit
numpy
pandas
scikit-learn
imbalanced-learn
Pillow
```

Save as `requirements.txt` in your project root.

---

## 🧠 ML Pipeline Overview

```
Raw CSV Data
    ↓
Feature Engineering  (Hour_of_day from Time column)
    ↓
Label Encoding       (Target: Accident_severity → 0, 1, 2)
    ↓
RandomOverSampler    (Balance classes)
    ↓
Train/Test Split     (80/20)
    ↓
trf1: SimpleImputer  (Fill missing values per column)
    ↓
trf2: OneHotEncoder  (Encode all categorical columns)
    ↓
trf4: SelectKBest    (Chi2, top 50 features)
    ↓
trf5: RandomForestClassifier
    ↓
pipe_file.pkl        (Saved pipeline)
```

---

## ⚠️ Problems Faced & Solutions
<img width="1532" height="1072" alt="Screenshot 2026-04-21 134302" src="https://github.com/user-attachments/assets/0bfa6e62-20e0-4878-90b4-ab73922681d9" />

### ❌ Problem 1: Streamlit not running — "missing ScriptRunContext" warning
**Cause:** The app was being executed with `python Accident_predict.py` instead of the correct Streamlit command.

**Fix:**
```bash
# Wrong ❌
python Accident_predict.py

# Correct ✅
streamlit run Accident_predict.py

# Alternative if above doesn't work ✅
python -m streamlit run Accident_predict.py
```

---

### ❌ Problem 2: `use_column_width` deprecation warning on image
**Cause:** The Streamlit parameter `use_column_width=True` is deprecated in newer versions.

**Fix:** Replace with the `use_container_width` parameter:
```python
# Old ❌
st.image(img, use_column_width=True)

# New ✅
st.image(img, use_container_width=True)
```

---

### ❌ Problem 3: Image file not found (`car_accident.png`)
**Cause:** The app referenced `car_accident.png` but the file was saved as `car_accident.jpg`.

**Fix:** Either rename the file or update the code to match the actual filename:
```python
img = Image.open('car_accident.png')   # ❌ file doesn't exist
img = Image.open('car_accident.jpg')   # ✅ correct filename
```

---

### ❌ Problem 4: Notebook used Google Colab's `files.upload()` — breaks locally
**Cause:** `from google.colab import files` only works inside Google Colab, not in a local environment.

**Fix:** Replace with a direct `pd.read_csv()` call:
```python
# Colab ❌
from google.colab import files
uploaded = files.upload()

# Local ✅
df = pd.read_csv('pipe_dataset.csv')
```

---

## 📊 Model Output

| Predicted Class | Label |
|----------------|-------|
| 0 | Fatal Injury |
| 1 | Serious Injury |
| 2 | Slight Injury |

---

## 🙋 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
