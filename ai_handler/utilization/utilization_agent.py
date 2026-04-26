from config.settings import logger, Settings
from langchain_gigachat.chat_models import GigaChat
from langchain_core.messages import SystemMessage
import os
from ai_handler.utilization.utilization_agent_prompt import prompt_for_agent

gigachat = GigaChat(temperature=0,
                    top_p=0.1,
                    credentials=Settings.GIGA_CREDENTIALS,
                    model="GigaChat-2",
                    verify_ssl_certs=False)


async def get_ai_answer(user_input):

    prompt = prompt_for_agent.format(
                        question=user_input)

    try:
        response = gigachat.invoke([SystemMessage(content=prompt)])
        content = response.content.strip()
        return content
    except Exception as e:
        logger.error('Error: ', e)
        return