from abc import ABC, abstractmethod
from dotenv import load_dotenv

from game.llms.fireworks import FireworksClient
from game.llms.bedrock import BedrockClient
from game.llms.openai import OpenAIClient


load_dotenv()

MODELS = {
    "OpenAI": [
        ('o1-2024-12-17', 'o1'),
        ('gpt-4o-2024-08-06', '4o-aug'),
        ('gpt-4o-2024-11-20', '4o-nov'),
        ('o3-mini-2025-01-31', 'o3'),
    ],
    "Bedrock": [('eu.anthropic.claude-3-5-sonnet-20240620-v1:0', 'sonnet')],
    "Fireworks": [
        ('accounts/fireworks/models/llama-v3p1-405b-instruct', 'llama'),
        ('accounts/fireworks/models/deepseek-r1', 'r1'),
    ],
}

class BaseLLMClient(ABC):
    @abstractmethod
    def chat(self, message: str) -> str:
        """Send a chat message and return a response."""

    @abstractmethod
    def vote(self, message: str) -> int:
        """Vote on a given message."""

def get_llm_client_instance(model_name: str) -> BaseLLMClient:
    for provider, models in MODELS.items():
        model_names = [m[0] for m in models]
        if model_name in model_names:
            if provider == "OpenAI":
                return OpenAIClient(model_name)
            if provider == "Fireworks":
                return FireworksClient(model_name)
            if provider == "Bedrock":
                return BedrockClient(model_name)
    raise ValueError(f"Model '{model_name}' is not implemented.")

class LLMClient:
    def __init__(self, model_name: str):
        self._client = get_llm_client_instance(model_name)

    def chat(self, message: str) -> str:
        return self._client.chat(message)

    def vote(self, message: str) -> int:
        return self._client.vote(message)
