import requests
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("NEWS_API_KEY")
url = f"https://newsapi.org/v2/top-headlines"
info = {
    "country": "us",
    "apiKey": key
}
response = requests.get(url, params=info)
data = response.json()

articles = data["articles"]
titles = []
for article in articles[1:5]:
    titles.append(article["title"])

print(len(titles), "articles found.")
for title in titles:
    print(title)

