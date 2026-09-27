import requests
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("ANTHROPIC_API_KEY")

url1 = "https://api.anthropic.com/v1/messages"
question = input("Ask me a question: ")
headers = {"x-api-key": key, "anthropic-version": "2023-06-01"}
body = {"model": "claude-haiku-4-5", "max_tokens": 1000, "messages": [{"role": "user", "content": question}]}
response = requests.post(url1, headers=headers, json=body)
print(response.status_code)
data = response.json()
answer = data["content"][0]["text"]
print(answer)