import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class PlaylistGenerator:
    def __init__(self):

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv("CLIENT_ID"),
            client_secret=os.getenv("CLIENT_SECRET"),
            redirect_uri=os.getenv("REDIRECT_URI"),
            scope="user-read-private"
        ))

    def search_tracks(self, query, limit=10):

        try:
            results = self.sp.search(q=query, type="track", limit=limit)
            tracks = []
            for item in results["tracks"]["items"]:
                track_info = {
                    "name": item["name"],
                    "artist": item["artists"][0]["name"],
                    "url": item["external_urls"]["spotify"]
                }
                tracks.append(track_info)
            return tracks
        except Exception as e:
            print("⚠ Spotify search error:", str(e))
            return []
