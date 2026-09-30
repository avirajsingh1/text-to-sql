import os

from dotenv import load_dotenv
# from google import genai
from google.genai import types

from models import QueryAnalysis
from clarification_prompt import create_analysis_prompt


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = os.getenv("GEMINI_MODEL")


def analyze_query(user_question):

    prompt = create_analysis_prompt(user_question)

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=QueryAnalysis,
        ),
    )

    analysis = QueryAnalysis.model_validate_json(
        response.text
    )

    return analysis