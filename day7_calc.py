def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        result = add(a, b)
        print("The sum is:", result)
    elif operation == "-":
        result = subtract(a, b)
        print("The difference is:", result)
    elif operation == "*":
        result = multiply(a, b)
        print("The multiplication is:", result)
    elif operation == "/":
        if b != 0:
            result = divide(a, b)
            print("The division is:", result)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Sorry, I don't recognise that operation.")