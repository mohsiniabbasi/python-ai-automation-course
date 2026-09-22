import requests
response = requests.delete("https://jsonplaceholder.typicode.com/todos/3")
print(response.status_code)