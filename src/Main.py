# Dotenv config
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

print('Running from main!')


birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])

