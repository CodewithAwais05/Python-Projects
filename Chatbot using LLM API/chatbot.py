from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

apiKey = os.getenv("GROQ_API_KEY")

client = Groq(api_key = apiKey)

conversation = [
{    "role" : "system" , "content" : "You are a helpful assistant."    }
]
print("Chatbot ready! Enter 'Quit' to exit.\n")

while True:
    user_input = input("You:   ")

    if user_input.lower() == "quit":
        print("\n===============GOOD-BYE===============\n")
        break
    
    conversation.append({"role" : "user" , "content" : user_input})
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = conversation
    )
    reply = response.choices[0].message.content
    print(f"Bot:  {reply}\n")

    conversation.append({"role" : "assistant" , "content" : reply})



