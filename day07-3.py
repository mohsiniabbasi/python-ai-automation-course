names = []
while True:
    name = input("name (or 'stop'): ")
    if name == "stop":
        break
    names.append(name)
    print(names)

print(names)