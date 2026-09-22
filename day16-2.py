import requests
book_mot = requests.post("https://jsonplaceholder.typicode.com/todos", json={"title": "Book MOT", "completed": False})
print(book_mot.status_code)
created = book_mot.json()
print(created["id"])