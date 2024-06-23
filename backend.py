import os
from dotenv import load_dotenv 
from groq import Groq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
class Chatbot:
    def __init__(self):
        self.api_key = GROQ_API_KEY

    def get_response(self, user_input):
        client = Groq(api_key=self.api_key)
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model="mixtral-8x7b-32768",
        )
        response = chat_completion.choices[0].message.content
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Show me your move")
    print(response)