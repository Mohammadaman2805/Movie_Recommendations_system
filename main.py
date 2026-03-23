import streamlit as st
import pickle
import requests
import os
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Movie Recommender", layout="wide")

# ---------------- LOAD DATA ----------------
BASE_DIR = os.path.dirname(__file__)

movies = pickle.load(open(os.path.join(BASE_DIR, "movie_dict.pkl"), "rb"))
vectors = pickle.load(open(os.path.join(BASE_DIR, "vectors.pkl"), "rb"))

# ---------------- FETCH POSTER ----------------
@st.cache_data
def fetch_poster(movie_id):
    try:
        api_key = "c688b89d3846ad57f459b15fd60dc98a"
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"

        response = requests.get(url)
        data = response.json()

        if response.status_code != 200 or data.get('poster_path') is None:
            return "https://via.placeholder.com/200x300?text=No+Image"

        return "https://image.tmdb.org/t/p/w200/" + data['poster_path']

    except:
        return "https://via.placeholder.com/200x300?text=Error"

# ---------------- RECOMMEND ----------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index

    if len(movie_index) == 0:
        return [], []

    movie_index = movie_index[0]

    # compute similarity dynamically
    distances = cosine_similarity([vectors[movie_index]], vectors)[0]

    movie_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    names, posters = [], []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        names.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))

    return names, posters

# ---------------- UI ----------------
st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox("Select a movie", movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)

    if not names:
        st.error("No recommendations found")
    else:
        cols = st.columns(5)

        for i in range(len(names)):
            with cols[i]:
                st.text(names[i])
                st.image(posters[i], use_container_width=True)


import sys
st.write(sys.version)
