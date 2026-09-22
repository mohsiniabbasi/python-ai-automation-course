try:
    f = open("missing.csv", "r")
    content = f.read()
    f.close()
    print(content)
except FileNotFoundError as e:
    print("could't open it:", e)
    #print("That file not there")

print("carry on")

try:
    print("trying")
    print(1 / 0)
except ZeroDivisionError:
    print("can't divide by zero")
finally:
    print("this runs no matter what")