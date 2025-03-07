import os
from game.llms.base import BaseLLMClient
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class OpenAIClient():
    def __init__(self, model):
        super().__init__()
        self.client = self.instantiate_client()
        self.model = model
    
    def instantiate_client(self):
        return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def chat(self, messages):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        message_text = response.choices[0].message.content
        return message_text
    
    def vote(self, messages):
        return self.chat(messages)