from domain.model.role_message import RoleMessage
class History:
    def __init__(self, list_message: list[RoleMessage]):
        self.list_messages = list_message