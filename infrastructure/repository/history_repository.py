from domain.model.history import History
class HistoryRepository:
    def __init__(self):
        self.data = []  # Liste des historiques

    def save(self, history: History):
        self.data.append(history)  # Ajoute l'history

    def get(self, user_id: int) -> History:
        return self.data.get(user_id, History())  # Retourne un historique vide si inexistant