from langchain.chat_models import ChatOpenAI
from config import OPENAI_API_KEY

def get_llm():
    return ChatOpenAI(model="gpt-4", temperature=0, openai_api_key=OPENAI_API_KEY)