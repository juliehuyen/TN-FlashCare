# from domain.port.history_repository_port import HistoryRepositoryPort
from domain.model.history import History
from infrastructure.repository.history_repository import HistoryRepository
from domain.port.chat_application_port import ChatApplicationPort

class HistoryService:
    def __init__(self, history_repository: ChatApplicationPort):
        self.history_repository = history_repository

    def get_history(self, i: int) -> History:
        return self.history_repository.get_history(i)
    
    def save_history(self, history: str):
        return self.history_repository.save_history(history)
