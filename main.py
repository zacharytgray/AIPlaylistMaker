import globals
import spotifyAPI
import GPTPlaylist

if __name__ == "__main__": 
    globals.initialize() 
    GPTPlaylist.main()
    spotifyAPI.main()
    print(globals.songList)
    


