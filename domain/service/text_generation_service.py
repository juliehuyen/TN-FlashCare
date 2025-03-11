from domain.port.chat_application_port import ChatApplicationPort

class TextGenerationService:
    def __init__(self, text_generator: ChatApplicationPort):
        self.text_generator = text_generator

    def get_generated_text(self, prompt: str) -> str:
        return self.text_generator.get_generated_text(prompt)