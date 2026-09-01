import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()

def get_llm():
    api_base = os.getenv("LLM_API_BASE", "http://localhost:11434")
    
    return ChatOllama(
        model="qwen2.5-coder:14b",
        base_url=api_base,
        temperature=0.2
    )