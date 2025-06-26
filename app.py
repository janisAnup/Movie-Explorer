import streamlit as st
from recommender import movies

# ---------- Helper ----------
def safe_round(value, decimals=2):
    try:
        return round(float(value), decimals)
    except:
        return "N/A"

# ---------- Streamlit Config ----------
st.set_page_config(page_title="🎬 Movie Explorer", layout="wide")
st.title("🎬 Movie Explorer by Genre")
st.markdown("Select a genre below to explore recommended movies 👇")

# ---------- Genre Dropdown ----------
all_genres = sorted({genre for sublist in movies['genres'] for genre in sublist})
selected_genre = st.selectbox("🎭 Choose a genre:", ["-- Select Genre --"] + all_genres)

# ---------- Show Genre Results ----------
if selected_genre and selected_genre != "-- Select Genre --":
    st.subheader(f"🎬 Movies in Genre: {selected_genre}")
    genre_movies = movies[movies['genres'].apply(lambda x: selected_genre in x)]

    if genre_movies.empty:
        st.warning("No movies found in this genre.")
    else:
        max_movies = st.slider("🔢 Number of movies to display:", 5, 30, 10)
        genre_movies = genre_movies.sort_values(by='popularity', ascending=False).head(max_movies)

        for i in range(0, len(genre_movies), 2):
            row = genre_movies.iloc[i:i+2]
            cols = st.columns(len(row))
            for idx, (index, movie) in enumerate(row.iterrows()):
                with cols[idx]:
                    st.markdown(f"### 🎬 [{movie['title']}]({movie['imdb_url']})", unsafe_allow_html=True)
                    st.markdown(f"**📅 Release Date:** {movie.get('release_date', 'N/A')}")
                    st.markdown(f"**🎭 Cast:** {', '.join(movie['top_actors']) if movie['top_actors'] else 'N/A'}")
                    st.markdown(f"**🎬 Director:** {movie.get('director', 'N/A')}")
                    st.markdown(f"**🏷️ Genres:** {', '.join(movie['genres'])}")
                    st.markdown(f"**🔖 Tags:** {', '.join(movie['tags']) if movie['tags'] else 'N/A'}")
                    st.markdown(f"**🌟 Rating:** {movie.get('vote_average', 'N/A')} / 10")
                    st.markdown(f"**🔥 Popularity:** {safe_round(movie.get('popularity'))}")
                    overview = movie['overview']
                    st.caption(overview[:300] + "..." if len(overview) > 300 else overview)
                    st.markdown("---")


