import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Set up Spotify API authentication
SPOTIPY_CLIENT_ID = "a87774e79a8241708ca7aeb9a66d6130"
SPOTIPY_CLIENT_SECRET = "be9fdcb8977941b080488f7d824b3bbf"

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_playlist_tracks(playlist_url):
    playlist_id = playlist_url.split("/")[-1].split("?")[0]  # Extract ID from URL
    results = sp.playlist_tracks(playlist_id)
    
    tracks = []
    for item in results['items']:
        track = item['track']
        features = sp.audio_features(track['id'])[0]  # Get audio features
        
        track_data = {
            'id': track['id'],
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'genre': sp.artist(track['artists'][0]['id'])['genres'] if track['artists'] else [],
            'danceability': features['danceability'],
            'energy': features['energy'],
            'valence': features['valence'],
            'tempo': features['tempo']
        }
        tracks.append(track_data)
    
    return pd.DataFrame(tracks)

# Example usage
playlist_url = "https://open.spotify.com/playlist/your_playlist_id"
df = get_playlist_tracks(playlist_url)
print(df.head())
