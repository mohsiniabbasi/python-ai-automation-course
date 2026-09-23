import requests
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("GEMINI_API_KEY")

url1 = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
question = input("Ask me a question: ")
headers = {"x-goog-api-key": key}
body = {"contents": [{"parts": [{"text": question}]}]}
response = requests.post(url1, headers=headers, json=body)
print(response.status_code)
data = response.json()
#print(data)
answer = data["candidates"][0]["content"]["parts"][0]["text"]
print(answer)


