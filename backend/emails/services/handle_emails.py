import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
from datetime import datetime
import uuid

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def send_email(category, gmail, name, snippet):
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT   = 587
    FROM        = os.getenv("MY_GMAIL_ADDRESS")
    PASSWORD    = os.getenv("GMAIL_APP_PASSWORD")   
    TO          = gmail
    date = datetime.now().strftime("%m/%d/%Y")

    msg = MIMEMultipart("alternative")
    msg["From"]    = FROM
    msg["To"]      = TO

    if category == "hhrr":
        msg["Subject"] = "Application confirmed"
        html_template_file = "hhrr.html"
    elif category == "client":
        msg["Subject"] = "Thank you for contacting us"
        html_template_file = "client.html"
    else:
        ticket_id = f"{datetime.now().strftime('%Y%m%d')}-{str(uuid.uuid4())[:6].upper()}"
        msg["Subject"] = f"We received your request - Support Ticket #{ticket_id}"
        html_template_file = "support.html"


    template_path = os.path.join(BASE_DIR, "html_template", html_template_file)
    reference = f"HHRR-{datetime.now().strftime('%Y%m%d')}-{str(uuid.uuid4())[:6].upper()}"

    with open(template_path) as f:
        html = f.read()

    html = html.replace("{{name}}", name)
    html = html.replace("{{reference}}", reference)
    html = html.replace("{{date}}", date)
    html = html.replace("{{problem_message}}", snippet)
    html = html.replace("{{ticket_id}}", ticket_id)


    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.ehlo()
        server.starttls()
        server.login(FROM, PASSWORD)
        server.sendmail(FROM, TO, msg.as_string())
        print("Sent")