# domain/service/text_generation_service.py

from domain.model.chat_history import ChatHistory
from domain.model.role_message import RoleMessage
from domain.port.driven.text_generator_port import TextGeneratorPort
from domain.service.system_prompt_service import SystemPromptService

class TextGenerationService:
    def __init__(self, text_generator: TextGeneratorPort, system_prompt_service: SystemPromptService):
        # Remove trailing comma to avoid tuple assignment
        
        self.text_generator = text_generator
        self.system_prompt_service = SystemPromptService()

    def get_generated_text(self, chat_history: ChatHistory) -> str:
        # 1) Retrieve the system prompt text
        system_content = self.system_prompt_service.get_system_prompt()
        # 2) Create a ChatMessage for the system prompt
        system_message = RoleMessage(role="system", message=system_content)

        # 3) Prepend the system message to existing history
        updated_messages = [system_message] + chat_history.messages
        updated_history = ChatHistory(messages=updated_messages)

        # 4) Delegate to the underlying text generator
        return self.text_generator.get_generated_text(updated_history)
