import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import uuid
import os
from dotenv import load_dotenv

load_dotenv(override=True)
SENDER_EMAIL=os.getenv("SENDER_EMAIL")
APP_PASSWORD=os.getenv("APP_PASSWORD")

sessions = {}
def pause_ai_call():
    print("AI call paused...")
def user_requests_human(user_id):
    pause_ai_call()
    session_id = str(uuid.uuid4())
    sessions[session_id] = {"user_id":user_id,"human_connected":False}
    print(f"Session created: {session_id} for user {user_id}")
    return session_id
def send_email_to_human(session_id: str, human_email: str, base_url: str):
    link = f"{base_url}/human_call?session_id={session_id}"
    sender_email =SENDER_EMAIL
    app_password =APP_PASSWORD

    subject = "Join Your Call"
    body = f"Hello,\n\nPlease click the link below to join your call:\n\n{link}\n\nThanks,\nYour IVR System"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = human_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, app_password)
        server.sendmail(sender_email, human_email, msg.as_string())
        server.quit()
        print(f"Email sent successfully to {human_email}!")
    except Exception as e:
        print("Failed to send email:", e)
