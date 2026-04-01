from fastapi import FastAPI
import httpx
import asyncio
import os

from dotenv import load_dotenv

load_dotenv()


def fetch_gmail_data(data):
    print(data)
    asyncio.run(run(content=data))
    

SECRET = os.getenv('SECRET')

prompt_system = """
    You are an RPA automation classifier. Your sole task is to analyze incoming emails and classify them into exactly one category.

    Categories:
    - HHRR: Human resources related emails (job applications, payroll, internal HR matters)
    - Support: Technical or internal support requests
    - Client: Emails from or related to clients, business inquiries, sales
    - Spam: Promotional, irrelevant, or unsolicited emails

    Rules:
    - Respond ONLY with a valid JSON object, no extra text, no markdown, no explanation
    - Always return exactly one category and the gmail address
    - If uncertain, choose the most likely category

    Input will contain: gmail address, subject and snippet of the email.

    Response format:
    {
        "category": "hhrr"|"support"|"client"|"spam",
        "gmail": "email@example.com"
    }
"""

async def run(content):
    url = "http://localhost:8088/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {SECRET}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "bitnet",
        "messages": [
            {"role": "system", "content": f"{prompt_system}"},
            {"role": "user", "content": f"{content}"}
        ]
    }

    async with httpx.AsyncClient(timeout=None) as client:
        response = await client.post(url, json=payload, headers=headers)

    data = response.json()

    result = data["choices"][0]["message"]["content"]
    
    print(result)