from Scripts import globals, GPTPlaylist, spotifyAPI


def main():
    globals.initialize()
    GPTPlaylist.main()
    spotifyAPI.main()


if __name__ == "__main__":
    main()
