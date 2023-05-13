import os
import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

# Set up the Spotify API client
scope = "user-read-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri="http://localhost:8080/callback", scope=scope))

# Check if a track is currently playing
current_track = None
while True:
    # Get the currently playing track
    track = sp.current_playback()
    if track and track["item"]:
        # Get the name of the song and artist
        song_name = track["item"]["name"]
        artist_name = track["item"]["artists"][0]["name"]
        # Print the name of the song and artist if it has changed
        if (song_name, artist_name) != current_track:
            print("\nSong: {} - Artist: {}".format(song_name, artist_name))
            current_track = (song_name, artist_name)
    # Wait for a few seconds before checking again
    time.sleep(5)
