import requests
from dotenv import load_dotenv
import os

load_dotenv()
claude_key = os.getenv("ANTHROPIC_API_KEY")

def ask_claude(history):
    url1 = "https://api.anthropic.com/v1/messages"
    headers = {"x-api-key": claude_key, "anthropic-version": "2023-06-01"}
    body = {"model": "claude-haiku-4-5", "max_tokens": 1000, "messages": history}
    response = requests.post(url1, headers=headers, json=body)
    data = response.json()
    answer = data["content"][0]["text"]
    return answer

history = []

while True:
    question = input("You: ")
    if question == "quit":
        break
    history.append({"role": "user", "content": question})
    answer = ask_claude(history)
    print("Claude:", answer)
    history.append({"role": "assistant", "content": answer})