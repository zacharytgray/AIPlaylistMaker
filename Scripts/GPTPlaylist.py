import openai
import globals
import keyboard
model_engine = "text-davinci-003"
openai.api_key = "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"


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
            globals.description = query
            if query in exit_words:
               print("ENDING CHAT")
               break
            else:
               songs = []
               resp = GPT(query)
               for i in resp:
                     if (i != "\n" and i != ""):
                        songs.append(i)
               # print("="*20)
               # print("="*20)
               globals.songList = songs
               break
   except KeyboardInterrupt:
      print("\nExiting ChatGPT")



def GPT(query):
   response = openai.Completion.create(
       engine=model_engine,
       prompt=query,
       max_tokens=100,
       n=1,
       temperature=0.5,
   )
#   return str.strip(response['choices'][0]['text']), response['usage']['total_tokens']
   return response.choices[0].text.split('\n')

# def main():
#    globals.songList = ["Blue Cigar - Midnight Sister", "Japanese Candy - Brutis VIII", "Lower the Heavens - The Donkeys", "Maply Syrup", "thisisnotarealsong"]

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()