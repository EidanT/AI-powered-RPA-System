import json
from emails.services.handle_emails import send_email

async def email_processor(result):
    data = json.loads(result)
    category = data["category"]
    gmail_address = data["gmail"]
    name = data["name"]
    snippet = data["snippet"]

    if category != "spam":
        send_email(category, gmail_address, name, snippet)
    else:
        print("spam")