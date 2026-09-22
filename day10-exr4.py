try:
    num1 = float(input("enter 1st number: "))
    num2 = float(input("enter 2nd number: "))
    result = num1 / num2
    print(result)
except ValueError:
    print("that's not a number")
except ZeroDivisionError:
    print("can't divide by zero")