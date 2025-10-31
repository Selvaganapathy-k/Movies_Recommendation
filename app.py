import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

st.set_page_config(page_title="🎬 MovieLens Recommender", layout="wide")

# ----------------------------
# Load Data and Model
# ----------------------------
@st.cache_data
def load_data():
    ratings = pd.read_csv("ratings.csv", encoding="utf-8")
    try:
        movies = pd.read_csv("movies.csv", encoding="utf-8")
    except UnicodeDecodeError:
        movies = pd.read_csv("movies.csv", encoding="latin1")

    # Encode users & movies same as training
    user_map = {uid: idx for idx, uid in enumerate(ratings['userId'].unique())}
    movie_map = {mid: idx for idx, mid in enumerate(ratings['movieId'].unique())}

    ratings['user_enc'] = ratings['userId'].map(user_map)
    ratings['movie_enc'] = ratings['movieId'].map(movie_map)
    return ratings, movies, user_map, movie_map

ratings, movies, user_map, movie_map = load_data()

@st.cache_resource
def load_recommender():
    return load_model("your_trained_movielens_model.h5", compile=False) # safer for inference

model = load_recommender()

# ----------------------------
# Recommend Movies Function
# ----------------------------
def recommend_movies(user_id, top_n=10):
    if user_id not in user_map:
        return None

    user_idx = user_map[user_id]
    watched = ratings[ratings['userId'] == user_id]['movieId'].values
    unseen = movies[~movies['movieId'].isin(watched)].copy()
    unseen['movie_enc'] = unseen['movieId'].map(movie_map)
    unseen = unseen.dropna(subset=['movie_enc'])

    user_array = np.array([user_idx] * len(unseen))
    movie_array = unseen['movie_enc'].astype(int).values
    preds = model.predict([user_array, movie_array], verbose=0).flatten()
    unseen['pred_rating'] = preds
    suggestions = unseen.sort_values(by='pred_rating', ascending=False).head(top_n)
    return suggestions[['title', 'genres', 'pred_rating']]

# ----------------------------
# Streamlit UI
# ----------------------------
st.title("🎬 MovieLens Recommendation System")
st.write("### Get personalized movie recommendations based on collaborative filtering")

user_ids = sorted(ratings['userId'].unique())
selected_user = st.selectbox("Select User ID", user_ids)

if st.button("Recommend Movies"):
    result = recommend_movies(selected_user)
    if result is None or len(result) == 0:
        st.error("No recommendations available.")
    else:
        st.success(f"Top recommendations for user {selected_user}:")
        st.dataframe(result.style.format({"pred_rating": "{:.2f}"}))
