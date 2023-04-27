import openai
from Scripts import globals

model_engine = "text-davinci-003"


def main():
    openai.api_key = globals.openai_APIKey

    flag = False
    while not flag:
        playlistName = input("What would you like to name your playlist?: \n")
        confirm = input(f"Your playlist name is '{playlistName}'. Type 'Y' to confirm: \n")
        if confirm == "Y" or confirm == 'y':
            globals.playlistName = playlistName
            flag = True

    exit_words = ("q", "Q", "quit", "QUIT", "EXIT")
    try:
        while True:
            print("Type q, Q, quit, QUIT or EXIT to cancel.")
            query = input("What playlist should I make?: \n")
            globals.description = query
            query = 'You will act as a music recommender. You will be prompted for a type of playlist, and you will ' \
                    'fulfill that request by responding with a list of 20 songs and their artists. You are to ' \
                    'creatively compile music in a way that matches the description, providing both accuracy and ' \
                    'variety in the music you curate. In your response, ' \
                    'strictly adhere to the following format without any context: ' \
                    '"Maple Syrup" - The Backseat Lovers, "Sugar" - Maroon 5, "Time" - Pink Floyd.' \
                    'You will now make the playlist using the following description: ' + query

            if globals.description in exit_words:
                print("ENDING CHAT")
                break
            else:
                songs = []
                resp = GPT(query)
                # print(resp)
                for song in resp:
                    songs.append(song)
                globals.songList = songs
                break
    except KeyboardInterrupt:
        print("\nExiting ChatGPT")


def GPT(query):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=query,
        max_tokens=500,
        n=1,
        temperature=0.5,
    )

    return response.choices[0].text.split(',')


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    main()
