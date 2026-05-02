# 📱 SMS Spam / Scam Detector

A machine learning-powered web application that detects whether an SMS message is **spam/scam** or **legitimate (ham)**. Built with Scikit-learn and deployed via a Streamlit interface.

---

## 🖥️ Demo

| Spam Detected | Ham (Not Spam) |
|---|---|
| <img width="1919" height="1120" alt="Screenshot 2026-05-03 010933" src="https://github.com/user-attachments/assets/9657b087-3c58-4798-b013-9c5359cf6409" />
| <img width="1903" height="1116" alt="Screenshot 2026-05-03 010905" src="https://github.com/user-attachments/assets/802589db-c983-4481-b4f2-ab59dca2ec4c" />
|

> **Spam input:** *"Congratulations ur awarded 500 of CD vouchers or 125gift guaranteed & Free entry 2 100 wkly draw..."*
> **Ham input:** *"I'm gonna be home soon and I don't want to talk about this stuff anymore tonight, k?"*

---

## 📁 Project Structure

```
SMS-Scam-Detector/
│
├── Scam_Detection.ipynb       # Full ML pipeline: EDA, preprocessing, training, evaluation
├── Scam_Detection.py          # Streamlit web app (frontend)
├── scam_detection.pkl         # Saved model + vectorizer (logistic regression + TF-IDF)
├── SMS_Spam_Dataset.csv       # Training dataset (labeled SMS messages)
│
└── screenshots/
    ├── spam_result.png
    └── ham_result.png
```

---

## ⚙️ How It Works

### 1. Data Preprocessing
- Lowercasing, URL removal, punctuation stripping
- Tokenization using NLTK
- Stopword removal
- Porter Stemming

### 2. Data Balancing
- Dataset is imbalanced (more ham than spam)
- Applied **RandomOverSampler** from `imbalanced-learn` to balance classes

### 3. Feature Extraction
- **TF-IDF Vectorizer** converts cleaned text into numerical feature vectors

### 4. Models Trained & Compared

| Model | Notes |
|---|---|
| Random Forest | Ensemble tree-based classifier |
| Logistic Regression ✅ | **Selected for deployment** (best balance of accuracy & speed) |
| SVM (Linear Kernel) | High accuracy, slower inference |
| Voting Ensemble | Hard voting across all three models |

### 5. Deployment
- Final model (`logistic_regression`) and `tfidf_vectorizer` saved as `scam_detection.pkl` using `pickle`
- Loaded in **Streamlit** app for real-time inference

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install streamlit scikit-learn nltk imbalanced-learn pandas numpy
```

Also download required NLTK resources:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### Run the App
<img width="1535" height="1078" alt="Screenshot 2026-05-03 011239" src="https://github.com/user-attachments/assets/471fffbe-9fc0-4e69-b84f-169bd9b01138" />

```bash
python -m streamlit run Scam_Detection.py
```

Then open your browser at `http://localhost:8501`

---

## 🧪 Exploratory Data Analysis (in Notebook)

The notebook includes:
- **Top 20 N-Grams** — most frequent word pairs in the dataset
- **Class Distribution** — spam vs. ham balance
- **Message Length Distribution** — spam messages tend to be longer
- **Word Clouds** — visual patterns for spam vs. ham vocabulary

---

## 🌍 Real-World Impact

SMS scams cost individuals and businesses **billions of dollars annually**. This tool provides:

- **Individual protection** — users can verify suspicious texts before clicking links or calling numbers
- **Telecom integration** — can be embedded in carrier-level spam filters
- **Enterprise security** — helps organizations protect employees from phishing via SMS (smishing)
- **Awareness tool** — students and developers can learn how NLP powers safety systems

**Who uses it?**
- Everyday mobile users wanting a second opinion on suspicious messages
- Developers building SMS filtering pipelines
- Students learning applied NLP and machine learning
- Cybersecurity researchers studying scam patterns

---

## 🐛 Issues Faced & How They Were Fixed

### 1. Imbalanced Dataset
**Problem:** The dataset had far more ham messages than spam, causing the model to be biased toward predicting "not spam."

**Fix:** Applied `RandomOverSampler` from `imbalanced-learn` to oversample the minority (spam) class before training.

---

### 2. Model Selection for Deployment
**Problem:** The Voting Ensemble had marginally better accuracy but was too large and slow to serialize + serve in a lightweight Streamlit app.

**Fix:** Chose **Logistic Regression** for deployment — nearly identical accuracy, much faster inference, and smaller pickle size.

---

### 3. Pickle Compatibility
**Problem:** Saving individual model and vectorizer as separate `.pkl` files caused version mismatch issues when loading on different machines.

**Fix:** Both the model and vectorizer are saved together in a **single dictionary** inside one `.pkl` file:
```python
pickle.dump({"logistic_regression": lr_classifier, "tfidf_vectorizer": tfidf_vectorizer}, f)
```

---

### 4. Text Cleaning Pipeline Not Applied at Inference
**Problem:** During early testing, raw user input was passed directly to the vectorizer without preprocessing, leading to poor predictions.

**Fix:** The same `clean_text()` function used during training (lowercase → remove URLs → remove punctuation → tokenize → remove stopwords → stem) is applied to user input before vectorization in the Streamlit app.

---

### 5. NLTK Resources Not Found
**Problem:** `punkt` and `stopwords` were not available in fresh environments, causing `LookupError` at runtime.

**Fix:** Added explicit `nltk.download()` calls at the top of the notebook and documented them in the setup instructions.

---

## 📊 Dataset

- **Source:** [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/noorsaeed/scam-detection-dataset) via Kaggle
- **Size:** ~5,500 labeled SMS messages
- **Labels:** `0` = Ham (legitimate), `1` = Spam/Scam

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| ML Framework | Scikit-learn |
| NLP | NLTK |
| Data Handling | Pandas, NumPy |
| Balancing | imbalanced-learn |
| Web App | Streamlit |
| Model Persistence | Pickle |
| Development | Jupyter Notebook, VS Code |

---

## 📄 License

This project is for educational purposes. Feel free to fork, extend, and adapt it.

---

## 🙌 Acknowledgements

- [UCI SMS Spam Collection](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)
- [Streamlit](https://streamlit.io/) for rapid ML app deployment
- [NLTK](https://www.nltk.org/) for NLP utilities
