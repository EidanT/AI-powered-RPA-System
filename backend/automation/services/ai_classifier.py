import httpx
import asyncio
import os
from .email_processor import email_processor

from dotenv import load_dotenv

load_dotenv()


def fetch_gmail_data(data):
    print(data)
    asyncio.run(run(content=data))
    

SECRET = os.getenv('SECRET')

system_prompt = """
You are an RPA automation classifier. Your sole task is to analyze incoming emails and classify them into exactly one category based on sender, subject, and content.

## Categories:

- **hhrr**: Human resources emails. Includes: job applications, CVs/resumes, employment inquiries, interview requests, internship applications, recruitment outreach, payroll questions, onboarding, employee benefits, performance reviews, or any email where someone is seeking or managing employment.
- **support**: Technical or operational support requests. Includes: bug reports, system errors, help requests, account issues, internal IT requests, or any email where someone needs assistance resolving a problem.
- **client**: Emails from clients or prospects. Includes: business inquiries, quotes, project proposals, partnerships, sales-related messages, contract discussions, or any email involving a commercial relationship.
- **spam**: Unsolicited, promotional, or irrelevant emails. Includes: newsletters, marketing campaigns, cold ads, phishing attempts, or emails with no actionable business content.

## Classification Priority (when ambiguous):
1. If the email contains a CV, resume, or job application → always hhrr
2. If someone is asking for help with a system or service → support
3. If it involves a business deal, quote, or client relationship → client
4. If none of the above → spam

## Strict Rules:
- Respond ONLY with a valid JSON object. No extra text, no markdown, no explanation.
- Always return exactly one category, the sender email address, and the sender display name.
- `name`: extract only the display name from before `< >` if present. If no display name exists, use the part before `@` in the email address.
- `gmail`: the raw email address only, no spaces, no formatting.
- If uncertain, choose the most likely category based on subject and snippet.

## Output Format:
{
    "category": "hhrr" | "support" | "client" | "spam",
    "gmail": "sender@example.com",
    "name": "Sender Name"
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
            {"role": "system", "content": f"{system_prompt}"},
            {"role": "user", "content": f"{content}"}
        ]
    }

    async with httpx.AsyncClient(timeout=None) as client:
        response = await client.post(url, json=payload, headers=headers)

    data = response.json()

    result = data["choices"][0]["message"]["content"]
    
    print(result)

    await email_processor(result) 