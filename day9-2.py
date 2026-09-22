import os
print("running in:", os.getcwd())

f = open("notes.txt", "w")
f.write("hello")
f.close()

print("done - file written")