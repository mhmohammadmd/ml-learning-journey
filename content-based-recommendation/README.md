# 🎬 Content-Based Movie Recommendation System

[![Kaggle](https://img.shields.io/badge/Kaggle-Notebook-blue)](https://www.kaggle.com/code/greywolfmd/content-based-movie-recommendation-system)

---

## 📌 Overview

This project implements a **Content-Based Movie Recommendation System** using the **MovieLens 25M dataset**.

Movies are represented as high-dimensional feature vectors generated from:
- Genre metadata
- User-generated tags  

TF-IDF vectorization is applied to construct feature representations, and cosine similarity is used to rank movies based on content relevance.

The system is designed to scale to large datasets (25M+ ratings).

---

## 🧠 Methodology

### 1️⃣ Data Preprocessing
- Cleaning missing values  
- Merging movies, ratings, and tags  
- Text normalization  

### 2️⃣ Content Feature Engineering
- Combining genres and tags  
- Constructing unified textual corpus  

### 3️⃣ TF-IDF Vectorization
- Converting textual metadata into numerical vectors  
- Generating high-dimensional sparse matrix  

### 4️⃣ User Profile Construction
- Aggregating movie vectors weighted by user ratings  
- Creating personalized preference vectors  

### 5️⃣ Similarity Computation
- Cosine similarity between user profile and movie vectors  
- Ranking Top-N recommendations  

---

## 📊 Evaluation

Planned evaluation metrics:

- Precision@K  
- Recall@K  
- Mean Average Precision (MAP)  

Future improvements:
- Dimensionality reduction using TruncatedSVD  
- Hybrid Recommendation System (Content + Collaborative Filtering)  

---

## 📂 Dataset

This project uses the **MovieLens 25M dataset** provided by GroupLens Research.

Due to its large size (~250MB+), the dataset is not included in this repository.

Kaggle Dataset:  
https://www.kaggle.com/datasets/grouplens/movielens-25m

Kaggle input path used:
```
/kaggle/input/movielens-25m/
```

---

## ⚙️ Execution Environment

This project is optimized for execution on **Kaggle** due to dataset size constraints.

### ▶ Running on Kaggle
1. Open the Kaggle notebook  
2. Attach the MovieLens 25M dataset  
3. Run all cells  

### ▶ Running Locally

1. Download the dataset from Kaggle  
2. Create a folder named `data/`  
3. Place these files inside:
   - movies.csv  
   - ratings.csv  
   - tags.csv  

4. Update file paths in your script:

```python
ratings = pd.read_csv("data/ratings.csv")
```

---

## 🛠 Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- TF-IDF Vectorizer  
- Cosine Similarity  

---

## 🚀 Features

- Content-based filtering using TF-IDF  
- Cosine similarity ranking  
- Metadata-driven movie profiling  
- User preference vector modeling  
- Scalable to 25M+ records  

---

## 🚀 How to Run

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the project

- Open in Kaggle (Recommended)
- OR run locally using Jupyter Notebook

---

## 👤 Author

**Mohammad**  
B.Tech Computer Science  
NIT Srinagar  

---
