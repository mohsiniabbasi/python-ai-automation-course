import time
import requests
from dotenv import load_dotenv
import os

load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")
claude_key = os.getenv("ANTHROPIC_API_KEY")


def ask_claude(question):
    url1 = "https://api.anthropic.com/v1/messages"
    headers = {"x-api-key": claude_key, "anthropic-version": "2023-06-01"}
    body = {"model": "claude-haiku-4-5", "max_tokens": 1000, "messages": [{"role": "user", "content": question}]}
    response = requests.post(url1, headers=headers, json=body)
    data = response.json()
    answer = data["content"][0]["text"]
    return answer


def ask_gemini(question):
    url1 = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
    headers = {"x-goog-api-key": gemini_key}
    body = {"contents": [{"parts": [{"text": question}]}]}
    response = requests.post(url1, headers=headers, json=body)
    data = response.json()
    answer = data["candidates"][0]["content"]["parts"][0]["text"]
    return answer

question = input("What is your question to both AIs? ")

start = time.time()
gemini_answer = ask_gemini(question)
claude_answer = ask_claude(question)
print("Seconds taken:", time.time() - start, 1)

print("\n Gemini's answer:\n", gemini_answer)
print("\n Claude's answer:\n", claude_answer)