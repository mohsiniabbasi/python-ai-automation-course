import requests
url1 = "https://api.open-meteo.com/v1/forecast"
info = {"latitude": 53.68, "longitude": -1.63, "current": "temperature_2m"}
response = requests.get(url1, params=info)
data = response.json()
temp = data["current"]["temperature_2m"]
when = data["current"]["time"]
print(f"The temperature of Mirfield at {when} is {temp} degrees.")
