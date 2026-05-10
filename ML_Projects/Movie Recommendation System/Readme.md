# 🎬 Movie Recommendation System - TMDB Dataset using cosine similarity

A content-based movie recommendation system built with Python, scikit-learn, and Streamlit — deployed as an interactive web app that suggests similar movies using NLP and cosine similarity on the TMDB 5000 dataset.

<img width="1452" height="840" alt="image" src="https://github.com/user-attachments/assets/2f3e45a9-7762-4d2d-a6f6-bb15f0fe1acc" />  <img width="959" height="560" alt="Screenshot 2026-05-11 004544" src="https://github.com/user-attachments/assets/d4525334-2dd9-42df-a945-0b2e9b9bc23f" /> 
 


## App Link **http://localhost:8501/**
---

## 📌 Table of Contents

- [What Does It Do?](#what-does-it-do)
- [Who Uses It?](#who-uses-it)
- [Real-World Impact](#real-world-impact)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Issues Faced & How I Resolved Them](#issues-faced--how-i-resolved-them)

---

## 🤔 What Does It Do?

This app takes a movie selected by the user and recommends **5 similar movies** based on content similarity. It analyzes the following features from each movie:

- **Overview** (plot description)
- **Genres**
- **Keywords**
- **Top 3 Cast members**
- **Director**

These features are combined into a single "tag" per movie, vectorized using **CountVectorizer**, and compared using **Cosine Similarity**. The top 5 most similar movies are returned along with their **official posters fetched live from the TMDB API**.

---

## 👥 Who Uses It?

| User Type | Use Case |
|---|---|
| **Movie enthusiasts** | Discover new films similar to ones they already love |
| **Casual viewers** | Get instant recommendations without scrolling through Netflix endlessly |
| **Students & developers** | Learn how NLP-based recommendation systems work in practice |
| **Data science learners** | A hands-on reference project for content-based filtering |

---

## 🌍 Real-World Impact

Recommendation systems are one of the most commercially valuable applications of machine learning today:

- **Streaming platforms** like Netflix, Prime Video, and Disney+ rely heavily on recommendation engines to retain users and drive watch time.
- Netflix estimates its recommendation system saves the company **over $1 billion per year** by reducing churn.
- Content-based filtering (the approach used here) is the foundation of many production-grade systems, especially for **cold-start problems** where user history is unavailable.
- This project demonstrates how even a **lightweight NLP pipeline** (bag-of-words + cosine similarity) can produce surprisingly relevant recommendations — making it a practical teaching tool and a starting point for more complex collaborative filtering or hybrid approaches.

---

## 📁 Project Structure

```
movie-recommendation-system/
│
├── Movie_Recommendation_System.ipynb   # Data preprocessing & model building (Google Colab)
├── Movie_app.py                        # Streamlit web application
├── movies.pkl                          # Serialized DataFrame (movie_id, title, tags) ## Large File (doesn't Uploaded yet)
├── similarity.pkl                      # Precomputed cosine similarity matrix         ## Large File (doesn't Uploaded yet)
└── README.md
```

> **Note:** The raw dataset files (`tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`) are not included due to size. Download them programmatically using `kagglehub`:

```python
import kagglehub

# Download latest version
path = kagglehub.dataset_download("tmdb/tmdb-movie-metadata")
print("Path to dataset files:", path)
```

Or download manually from [Kaggle — TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

---

## ⚙️ How It Works

```
Raw CSV Data (TMDB 5000)
        │
        ▼
  Data Merging & Cleaning
  (movies + credits on 'title')
        │
        ▼
  Feature Extraction
  (genres, keywords, cast top-3, director, overview)
        │
        ▼
  Tag Construction
  (all features collapsed into one text blob per movie)
        │
        ▼
  Text Preprocessing
  (lowercasing → Porter Stemming)
        │
        ▼
  CountVectorizer (max 5000 features, stop words removed)
        │
        ▼
  Cosine Similarity Matrix (4806 × 4806)
        │
        ▼
  Serialized → movies.pkl + similarity.pkl
        │
        ▼
  Streamlit App → Top 5 Recommendations + TMDB Posters
```

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Data Processing | `pandas`, `numpy`, `ast` |
| NLP | `nltk` (PorterStemmer), `scikit-learn` (CountVectorizer) |
| Similarity | `scikit-learn` (cosine_similarity) |
| Serialization | `pickle` |
| Web App | `Streamlit` |
| Poster Fetching | TMDB API (`requests`) |
| Development | Google Colab + VS Code |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/campusx-official/movie-recommender-system-tmdb-dataset/tree/main
cd movie-recommendation-system
```

### 2. Install dependencies
```bash
pip install streamlit pandas scikit-learn nltk requests
```

### 3. Run the app
```bash
streamlit run Movie_app.py
```

> Make sure `movies.pkl` and `similarity.pkl` are in the same directory as `Movie_app.py`.

### 4. Get a TMDB API Key (optional but recommended)
Register at [https://www.themoviedb.org/](https://www.themoviedb.org/) and replace the API key in `Movie_app.py`:
```python
url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY"
```

---

## 🐛 Issues Faced & How I Resolved Them

### 1. `KeyError` on pickle load — mismatched variable name
**Problem:** The notebook saved the file as `movies_dict.pkl` but `Movie_app.py` was trying to load `movies.pkl` (and vice versa for column names).  
**Fix:** Ensured consistent naming between the notebook's `pickle.dump()` call and the app's `pickle.load()` call. Standardized the saved object to a dictionary (`movies.to_dict()`) and reconstructed it as a DataFrame in the app.

---

### 2. Poster not loading — TMDB API returning `None` for `poster_path`
**Problem:** Some movies in the dataset don't have a poster on TMDB, causing the app to crash when trying to build the image URL.  
**Fix:** Added a conditional check in `fetch_poster()`:
```python
if 'poster_path' in data and data['poster_path']:
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
else:
    return "https://via.placeholder.com/500x750?text=No+Image"
```

---

### 3. Similarity matrix was too large to load quickly
**Problem:** The cosine similarity matrix for ~4800 movies is a 4806×4806 float matrix (~185 MB), making pickle load slow.  
**Fix:** Accepted this as a one-time cost on app startup. For production, this could be replaced with approximate nearest neighbor search (e.g., `faiss` or `annoy`) or a vector database.

---

### 4. Multi-word names causing incorrect matching (e.g., "Sam Worthington" → treated as two separate tokens)
**Problem:** Cast names with spaces were being split by the vectorizer, so "Sam" and "Worthington" were treated as separate features, diluting the signal.  
**Fix:** Used a `collapse()` function that removes spaces from multi-word names before tagging:
```python
def collapse(L):
    return [i.replace(" ", "") for i in L]
# "Sam Worthington" → "SamWorthington" (single token)
```

---

### 5. Stemming over-aggressively reducing keywords
**Problem:** PorterStemmer was converting some meaningful words to unrecognizable stems (e.g., `"loving"` → `"love"` is fine, but edge cases like `"flies"` → `"fli"` caused noise).  
**Fix:** Acknowledged this as a known tradeoff of Porter Stemming. For improved accuracy, a lemmatizer (`WordNetLemmatizer` from NLTK) could be used instead — it produces real dictionary words.

---

## 📄 License

This project is open-source and free to use for learning purposes.

---

## 🙌 Acknowledgements

- [TMDB](https://www.themoviedb.org/) for the movie dataset and poster API
- [Kaggle — TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) for the raw data
- [Streamlit](https://streamlit.io/) for making ML app deployment effortless
