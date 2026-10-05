import requests
url = "https://quotes.toscrape.com"
response = requests.get(url)
print(response.status_code)
print(response.text[0:300])
