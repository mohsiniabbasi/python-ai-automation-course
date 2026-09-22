import requests
response = requests.get("https://api.postcodes.io/postcodes/WF129pu")
#print(response.status_code)
#print(response.text)
data = response.json()
print(data["status"])
print(data["result"]["postcode"])
print(data["result"]["admin_ward"])
print(data["result"]["parliamentary_constituency"])
print(data["result"]["region"])

