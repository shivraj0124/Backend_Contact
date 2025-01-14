import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
load_dotenv()

def sendmail(name, email, message):

    smtp_server = os.getenv("smtp_server")
    smtp_port = os.getenv("smtp_port")
    sender_email = os.getenv("sender_email")
    sender_password = os.getenv("sender_password")
    recipient_email = os.getenv("recipient_email")

    subject = f"Message from {name}"
    body = f"Name: {name} \n\nEmail: {email}\n\nMessage: {message}\n\n"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
        raise e
