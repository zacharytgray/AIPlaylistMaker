import openai
model_engine = "text-davinci-003"
openai.api_key = "YOUR_API_KEY"

def main():
    exit_words = ("q","Q","quit","QUIT","EXIT")
    ("Type q, Q, quit, QUIT or EXIT to cancel.")
    try:
        while True:
            query = input("Talk to ChatGPT: ")
            if query in exit_words:
                print("ENDING CHAT")
                break
            else:
                response = GPT(query)
                print(response)
    except KeyboardInterrupt:
        print("\nExiting ChatGPT")



def GPT(query):
   response = openai.Completion.create(
       engine=model_engine,
       prompt=query,
       max_tokens=100,
       n=1,
       temperature=0,
   )
#   return str.strip(response['choices'][0]['text']), response['usage']['total_tokens']
   return response.choices[0]


if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()