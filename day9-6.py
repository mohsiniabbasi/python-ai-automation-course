import json

lead = {"name": "john", "email": "john@example.com", "budget": 5000}
f = open("lead.json", "w")
json.dump(lead, f)
f.close()

print("packed")
