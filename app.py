import streamlit as st
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- LOAD DATA ----------------
with open("movie_dict.pkl", "rb") as f:
    data = pickle.load(f)

movie_dictionary = data["movie_dict"]
df = data["df"]

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Netflix Movie Recommender",
    layout="wide"
)

# ---------------- NETFLIX CSS ----------------
st.markdown("""
<style>
.stApp {
    background-color: #141414;
    color: white;
}

h1 {
    color: #E50914;
    font-weight: 800;
    text-align: center;
    letter-spacing: 2px;
}

/* Dropdown */
.stSelectbox div {
    background-color: #222;
    color: white;
}

/* Button */
.stButton>button {
    background-color: #E50914;
    color: white;
    font-weight: bold;
    border-radius: 6px;
    padding: 10px 20px;
    border: none;
}
.stButton>button:hover {
    background-color: #f6121d;
}

/* Movie Card */
.movie-card {
    background-color: #1f1f1f;
    border-radius: 12px;
    padding: 10px;
    margin-bottom: 25px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.7);
    transition: transform 0.3s;
}
.movie-card:hover {
    transform: scale(1.05);
}

.movie-title {
    font-size: 17px;
    font-weight: bold;
    margin-top: 8px;
}

.movie-genre {
    font-size: 13px;
    color: #b3b3b3;
}

.movie-overview {
    font-size: 12px;
    color: #dcdcdc;
    margin-top: 6px;
    line-height: 1.4;
}
</style>
""", unsafe_allow_html=True)

# ---------------- IMAGE QUALITY FIX ----------------
def get_high_quality_image(url, width=600, height=900):
    if "UX" in url:
        url = url.replace("UX67", f"UX{width}")
    if "UY" in url:
        url = url.replace("UY98", f"UY{height}")
    if "CR" in url:
        url = url.replace("CR0,0,67,98", f"CR0,0,{width},{height}")
    return url

# ---------------- RECOMMEND FUNCTION ----------------
def recommend(movie, n=6):
    movie_vector = np.array(movie_dictionary[movie]).reshape(1, -1)
    similarities = {}

    for m, vec in movie_dictionary.items():
        if m != movie:
            similarities[m] = cosine_similarity(
                movie_vector,
                np.array(vec).reshape(1, -1)
            )[0][0]

    return sorted(similarities, key=similarities.get, reverse=True)[:n]

# ---------------- UI HEADER ----------------
st.markdown("<h1>NETFLIX MOVIE RECOMMENDER</h1>", unsafe_allow_html=True)

st.markdown("### 🍿 Choose a movie you like")

movie = st.selectbox("", movie_dictionary.keys())
btn = st.button("Recommend")

# ---------------- DISPLAY MOVIES ----------------
if btn:
    movies = recommend(movie)
    cols = st.columns(5)  # Netflix-style row

    for idx, title in enumerate(movies):
        with cols[idx % 5]:
            genre = df.loc[df["Series_Title"] == title, "Genre"].iloc[0]
            poster = df.loc[df["Series_Title"] == title, "Poster_Link"].iloc[0]
            overview = df.loc[df["Series_Title"] == title, "Overview"].iloc[0]

            st.image(get_high_quality_image(poster), use_container_width=True)

            st.markdown(f"""
            <div class="movie-card">
                <div class="movie-title">{title}</div>
                <div class="movie-genre">{genre}</div>
                <div class="movie-overview">{overview[:120]}...</div>
            </div>
            """, unsafe_allow_html=True)
