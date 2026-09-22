try:
    lead = {"name": "john", "email": "john@example.com"}
    print(lead["phone"])
except KeyError:
    print("no phone in file")


lead = {"name": "john", "email": "john@example.com"}

if "phone" in lead:
    print(lead["phone"])
else:
    print("no phone in file")