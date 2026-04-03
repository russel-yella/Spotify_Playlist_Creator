from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID="YOUR SPOTITY ID"
SPOTIPY_CLIENT_SECRET="YOUR SPOTIPY SECRET"
SPOTIPY_REDIRECT_URI="http://127.0.0.1:8888/callback"

scope = "playlist-modify-private playlist-modify-public"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=scope,
        show_dialog=True,
        cache_path=".cache"
    )
)

user_id = sp.current_user()["id"]

date = input("Enter date YYYY-MM-DD: ")

# scrape Billboard
url = f"https://www.billboard.com/charts/hot-100/{date}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

song_names = [
    song.getText().strip()
    for song in soup.select("li ul li h3")
]

artist_names = [
    artist.getText().strip()
    for artist in soup.select("li ul li h3 + span")
]
year = date.split("-")[0]

song_uris = []

for song, artist in zip(song_names, artist_names):

    result = sp.search(
        q=f"{song} {artist}",
        type="track",
        limit=1
    )

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(f"Added: {song} - {artist}")

    except IndexError:
        print(f"Not found: {song} - {artist}")


playlist = sp.user_playlist_create(
    user=None,
    name=f"{date} Billboard 100",
    public=False
)

sp.playlist_add_items(
    playlist_id=playlist["id"],
    items=song_uris
)

print("Playlist created successfully!")
print(playlist["external_urls"]["spotify"])