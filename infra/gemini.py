import requests
import os
import json
from dotenv import load_dotenv
from fastapi import HTTPException


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, "../.env"))

def questionToGemini(content: str):
    URI = os.environ["GEMINI_API_URL"] + "?key=" + os.environ["GEMINI_API_KEY"]
    headers = { "Content-Type": "application/json" }
    data = {
        "contents": [
            {
                "parts": [
                    {"text": content}
                ]
            }
        ]
    }
    try :
        response = requests.post(URI, headers=headers, data=json.dumps(data))
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except requests.ConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Error Gemini API: {e}")