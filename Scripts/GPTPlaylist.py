import openai
import globals
model_engine = "text-davinci-003"
openai.api_key = "YOUR_API_KEY"


def main():
    
   flag = False
   while not flag:
      playlistName = input("What would you like to name your playlist?: ")
      confirm = input(f"Your playlist name is '{playlistName}'. Type 'Y' to confirm.")
      if confirm == "Y" or confirm == 'y':
         globals.playlistName = playlistName
         flag = True
         break


   exit_words = ("q","Q","quit","QUIT","EXIT")
   try:
        while True:
            print("Type q, Q, quit, QUIT or EXIT to cancel.")
            query = input("What playlist should I make?: ")
            query = 'Follow these instructions precisely. Enter your response in a list format without any context. Your inputs will be music requests, and you will respond with a list of songs formatted as the following example: "Maple Syrup" - The Backseat Lovers, "Sugar" - Maroon 5, "Time" - Pink Floyd. You  will now create a playlist based off of the following conditions: ' + query
            globals.description = query
            if query in exit_words:
               print("ENDING CHAT")
               break
            else:
               songs = []
               resp = GPT(query)
               print(resp)
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
       max_tokens=200,
       n=1,
       temperature=0.5,
   )
#   return str.strip(response['choices'][0]['text']), response['usage']['total_tokens']
   # return response.choices[0].text.split('\n')
   return response.choices[0].text.split(',')

# def main():
#    globals.songList = ["Blue Cigar - Midnight Sister", "Japanese Candy - Brutis VIII", "Lower the Heavens - The Donkeys", "Maply Syrup", "thisisnotarealsong"]

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()