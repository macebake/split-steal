import os
import boto3
from dotenv import load_dotenv

load_dotenv()

class BedrockClient():
    def __init__(self, model):
        super().__init__()
        self.client = self.instantiate_client()
        self.model = model

    def instantiate_client(self):
        session = boto3.Session(profile_name=os.getenv("AWS_PROFILE"))
        return session.client(service_name="bedrock-runtime")

    def chat(self, messages):

        fixed_messages = self.fix_messages(messages)

        response = self.client.converse(
            modelId=self.model,
            messages=fixed_messages,
        )

        return response["output"]["message"]["content"][0]["text"]

    def vote(self, messages):
        return self.chat(messages)

    def fix_messages(self, messages):
        """
        Ensures that messages are in the correct format for the Bedrock API.
        Kinda horrific, but Anthropic is the only standout here.
        """
        if isinstance(messages, dict):
            messages = [messages]

        for message in messages:
            if not isinstance(message["content"], list):
                message["content"] = [{"text": message["content"]}]

        return messages
