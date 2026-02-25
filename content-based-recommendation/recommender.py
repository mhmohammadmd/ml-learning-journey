import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ContentBasedRecommender:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
        self.tfidf_matrix = None
        self.movies = None

    def fit(self, movies_df):
        self.movies = movies_df
        self.tfidf_matrix = self.vectorizer.fit_transform(movies_df['content'])

    def build_user_profile(self, liked_movie_indices):
        user_vectors = self.tfidf_matrix[liked_movie_indices]
        return user_vectors.mean(axis=0)

    def recommend(self, user_profile, top_n=10):
        similarity_scores = cosine_similarity(user_profile, self.tfidf_matrix)
        scores = similarity_scores.flatten()
        top_indices = scores.argsort()[-top_n:][::-1]
        return self.movies.iloc[top_indices][['title', 'genres']]
