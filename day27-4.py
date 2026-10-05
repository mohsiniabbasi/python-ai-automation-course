import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
boxes = soup.find_all("div", class_="quote")
for box in boxes:
    text = box.find("span", class_="text").text
    author = box.find("small", class_="author").text
    print(author, "-", text)
    