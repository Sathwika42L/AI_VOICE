from fastapi import FastAPI, Form
from ivr_logic2 import option_1, option_2,option_3,option_4,option_5,option_6,option_7,option_8,option_9
import pyttsx3
from send_email import send_email_to_human,user_requests_human
from dotenv import load_dotenv
import os

load_dotenv(override=True)
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
DEFAULT_USERNAME = os.getenv("DEFAULT_USERNAME")
HUMAN_EMAIL = os.getenv("HUMAN_EMAIL")

app = FastAPI()

def speak(text: str):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

@app.get("/call")
def call():
    greeting = "Thank you for calling Vibho Software Company. Press 1 for About Us, 2 for Services,3 for address,4 for contact details,5 for CEO details,6 for current job openings,7 for contact human agent,8 for available timings,9 to end up call"
    speak(greeting)
    return {"response": greeting}

@app.post("/press")
def press(key: int = Form(...)):
    if key == 1:
        reply = option_1()
    elif key == 2:
        reply = option_2()
    elif key == 3:
        reply = option_3()
    elif key == 4:
        reply = option_4()
    elif key == 5:
        reply = option_5()
    elif key == 6:
        reply = option_6()
    elif key == 7:
        reply = option_7()
        session_id = user_requests_human(DEFAULT_USERNAME)
        send_email_to_human(session_id,HUMAN_EMAIL, BASE_URL)

    elif key == 8:
        reply = option_8()
    elif key == 9:
        reply = option_9()

    else:
        reply = "Invalid option. Please press between 1 to 9."
    
    speak(reply)
    return {"response": reply}
