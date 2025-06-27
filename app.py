import streamlit as st
from recommender import movies

st.set_page_config(page_title="🎬 Movie Explorer", layout="wide")
st.title("🎥 Movie Explorer")
st.markdown("Explore movies by genre 👇")

all_genres = sorted({genre for genres in movies['genres'] for genre in genres})
selected_genre = st.selectbox("🎭 Select a Genre", all_genres)

if selected_genre:
    genre_movies = movies[movies['genres'].apply(lambda x: selected_genre in x)]

    st.subheader(f"🎬 Movies in Genre: {selected_genre}")
    for i in range(0, len(genre_movies), 2):
        row = genre_movies.iloc[i:i+2]
        cols = st.columns(len(row))
        for idx, (_, movie) in enumerate(row.iterrows()):
            with cols[idx]:
                st.markdown(f"### 🎬 [{movie['title']}]({movie['imdb_url']})", unsafe_allow_html=True)
                st.markdown(f"**📅 Release Date:** {movie.get('release_date', 'N/A')}")
                st.markdown(f"**🏷️ Genres:** {', '.join(movie['genres'])}")
                st.markdown(f"**🔖 Tags:** {', '.join(movie['tags']) if movie['tags'] else 'N/A'}")
                rating = movie.get('vote_average', 'N/A')
                st.markdown(f"**🌟 Rating:** {rating} / 10")
                try:
                    popularity = round(float(movie['popularity']), 2)
                except:
                    popularity = "N/A"
                st.markdown(f"**🔥 Popularity:** {popularity}")
                overview = movie['overview']
                st.caption(overview[:300] + "..." if len(overview) > 300 else overview)
                st.markdown("---")
