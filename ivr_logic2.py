import os
import requests
import json
from dotenv import load_dotenv

# --- Set your API key ---
load_dotenv(override=True)
GROQ_API_KEY = os.getenv("API_KEY")
VIBHO_URL = os.getenv("VIBHO_URL")
API_URL = os.getenv("API_URL")
MODEL = "llama-3.1-8b-instant"
content = f"""
    You are an IVR assistant.Give short,helpful replies.
    For information to give replies see here {VIBHO_URL},
    dont give other unrelated numbers like 0 for services,
    Dont tell welcome for all,at about us only mention greetings

"""
def ask_groq(prompt: str)->str:
    """Send prompt to Groq API and return only the assistant's reply."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": content},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 256,
        "temperature": 0.2
    }

    resp = requests.post(API_URL, headers=headers, data=json.dumps(payload))
    resp_json = resp.json()

    # Return only the text content from choices
    try:
        return resp_json["choices"][0]["message"]["content"].strip()
    except KeyError:
        return f" API Error: {resp_json}"


def option_1():
    return ask_groq("Explain Vibho Software Company in simple words suitable for a phone caller.")

def option_2():
    return ask_groq("List the main services offered by Vibho Software Company in a short format for a caller.")

def option_3():
    return ask_groq("Tell the caller the address and location of Vibho Software in simple words.(street no 1,partika nagar,hitechcity,hyderabad,india,headquarts at south africa)")

def option_4():
    return ask_groq("Give short contact details of Vibho Software for a caller.(Natasha is the HR of vibho ,her mobile no is 9701010101)")

def option_5():
    return ask_groq("Explain about the founder or CEO of Vibho Software in very simple words for a phone caller.(Kishor pulluri)")

def option_6():
    return ask_groq("List the current job openings at Vibho Software in short.(dont tell random openings,tell to visit company website at https://www.vibhotech.com/")

def option_7():
    return ask_groq("Tell the caller that a human agent will join shortly.")
def option_8():
    return ask_groq("Tell about available timings(Monday to friday - 10AM to 8PM and saturday,sunday off )")

def option_9():
    return ask_groq("End the call also give a end sound like call end sound")


if __name__ == "__main__":
    print("Option 1 Output:\n", option_1())
    print("\nOption 2 Output:\n", option_2())
    print("\nOption 2 Output:\n", option_3())
    print("\nOption 2 Output:\n", option_4())
    print("\nOption 2 Output:\n", option_5())
    print("\nOption 2 Output:\n", option_6())
    print("\nOption 2 Output:\n", option_7())

    


