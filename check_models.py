import requests,os
from dotenv import load_dotenv

load_dotenv(override=True)
GROQ_API_KEY =os.getenv("API_KEY")

CHECK_MODEL_URL=os.getenv("CHECK_MODEL_URL")
headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}"
}

response = requests.get(CHECK_MODEL_URL, headers=headers)
print(response.json())
