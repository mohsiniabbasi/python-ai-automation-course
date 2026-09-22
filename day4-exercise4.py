lead = {
    "name": "Eisa",
    "Budget": int(input("Enter the budget for the lead: ")),
    "Country": input("Enter the country for the lead: ")
}
if lead["Budget"] > 5000 and lead["Country"] == "UK":
    print(f"{lead["name"]}: PRIORITY - send to a senior rep")
elif lead["Budget"] > 5000 and lead["Country"] != "UK":
    print(f"{lead["name"]}: high budget, overseas - send to the export team")
elif lead["Budget"] >= 1000:
    print(f"{lead["name"]}: standard lead - add to the nurture sequence")
else:
    print(f"{lead["name"]}: low budget - send the self-serve guide")