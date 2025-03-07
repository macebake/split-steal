from abc import ABC, abstractmethod

class BaseLLMClient(ABC):
    @abstractmethod
    def chat(self, message: str) -> str:
        """Send a chat message and return a response."""
        pass

    @abstractmethod
    def vote(self, message: str) -> int:
        """Vote on a given message."""
        pass