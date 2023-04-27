import openai
import requests
from Scripts import globals

model_engine = "dall-e-2"


def main():
    openai.api_key = globals.openai_API_Key

    exit_words = ("q", "Q", "quit", "QUIT", "EXIT")
    try:
        while True:
            print("What do you want as the album art for this playlist?")
            query = input("(Hint: The more specific you are, the better the results.) \n")
            globals.albumArt = query
            query = f"Create playlist cover art for a playlist that is named '{globals.playlistName}' " \
                    f"and has the following description. Use appropriate colors. Do not use any words in the image.: " \
                    + globals.albumArt

            if globals.description in exit_words:
                print("ENDING CHAT")
                break
            else:
                generateImage(query)
                break

    except KeyboardInterrupt:
        print("\nExiting ChatGPT")


def generateImage(query):
    response = openai.Image.create(
        prompt=query,
        n=1,
        size="512x512"
    )

    image_url = response['data'][0]['url']
    image_response = requests.get(image_url)

    with open('generated_image.png', 'wb') as f:
        f.write(image_response.content)


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    main()
