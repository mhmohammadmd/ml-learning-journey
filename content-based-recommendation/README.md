# 🎬 Content-Based Movie Recommendation System
[![Kaggle](https://img.shields.io/badge/Kaggle-Notebook-blue)](https://www.kaggle.com/code/greywolfmd/content-based-movie-recommendation-system)
## 📌 Overview
This project implements a content-based recommendation system using the MovieLens dataset.  
Movies are represented using TF-IDF vectors generated from genres and tag metadata.  
Cosine similarity is used to generate personalized recommendations.

---

## 🧠 Methodology

1. Data preprocessing
2. Content feature engineering (genres + tags)
3. TF-IDF vectorization
4. User profile construction
5. Cosine similarity ranking

---

## 📊 Evaluation
Future work includes implementing:
- Precision@K
- Recall@K
- Dimensionality reduction using TruncatedSVD

---

## 🛠 Tech Stack
- Python
- Pandas
- Scikit-learn
- TF-IDF
- Cosine Similarity

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
