while True:
    password = input("Enter password: ")
    if password == "nice01":
        print("welcome")
        break
    print("WRONG, Try again")\

names = []
while True:
    name = input("name (or 'stop'): ")
    if name == "stop":
        break
    names.append(name)

print(names)
