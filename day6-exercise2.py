def order_total(price, quantity):
    return price * quantity
price = int(input("Enter price: "))
quantity = int(input("Enter quantity: "))
result = order_total(price, quantity)
print(result)

whole = 25
decimal = 25.50
print(whole)
print(decimal)
print(type(whole), type(decimal))


print(type("hello"))
print(type([1, 2, 3]))
print(type({"name": "Mohsan"}))
print(type((1, 2)))
print(type(True))
print(type(order_total))