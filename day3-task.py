lead = {"name": "john doe", 
        "email": "john@example.com",
        "budget": 5000
        }
print (lead["name"] .title(), lead["email"])
print (f"{lead['name'] .title()} - ({lead['email']})")
print (lead.get("phone"))
services = ["SEO", "GEO", "Webdesign", "SEO"]

services.append("automation")           
print (services)
services.remove("GEO")
print (services)
unique_services = set(services)
print (services)
company = ("Pivot Bureau", 2024)
print (company[-1])
print (len(unique_services))


