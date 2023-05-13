import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up the Spotify API client
scope = "user-read-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='21a006ab95cd4665b15a232271b04aba', client_secret="c1b12da2e6a44662bd38904efedf9ff2", redirect_uri="http://localhost:8080/callback", scope=scope))

# Get the user's currently playing track
current_track = sp.current_playback()

# Check if a track is currently playing
if current_track is None:
    print("No track is currently playing.")
else:
    # Get the name of the song and the artist
    track_name = current_track['item']['name']
    artist_name = current_track['item']['artists'][0]['name']

    # Print the name of the song and artist to the terminal
    print("Currently playing:", track_name, "by", artist_name)
