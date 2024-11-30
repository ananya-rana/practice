from openai import OpenAI
from dotenv import load_dotenv
import os

# Load the variables from .env
load_dotenv()

# Access the API key
api_key = os.getenv("API_KEY")
client = OpenAI(api_key=api_key)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"},
                    "unit": {"type": "string", "enum": ["c", "f"]},
                },
                "required": ["location", "unit"],
                "additionalProperties": False,
            },
        },
    }
]

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "What's the weather like in Paris today?"}],
    tools=tools,
)

print(completion.choices[0].message.tool_calls)
