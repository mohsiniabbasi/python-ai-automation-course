import json
job = '{"pickup": "Mirfield", "Fare": 32,  "customer": {"Name": "Ali", "Phone": "1234567890"}}'
message = json.loads(job)
print(message["customer"]["Name"])
print(message["Fare"])
