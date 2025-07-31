from dotenv import load_dotenv
import os 

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_aPI_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    
    ALLOWED_MODEL_NAMES = [
        "llama-3.3-70b-versatile",
        "gemma2-9b-it"
    ]
    
settings= Settings()