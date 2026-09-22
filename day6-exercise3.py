orders = [[25, 4], [10, 3], [50, 1]]
def order_total(price, quantity):
    return price * quantity
for order in orders:
    print(order_total(order[0], order[1]))


orders = [[25, 4], [10, 3], [50, 1]]
print(orders[0])
print(orders[1])

def add_vat(amount):
    return amount * 2

total = add_vat(100)
print(total)
print(add_vat(50))