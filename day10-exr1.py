try:
    age = int(input("your age: "))
    print(age)
except ValueError:
    print("that's not a number")