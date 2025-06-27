import pandas as pd
import ast
import streamlit as st

@st.cache_data
def load_movies():

    movies = pd.read_csv("movies_metadata.csv", low_memory=False)
    keywords = pd.read_csv("keywords.csv")
    links = pd.read_csv("links.csv")

    movies = movies[movies["status"] == "Released"]
    movies = movies[movies["overview"].notnull()]

    movies['id'] = pd.to_numeric(movies['id'], errors='coerce')
    links['tmdbId'] = pd.to_numeric(links['tmdbId'], errors='coerce')


    movies = movies.merge(keywords, on='id', how='left')
    movies = movies.merge(links[['tmdbId', 'imdbId']], left_on='id', right_on='tmdbId', how='left')

    movies['imdb_url'] = movies['imdbId'].apply(
        lambda x: f"https://www.imdb.com/title/tt{int(x):07d}" if pd.notnull(x) else None
    )

    def extract_list(col):
        try:
            return [item['name'] for item in ast.literal_eval(col) if isinstance(item, dict)]
        except:
            return []

    def extract_keywords(col):
        try:
            return [item['name'] for item in ast.literal_eval(col)][:5]
        except:
            return []

    movies['genres'] = movies['genres'].apply(extract_list)
    movies['tags'] = movies['keywords'].apply(extract_keywords)
    movies['title_lower'] = movies['title'].str.lower().fillna("")

    return movies

movies = load_movies()



