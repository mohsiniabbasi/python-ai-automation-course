import os
print("running in:", os.getcwd())

f = open("lead.csv", "r")
content = f.read()
f.close()

print(content)
print(type(content))