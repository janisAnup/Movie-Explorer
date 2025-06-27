import pandas as pd
import ast
import streamlit as st

@st.cache_data
def load_movies():

    movies = pd.read_csv("movies_metadata.csv", low_memory=False)

    movies = movies.dropna(subset=["title", "genres", "overview"])

    def parse_genres(genre_str):
        try:
            genres = ast.literal_eval(genre_str)
            return [genre['name'] for genre in genres if 'name' in genre]
        except:
            return []

    movies['genres'] = movies['genres'].apply(parse_genres)

    movies['title_lower'] = movies['title'].str.lower()

    movies['overview'] = movies['overview'].fillna('')
    movies['vote_average'] = pd.to_numeric(movies['vote_average'], errors='coerce').fillna(0)
    movies['popularity'] = pd.to_numeric(movies['popularity'], errors='coerce').fillna(0)
    movies['release_date'] = movies['release_date'].fillna("Unknown")


    def get_imdb_url(imdb_id):
        if pd.notna(imdb_id) and imdb_id != 'nan':
            return f"https://www.imdb.com/title/{imdb_id}/"
        return "#"

    movies['imdb_url'] = movies['imdb_id'].apply(get_imdb_url)

    try:
        keywords = pd.read_csv("keywords.csv")
        keywords['keywords'] = keywords['keywords'].fillna('[]').apply(ast.literal_eval)

        keyword_dict = {}
        for _, row in keywords.iterrows():
            movie_id = row['id']
            keyword_list = [kw['name'] for kw in row['keywords'] if 'name' in kw]
            keyword_dict[str(movie_id)] = keyword_list

        movies['tags'] = movies['id'].astype(str).map(keyword_dict).fillna('').apply(lambda x: x if isinstance(x, list) else [])
    except:
        movies['tags'] = [[] for _ in range(len(movies))]

    return movies

movies = load_movies()






