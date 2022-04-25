# Dotenv config
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv

artists_list = [
    'spotify:artist:2WX2uTcsvV5OnS0inACecP',
]

csv_info = ['Artist,Album,SpotifyUrl,TrackName,TrackDuration(sec),TrackPopularity']

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

for artist in artists_list:
    results = spotify.artist_top_tracks(artist)

    tracks = results['tracks']
    for track in tracks:
        artist_name = ' | '.join(map(lambda a : a['name'], track['artists']))
        album_name = track['album']['name']
        spotify_url = track['external_urls']['spotify']
        track_name = track['name']
        track_duration_s = track['duration_ms'] / 1000
        track_popularity = track['popularity']

        csv_info.append(f'{artist_name},{album_name},{spotify_url},{track_name},{track_duration_s},{track_popularity}')

with open('results.csv','w') as f:
    f.write('\n'.join(csv_info))
