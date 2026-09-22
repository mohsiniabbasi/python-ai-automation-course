import requests
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("NEWS_API_KEY")
url1 = "https://newsapi.org/v2/top-headlines"
info = {"country": "us", "apiKey": key}
response = requests.get(url1, params=info)
data = response.json()
print(response.status_code)

articles = data["articles"]
count = 1
for article in articles:
    title = article["title"]
    source = article["source"]["name"]
    print(f"{count}. {title} — {source}")
    count = count + 1