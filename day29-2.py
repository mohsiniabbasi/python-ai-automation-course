import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
key = os.getenv("NEWS_API_KEY")
gemini_key = os.getenv("GEMINI_API_KEY")


def ask_gemini(question):
    url1 = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
    headers = {"x-goog-api-key": gemini_key}
    body = {"contents": [{"parts": [{"text": question}]}]}
    response = requests.post(url1, headers=headers, json=body)
    data = response.json()
    answer = data["candidates"][0]["content"]["parts"][0]["text"]
    return answer


url = "https://newsapi.org/v2/top-headlines"
info = {"country": "us", "apiKey": key}
response = requests.get(url, params=info)
data = response.json()

articles = data["articles"]
titles = []
for article in articles[1:5]:
    titles.append(article["title"])

text = ""
for title in titles:
    text = text + title + "\n"

question = "Here are some news headlines:\n" + text + "\nDo two things:\n1. Summarise them in 3 short bullet points.\n2. Say which one matters most for a small business owner, and why."
summary = ask_gemini(question)

print("Headlines:")
print(text)
print("Summary:")
print(summary)

f = open("day29-2.txt", "w", encoding="utf-8")
f.write("AI NEWS BRIEF\n\n")
f.write(datetime.now().strftime("%d %B %Y, %H:%M") + "\n\n")
f.write("Summary:\n")
f.write(summary + "\n\n")
f.write("Headlines:\n")
f.write(text)
f.close()

print("\nSummary and headlines written to day29-2.txt")