import requests
leeds = requests.post("https://jsonplaceholder.typicode.com/todos", json={"title": "Collect fare from Leeds job", "completed": False})
screenwash = requests.post("https://jsonplaceholder.typicode.com/todos", json={"title": "Buy screenwash", "completed": False})
opening = requests.post("https://jsonplaceholder.typicode.com/posts", json={"title": "Open Saturday", "body": "We are open 9 to 1 this Saturday"})
print(leeds.status_code)
print(leeds.json())
print(screenwash.status_code)
print(screenwash.json())
print(opening.status_code)
print(opening.json())

