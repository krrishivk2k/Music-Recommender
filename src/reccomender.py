from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import numpy as np

def recommend_songs(df, song_name, num_recommendations=5):
    feature_cols = ['danceability', 'energy', 'valence', 'tempo']
    
    # Normalize the features
    scaler = StandardScaler()
    normalized_features = scaler.fit_transform(df[feature_cols])

    # Compute similarity matrix
    similarity_matrix = cosine_similarity(normalized_features)

    # Get index of the input song
    song_index = df[df['name'] == song_name].index[0]
    
    # Get similarity scores for all songs
    similarity_scores = list(enumerate(similarity_matrix[song_index]))
    
    # Sort by highest similarity (excluding the song itself)
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]

    # Retrieve song recommendations
    recommended_songs = df.iloc[[idx for idx, _ in similarity_scores]]
    
    return recommended_songs[['name', 'artist', 'genre']]

# Example usage
recommendations = recommend_songs(df, "Song Name", num_recommendations=5)
print(recommendations)
