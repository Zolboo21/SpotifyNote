from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
print(f"CLIENT_ID: {client_id}")
print(f"CLIENT_SECRET: {client_secret}")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    print(json_result)
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def get_current_track(token):
    print("Getting current track...")
    url = "https://api.spotify.com/v1/me/player/currently-playing"
    header = get_auth_header(token)
    result = get(url, headers=header)
    json_result = json.loads(result.content)

    if "item" in json_result:
        track_name = json_result["item"]["name"]
        artist_name = json_result["item"]["artists"][0]["name"]
        print(f"Currently playing: {track_name} by {artist_name}")
    else:
        print("No track currently playing.")

token = get_token()
get_current_track(token)

