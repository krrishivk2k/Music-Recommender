import streamlit as st
from api import get_playlist_tracks
from src.recommend import recommend_songs

st.title("Spotify Song Recommender")

playlist_url = st.text_input("Paste a Spotify Playlist URL:")
if playlist_url:
    df = get_playlist_tracks(playlist_url)
    song_choice = st.selectbox("Choose a song:", df["name"])
    
    if st.button("Get Recommendations"):
        recommendations = recommend_songs(df, song_choice)
        st.write(recommendations)

