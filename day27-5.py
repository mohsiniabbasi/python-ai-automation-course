import csv
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

out = open("quotes.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(out)
writer.writerow(['Author', 'Quote' ])  # Write header row

boxes = soup.find_all("div", class_="quote")
for box in boxes:
    text = box.find("span", class_="text").text
    author = box.find("small", class_="author").text
    writer.writerow([author, text])  # Write each quote to CSV
    
out.close()