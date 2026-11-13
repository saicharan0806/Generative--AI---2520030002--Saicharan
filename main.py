from dotenv import load_dotenv
from google import genai
import os
load_dotenv()
api_key = os.getenv("GEMINI_KEY")
if not api_key:
    raise ValueError("Gemini api key is not found")
client = genai.Client(api_key = api_key)
response = client.models.generate_content(
    model = "gemini-3.5-flash-lite",
    contents = "What is Deep Learning? Explain in simple words?"
)
print("\nLLM Response:")
print(response.text)