from env_config import EnvConfig

from domain.port.impl.generator_controller_adapter import GeneratorControllerAdapter
from domain.service.text_generation_service import TextGenerationService
from domain.service.system_prompt_service import SystemPromptService
from domain.service.chat_history_service import ChatHistoryService

from infrastructure.adapter.infrastructure_adapter import InfrastructureAdapter
from infrastructure.history.json_history_repository import JsonHistoryRepository
from infrastructure.text_generator.cohere_text_generator import CohereTextGenerator

from rest.endpoint.generator_rest_adapter import GeneratorRestAdapter

def create_generator_rest_adapter():
    # Initialiser les services de persistance
    cohere_text_generator = CohereTextGenerator()
    
    json_history_repository = JsonHistoryRepository(EnvConfig.get_json_history_repository())
    
    # Injecter CohereTextGenerator dans TextGeneratorAdapter
    infrastructure_adapter = InfrastructureAdapter(cohere_text_generator, json_history_repository)
    
    # Initialiser les services
    # system_prompt_service = SystemPromptService()
    text_generation_service = TextGenerationService(infrastructure_adapter)
    chat_history_service = ChatHistoryService(infrastructure_adapter)

    # Configurer les services et adaptateurs
    generator_controller_adapter = GeneratorControllerAdapter(text_generation_service, chat_history_service)
    return GeneratorRestAdapter(generator_controller_adapter)



