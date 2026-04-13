import os
from dotenv import load_dotenv
from google import genai
from pinecone import Pinecone
from openai import OpenAI

load_dotenv()

# --- Constants ---
EMBEDDING_MODEL = "gemini-embedding-2-preview"
EMBEDDING_DIMENSION = int(os.getenv("EMBEDDING_DIMENSION", "1536"))
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "multimodal-embeddings")
PINECONE_METRIC = "cosine"
MAX_VIDEO_SECONDS = 120

SUPPORTED_IMAGE_EXT = {".png", ".jpg", ".jpeg"}
SUPPORTED_VIDEO_EXT = {".mp4", ".mov"}
SUPPORTED_TEXT_EXT = {".txt", ".md", ".html", ".json", ".csv"}

# --- Clients ---
gemini_client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

pc_client = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

openrouter_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)
