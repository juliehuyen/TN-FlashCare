import os
from dataclasses import dataclass
from dotenv import load_dotenv
import cohere

from domain.port.chat_application_port import ChatApplicationPort

from infrastructure.text_generator.cohere_text_generator import CohereTextGenerator
from infrastructure.repository.history_repository import HistoryRepository

load_dotenv()
COHERE_API_KEY = os.environ.get('COHERE_API_KEY')

@dataclass
class ChatApplicationAdapter(ChatApplicationPort):
    cohere_text_generator: CohereTextGenerator = CohereTextGenerator()
    history_repository: HistoryRepository = HistoryRepository()

    def get_generated_text(self, prompt: str) -> str:
        return self.cohere_text_generator.generate_text(prompt=prompt)
    
    def get_history(self, i: int) -> str:
        return self.history_repository.get(i)
    
    def save_history(self, history: str):
        return self.history_repository.save(history)