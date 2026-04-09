import json
from client.views import client
from emails.services.handle_emails import send_email

async def email_processor(result):
    data = json.loads(result)
    category = data["category"]
    gmail_address = data["gmail"]
    name = data["name"]

    if data["category"] == "hhrr":
        send_email(category, gmail_address, name)
    elif data["category"] == "client":
        client(gmail_address)
        send_email(category, gmail_address, name)
    elif data["category"] == "support":
        send_email(category, gmail_address, name)
    else:
        print("spam")