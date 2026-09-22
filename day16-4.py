import requests
response = requests.delete("https://jsonplaceholder.typicode.com/todos/8", json={"title": "Collect fare from Leeds job", "completed": True})
print(response.status_code)
result = response.json()
print(result["completed"])
