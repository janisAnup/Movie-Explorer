import pandas as pd
import ast
import streamlit as st


def extract_genres(genre_str):
    try:
        genres = ast.literal_eval(genre_str)
        return [g['name'] for g in genres if isinstance(g, dict)]
    except:
        return []

def extract_cast(cast_str):
    try:
        cast = ast.literal_eval(cast_str)
        return [actor['name'] for actor in cast[:3]]
    except:
        return []

def extract_director(crew_str):
    try:
        crew = ast.literal_eval(crew_str)
        for member in crew:
            if member.get('job') == 'Director':
                return member['name']
        return None
    except:
        return None

def extract_keywords(kw_str):
    try:
        keywords = ast.literal_eval(kw_str)
        return [k['name'] for k in keywords][:5]
    except:
        return []


@st.cache_data
def load_movies():
    # Load CSVs
    movies = pd.read_csv("movies_metadata.csv", low_memory=False)
    credits = pd.read_csv("credits.csv")
    keywords = pd.read_csv("keywords.csv")
    links = pd.read_csv("links.csv")

    # Filter useful columns and convert types
    movies = movies[['id', 'title', 'overview', 'genres', 'release_date', 'vote_average', 'popularity']]
    movies = movies.dropna(subset=['title', 'overview', 'genres'])
    movies['id'] = pd.to_numeric(movies['id'], errors='coerce')

    credits['id'] = pd.to_numeric(credits['id'], errors='coerce')
    keywords['id'] = pd.to_numeric(keywords['id'], errors='coerce')
    links['tmdbId'] = pd.to_numeric(links['tmdbId'], errors='coerce')
    links = links.rename(columns={'tmdbId': 'id'})

    # Merge all
    movies = movies.merge(credits[['id', 'cast', 'crew']], on='id', how='left')
    movies = movies.merge(keywords[['id', 'keywords']], on='id', how='left')
    movies = movies.merge(links[['id', 'imdbId']], on='id', how='left')

    # Feature engineering
    movies['genres'] = movies['genres'].apply(extract_genres)
    movies['top_actors'] = movies['cast'].apply(extract_cast)
    movies['director'] = movies['crew'].apply(extract_director)
    movies['tags'] = movies['keywords'].apply(extract_keywords)
    movies['imdb_url'] = "https://www.imdb.com/title/tt" + movies['imdbId'].astype(str).str.zfill(7)

    return movies

movies = load_movies()


