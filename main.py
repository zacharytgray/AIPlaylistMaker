from Scripts import globals, GPTPlaylist, spotifyAPI

if __name__ == "__main__": 
    globals.initialize() 
    GPTPlaylist.main()
    spotifyAPI.main()
    print(globals.songList)
    


