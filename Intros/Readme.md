# 🧪 ML-Experiments / Intros

> A beginner-friendly collection of Jupyter Notebooks covering the **core data preprocessing techniques** used in every Machine Learning pipeline.

---

## 📌 What Is This?

This repository is a hands-on **introduction to Machine Learning preprocessing** — the essential first steps before training any ML model. Each notebook focuses on one key concept, with clean code, explanations, and examples using real or built-in datasets.

Think of it as your **ML Data Prep Starter Kit**.

---

## 🎯 Purpose

Before feeding data into an ML model, raw data must be:
- Cleaned (handling missing values)
- Encoded (converting categories to numbers)
- Scaled (normalizing ranges)
- Split (separating training and testing sets)

This repo walks through each of these steps — **one notebook at a time** — so you can understand and apply them independently.

---

## 📁 Notebook Overview

| Notebook | Topic | What It Does |
|---|---|---|
| `BuiltIn_DataSets.ipynb` | Built-in Datasets | Explores datasets available via scikit-learn (Iris, Boston, etc.) |
| `Train_Test_Split.ipynb` | Train/Test Split | Splits data into training and testing sets to evaluate model performance |
| `Feature_Scaling.ipynb` | Feature Scaling | Scales features to a common range using Min-Max or similar techniques |
| `standardScaler.ipynb` | Standard Scaler | Standardizes features by removing the mean and scaling to unit variance |
| `Categorical_Encoding.ipynb` | Categorical Encoding | Converts text/category columns into numeric values using Label Encoding |
| `OneHotEncoder.ipynb` | One-Hot Encoding | Transforms categorical variables into binary columns (0s and 1s) |
| `Data_Imputation.ipynb` | Data Imputation | Handles missing values using strategies like mean, median, and mode |




---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/ojaspaul123/ML-Experiments.git
cd ML-Experiments/Intros
```

### 2. Install Dependencies
```bash
pip install numpy pandas scikit-learn matplotlib jupyter
```

### 3. Launch Jupyter Notebook
```bash
jupyter notebook
```

Then open any `.ipynb` file from the browser interface.

---

## 🛠️ Requirements

- Python 3.7+
- Jupyter Notebook or JupyterLab
- Libraries: `numpy`, `pandas`, `scikit-learn`, `matplotlib`

---



## 📚 Concepts Covered

```
Raw Data
   │
   ├── Missing Values?        → Data_Imputation.ipynb
   ├── Categorical Columns?   → Categorical_Encoding.ipynb
   │                            OneHotEncoder.ipynb
   ├── Need Scaling?          → Feature_Scaling.ipynb
   │                            standardScaler.ipynb
   ├── Using Built-in Data?   → BuiltIn_DataSets.ipynb
   └── Ready to Model?        → Train_Test_Split.ipynb
```

---

## 🤝 Contributing

Contributions are welcome! To contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-topic`)
3. Add your notebook with proper markdown explanations
4. Open a Pull Request

---

## 👤 Author

**ojaspaul123**
- GitHub: [@ojaspaul123](https://github.com/ojaspaul123)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
