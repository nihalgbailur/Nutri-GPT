import os
import openai
from loguru import logger
# Load environment variables from .env file
from dotenv import load_dotenv
# OpenAI LLM wrapper used by LlamaIndex
from llama_index.llms import OpenAI as LlamaOpenAI
# Used to build vector index from your documents
from llama_index import VectorStoreIndex
# Reads documents from a local folder (e.g., /data/)
from llama_index import SimpleDirectoryReader
# Centralized context manager for LLM settings (model, embeddings, etc.)
from llama_index import ServiceContext

# load env variables
load_dotenv()

api_key=os.getenv("OPEN_API_KEY") 

logger.add("logs/app.log",rotation="10 MB")
service_context = ServiceContext.from_defaults(
    llm=LlamaOpenAI(model="gpt-4")
)
# Build index
def build_food_index(data_path: str = "data") -> VectorStoreIndex:
    try:
        documents = SimpleDirectoryReader(data_path).load_data()
        index = VectorStoreIndex.from_documents(documents, service_context=service_context)
        logger.info("Food knowledge index built successfully.")
        return index
    except Exception as e:
        logger.error(f"Error building index: {str(e)}")
        return None
