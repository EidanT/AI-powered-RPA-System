from ollama import Client
import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv('OLLAMA_URL')
OLLAMA_SECRET = os.getenv('OLLAMA_SECRET')

client = Client(
  host=f'{OLLAMA_URL}',
  headers={'secret': f'{OLLAMA_SECRET}'}
)

system_prompt = """
    You are an AI classifier. Your only purpose is to classify Gmails in 3 categories; HHRR, Support, Tickets or Client.
    Your output MUST be a valid JSON format.
"""

content = """
    Hello
"""

response = client.chat(model='llama3.1:latest', messages=[
    {
        'role': 'system', 
        'content': system_prompt
    },
    {
        'role': 'user',
        'content': f'{content}',
    },
])

print(response['message']['content'])