import os
from dotenv import load_dotenv

from chat_service.domain.model.chat_history import ChatHistory
from chat_service.domain.model.role_message import RoleMessage
from chat_service.domain.port.driven.text_generator_port import TextGeneratorPort
from chat_service.domain.port.driven.chat_history_persistence_port import ChatHistoryPersistencePort

from chat_service.infrastructure.history.json_history_repository import JsonHistoryRepository
from chat_service.infrastructure.text_generator.cohere_text_generator import CohereTextGenerator

# Charger les variables d'environnement depuis un fichier .env
load_dotenv()
COHERE_API_KEY = os.environ.get('COHERE_API_KEY')  # Récupère la clé API Cohere

class InfrastructureAdapter(TextGeneratorPort, ChatHistoryPersistencePort):
    def __init__(self, 
                 cohere_text_generator: CohereTextGenerator,
                 json_history_repository: JsonHistoryRepository):
        self.cohere_text_generator = cohere_text_generator
        self.json_history_repository = json_history_repository

    def get_generated_text(self, chat_history: ChatHistory) -> str:
        return self.cohere_text_generator.generate_text(chat_history)

    def get_all_conversations(self) -> list[str]:
        return self.json_history_repository.get_all_conversations()
    
    def get_history(self, conversation_guid: str) -> ChatHistory:
        return self.json_history_repository.get_history_from_file(conversation_guid)
    
    def create_conversation(self):
        return self.json_history_repository.create_conversation()
    
    def add_message_to_history(self, conversation_guid: str, role_message: RoleMessage) -> ChatHistory:
        return self.json_history_repository.add_entry_to_conversation(conversation_guid, role_message)
    
    def clear_history(self, conversation_guid: str) -> ChatHistory:
        return self.json_history_repository.clear_conversation(conversation_guid)