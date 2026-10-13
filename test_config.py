import os
from dotenv import load_dotenv

load_dotenv()

sender = os.getenv("EMAIL_SENDER")
recipient = os.getenv("EMAIL_RECIPIENT")
host = os.getenv("SMTP_HOST")
password = os.getenv("EMAIL_PASSWORD")

print("Sender configured:", bool(sender))
print("Recipient configured:", bool(recipient))
print("SMTP configured:", host == "smtp.gmail.com")
print("Password configured:", bool(password))
