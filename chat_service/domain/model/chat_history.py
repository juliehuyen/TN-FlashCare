from dataclasses import dataclass
from chat_service.domain.model.role_message import RoleMessage

@dataclass
class ChatHistory:
    messages: list[RoleMessage]
