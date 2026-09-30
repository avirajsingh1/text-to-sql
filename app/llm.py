import os

from dotenv import load_dotenv
from google import genai

from prompts import create_prompt

load_dotenv()

client = genai.Client(
    api_key= os.getenv("GEMINI_API_KEY")
)

def generate_sql(user_question):
    prompt = create_prompt(user_question)
    
    response = client.models.generate_content(
        model = "gemini-3.5-flash",
        contents= prompt
    )
    
    sql = response.text.strip()
    
    return sql