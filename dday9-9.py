import json
f = open("lead.json", "r")
lead = json.load(f)
f.close()

print(lead)
print(type(lead))
print(lead["name"])

print(lead["budget"] + 1000)
