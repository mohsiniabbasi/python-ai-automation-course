import requests
from datetime import datetime

town = input("Which town? ")
url2 = "https://geocoding-api.open-meteo.com/v1/search"
info2 = {"name": town, "count": 1}
response2 = requests.get(url2, params=info2)
data2 = response2.json()
first = data2["results"][0]
lat = first["latitude"]
lon = first["longitude"]
place = first["name"]                  
region = first["admin1"]               
country = first["country"]

url1 = "https://api.open-meteo.com/v1/forecast"
info = {"latitude": lat, "longitude": lon, "current": "temperature_2m"}
response = requests.get(url1, params=info)
data = response.json()
temp = data["current"]["temperature_2m"]
when = data["current"]["time"]
d = datetime.fromisoformat(when)
nice = d.strftime("%A %d %B, %H:%M")
print(f"The temperature of {place}, {region}, {country} at {nice} is {temp} degrees.")