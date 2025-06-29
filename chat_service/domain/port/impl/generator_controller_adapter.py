from chat_service.domain.model.chat_history import ChatHistory
from chat_service.domain.model.role_message import RoleMessage
from chat_service.domain.port.driving.generator_controller_port import GeneratorControllerPort

from chat_service.domain.service.chat_history_service import ChatHistoryService
from chat_service.domain.service.text_generation_service import TextGenerationService

class GeneratorControllerAdapter(GeneratorControllerPort):
    def __init__(
        self,
        text_generation_service: TextGenerationService = None,
        chat_history_service: ChatHistoryService = None,
        system_prompt_service: str = None):
        self.text_generation_service = text_generation_service
        self.chat_history_service = chat_history_service
        self.sytem_prompt_service = system_prompt_service

    def generate_message(self, prompt: str) -> str:
        role_msg = RoleMessage(role="user", message=prompt)
        chat_history = ChatHistory(messages=[role_msg])
        return self.text_generation_service.get_generated_text(chat_history)

    def get_conversations(self) -> list[str]:
        return self.chat_history_service.get_all_conversations()

    def create_conversation(self) -> str:
        return self.chat_history_service.create_conversation()

    def get_history(self, conversation_guid: str) -> ChatHistory:
        return self.chat_history_service.get_history(conversation_guid)

    def generate_message_in_conversation(self, conversation_guid: str, prompt: str) -> ChatHistory:
        history_with_prompt = self.add_user_prompt_to_history(conversation_guid, prompt)
        generated_text = self.text_generation_service.get_generated_text(history_with_prompt)
        return self.add_generated_message_to_history(conversation_guid, generated_text)

    def add_user_prompt_to_history(self, conversation_guid: str, prompt: str) -> ChatHistory:
        return self.add_message_to_history(conversation_guid, "user", prompt)

    def add_generated_message_to_history(self, conversation_guid: str, generated_text: str) -> ChatHistory:
        return self.add_message_to_history(conversation_guid, "assistant", generated_text)

    def add_message_to_history(self, conversation_guid: str, role: str, message: str) -> ChatHistory:
        message_to_save = RoleMessage(role, message)
        return self.chat_history_service.add_message(conversation_guid, message_to_save)

    def clear_history(self, conversation_guid: str) -> ChatHistory:
        return self.chat_history_service.clear_history(conversation_guid)