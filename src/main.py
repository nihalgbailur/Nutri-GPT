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


