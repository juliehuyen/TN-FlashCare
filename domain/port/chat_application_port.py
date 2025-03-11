from abc import ABC, abstractmethod
from domain.model.history import History

class ChatApplicationPort(ABC):
    @abstractmethod
    def get_generated_text(self, prompt: str) -> str:
        pass

    @abstractmethod
    def get_history(self, i: int) -> list:
        pass

    @abstractmethod
    def save_history(self, history: History):
        pass