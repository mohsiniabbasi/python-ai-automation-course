try:
    f = open("notes.txt", "r")
    content = f.read()
    f.close()
    print(content)
except FileNotFoundError:
    print("no client file yet")

print("finished")



