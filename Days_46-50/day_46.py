# Day 46 of 100 Days of Code Challenge
# Step Back in Time Spotify Playlist
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

REDIRECT_URI = "http://example.com"

input_date = input("Enter a date from the last 20 years in the format (YYYY-MM-DD)\n")
year = input_date[:4]
billboard_url = f'http://billboard.com/charts/hot-100/{input_date}/'

r = requests.get(url=billboard_url)
website_data = r.text

soup = BeautifulSoup(website_data, "html.parser")
titles = [song.text.strip('\t\n') for song in soup.select("li ul li h3")]

# connect to spotify API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get("CLIENT_ID"),
                                               client_secret=os.environ.get("CLIENT_SECRET"),
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"))

user_id = sp.current_user()["id"]

song_uris = []
for title in titles:
    try:
        song_uris.append(sp.search(q=f"track: {title} year: {year}", limit=1)["tracks"]["items"][0]["uri"])
    except IndexError:
        pass

playlist_id = sp.user_playlist_create(user=user_id,
                                      name=f"{input_date} Billboard 100",
                                      public=False,
                                      description="A python created playlist!")

sp.playlist_add_items(playlist_id=playlist_id['id'], items=song_uris)
