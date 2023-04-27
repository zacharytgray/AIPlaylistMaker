import base64
import spotipy
from Scripts import globals, GPTImage
from PIL import Image
from spotipy.oauth2 import SpotifyOAuth


def main():
    CLIENT_ID = globals.CLIENT_ID
    CLIENT_SECRET = globals.CLIENT_SECRET
    REDIRECT_URI = globals.REDIRECT_URI
    SCOPE = globals.SCOPE
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope=SCOPE))
    user = sp.current_user()
    user_id = user['id']

    playlist_name = globals.playlistName
    description = "This playlist was created by AI using the following prompt: " + globals.description

    my_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=description)

    for song in globals.songList:
        results = sp.search(q=song, limit=1, type='track')

        items = results['tracks']['items']
        if items:
            track = items[0]
            track_uri = track['uri']
            sp.playlist_add_items(my_playlist['id'], [track_uri])
        else:
            print(f"{song} not found on Spotify")

    GPTImage.main()

    image = Image.open("/Users/zacharytgray/Documents/GitHub/PlaylistMaker/generated_image.png")
    new_image = image.resize((215, 215))
    new_image.save("generated_image.png")

    with open("/Users/zacharytgray/Documents/GitHub/PlaylistMaker/generated_image.png", "rb") as image_file:
        image_64_encode = base64.b64encode(image_file.read())
    if len(image_64_encode) > 256000:
        print("image is too big: ", len(image_64_encode))
    else:
        sp.playlist_upload_cover_image(playlist_id=my_playlist['id'], image_b64=image_64_encode)


if __name__ == "__main__":
    main()
