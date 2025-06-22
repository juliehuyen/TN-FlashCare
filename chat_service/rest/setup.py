from env_config import EnvConfig

from chat_service.domain.port.impl.generator_controller_adapter import GeneratorControllerAdapter
from chat_service.domain.service.text_generation_service import TextGenerationService
from chat_service.domain.service.chat_history_service import ChatHistoryService
from chat_service.domain.service.system_prompt_service import SystemPromptService

from chat_service.infrastructure.adapter.infrastructure_adapter import InfrastructureAdapter
from chat_service.infrastructure.history.json_history_repository import JsonHistoryRepository
from chat_service.infrastructure.text_generator.cohere_text_generator import CohereTextGenerator

from chat_service.rest.endpoint.generator_rest_adapter import GeneratorRestAdapter

def create_generator_rest_adapter():
    # Initialiser les services de persistance
    cohere_text_generator = CohereTextGenerator()
    
    json_history_repository = JsonHistoryRepository(EnvConfig.get_json_history_repository())
    
    # Injecter CohereTextGenerator dans TextGeneratorAdapter
    infrastructure_adapter = InfrastructureAdapter(cohere_text_generator, json_history_repository)
    
    # Initialiser les services
    system_prompt_service = SystemPromptService()
    text_generation_service = TextGenerationService(infrastructure_adapter, system_prompt_service)
    chat_history_service = ChatHistoryService(infrastructure_adapter)

    # Configurer les services et adaptateurs
    generator_controller_adapter = GeneratorControllerAdapter(
        text_generation_service, chat_history_service, system_prompt_service
    )
    return GeneratorRestAdapter(generator_controller_adapter)



