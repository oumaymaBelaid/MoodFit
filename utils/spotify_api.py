emotion_to_playlist = {
    "joy": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
    "sadness": "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1",
    "anger": "https://open.spotify.com/playlist/37i9dQZF1DWYkaDif7ZtbP",
    "love": "https://open.spotify.com/playlist/37i9dQZF1DX0BcQWzuB7ZO",
    "fear": "https://open.spotify.com/playlist/37i9dQZF1DWWEJlAGA9gs0",
    "surprise": "https://open.spotify.com/playlist/37i9dQZF1DWWEJlAGA9gs0"
}

def get_playlist_for_emotion(emotion):
    return emotion_to_playlist.get(emotion.lower(), emotion_to_playlist["joy"])
