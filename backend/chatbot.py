from google import genai
from rag import retrieve_answer
from config import GEMINI_API_KEY

# Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

def get_response(message):

    try:

        # Retrieve FAQ answer
        retrieved_data = retrieve_answer(message)

        # Prompt
        prompt = f"""
You are an AI Customer Support Assistant.

Use the following company information to answer professionally.

Company Information:
{retrieved_data}

Customer Question:
{message}
"""

        # Generate Gemini response
        response = client.models.generate_content(
            model="gemini-1.5-pro",
            contents=prompt
        )

        return response.text

    except Exception as e:

        print("Gemini Error:", e)

        return retrieve_answer(message)