import requests
from dotenv import load_dotenv
import os

load_dotenv()

SPOTIFY_API_BASE_URL = 'https://api.spotify.com/v1'

def get_token():
    auth_url = 'https://accounts.spotify.com/api/token'
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })

    return response.json()['access_token']

def get_current_track(token):
    url = SPOTIFY_API_BASE_URL + '/me/player/currently-playing'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response_json = response.json()
        if response_json['is_playing']:
            track_name = response_json['item']['name']
            artist_names = ", ".join([artist['name'] for artist in response_json['item']['artists']])
            return f"{track_name} by {artist_names}"
        else:
            return 'No track is currently playing.'
    else:
        return f'Error: {response.status_code} {response.reason}'

token = get_token()
current_track = get_current_track(token)
print(current_track)
