import spotipy
from Scripts import globals
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"
REDIRECT_URI = "REDIRECT_URL"
SCOPE = "YOUR_SCOPE"
# EXAMPLE_SCOPE = SCOPE = "user-library-read user-library-modify playlist-read-private playlist-modify-private playlist-modify-public"


def main():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope = SCOPE))


    user = sp.current_user()
    user_id = user['id']

    playlist_name = globals.playlistName
    description = globals.description

    my_playlist = sp.user_playlist_create(user = user_id, name = playlist_name, public = False, description = description)
    # sp.user_playlist_add_tracks(user = user_id, playlist_id = my_playlist['id'], tracks = song_id_list)

    for song in globals.getList():
        results = sp.search(q = song, limit = 1, type = 'track')

        items = results['tracks']['items']
        if items:
            track = items[0]
            track_uri = track['uri']
            sp.playlist_add_items(my_playlist['id'], [track_uri])
        else:
            print(f"{song} not found on Spotify")




if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()


