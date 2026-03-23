import streamlit as st
import pickle
from concurrent.futures import ThreadPoolExecutor
import os
# ---------------- CONFIG ----------------
st.set_page_config(page_title="Movie Recommender", layout="wide")

# ---------------- LOAD DATA ----------------
BASE_DIR = os.path.dirname(__file__)

movies = pickle.load(open(os.path.join(BASE_DIR, "movie_dict.pkl"), "rb"))
similarity = pickle.load(open(os.path.join(BASE_DIR, "similarity.pkl"), "rb"))


# ---------------- CACHE FUNCTION ----------------


import requests


@st.cache_data
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c688b89d3846ad57f459b15fd60dc98a"
        response = requests.get(url, timeout=5)
        data = response.json()
        return "https://image.tmdb.org/t/p/w200/" + data['poster_path']

    except:
        return "https://via.placeholder.com/200x300?text=No+Image"
# ---------------- RECOMMEND FUNCTION ----------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    movie_ids = []

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        movie_ids.append(movies.iloc[i[0]].movie_id)

    # Parallel fetch posters
    with ThreadPoolExecutor() as executor:
        posters = list(executor.map(fetch_poster, movie_ids))

    return recommended_movies, posters


# ---------------- UI ----------------
st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])

