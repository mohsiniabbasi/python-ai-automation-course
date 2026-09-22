import requests
response = requests.put("https://jsonplaceholder.typicode.com/todos/5", json={"title": "Book MOT", "completed": True})
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json={"title": "Closed Saturday", "body": "Sorry, closed this Saturday"})
#esult = response.json()
print(response.status_code)
print(response.json())
#print(result["completed"])
