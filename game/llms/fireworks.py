import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()


class FireworksClient():
    def __init__(self, model):
        super().__init__()
        self.model = model

    def chat(self, messages, temperature=0.7):
        url = "https://api.fireworks.ai/inference/v1/chat/completions"
        payload = {
            "model": self.model,
            "top_p": 1,
            "top_k": 40,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "temperature": temperature,
            "messages": messages,
        }

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('FIREWORKS_API_KEY')}"
        }
        response = requests.request(
            "POST",
            url,
            headers=headers,
            data=json.dumps(payload),
            timeout=30,
        )
        text = json.loads(response.text)
        message = text['choices'][0]['message']['content']

        if "deepseek-r1" in self.model:
            return self.remove_thinking(message)

        return message

    def vote(self, messages):
        return self.chat(messages)

    def remove_thinking(self, message):
        split_thinking = message.split("</think>")[1]
        stripped_newlines = split_thinking.replace("\n", "")
        return stripped_newlines
