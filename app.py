import streamlit as st
from recommender import movies

st.set_page_config(page_title="🎬 Movie Explorer by Genre", layout="wide")
st.title("🎥 Movie Explorer by Genre")
st.markdown("Select a genre to explore movies 👇")

# 🎭 Genre dropdown
all_genres = sorted({genre for sublist in movies['genres'] for genre in sublist})
selected_genre = st.selectbox("🎭 Choose Genre:", ["-- Select Genre --"] + all_genres)

# 🎬 Genre-based movie list
if selected_genre and selected_genre != "-- Select Genre --":
    st.subheader(f"🎬 Movies in Genre: {selected_genre}")
    genre_movies = movies[movies['genres'].apply(lambda x: selected_genre in x)].head(30)

    for i in range(0, len(genre_movies), 2):
        row = genre_movies.iloc[i:i+2]
        cols = st.columns(len(row))
        for idx, (index, movie) in enumerate(row.iterrows()):
            with cols[idx]:
                st.markdown(f"### 🎬 [{movie['title']}]({movie['imdb_url']})", unsafe_allow_html=True)
                st.markdown(f"**📅 Release Date:** {movie.get('release_date', 'N/A')}")
                st.markdown(f"**🏷️ Genres:** {', '.join(movie['genres'])}")
                st.markdown(f"**🔖 Tags:** {', '.join(movie['tags']) if movie['tags'] else 'N/A'}")
                st.markdown(f"**🌟 Rating:** {movie.get('vote_average', 'N/A')} / 10")
                try:
                    popularity_score = float(movie.get('popularity', 0))
                    st.markdown(f"**🔥 Popularity:** {round(popularity_score, 2)}")
                except:
                    st.markdown("**🔥 Popularity:** N/A")
                overview = movie['overview']
                st.caption(overview[:300] + "..." if len(overview) > 300 else overview)
                st.markdown("---")
else:
    st.info("Please select a genre from the dropdown above.")



