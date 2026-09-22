for number in range(1, 20):
    if number % 3 == 0:
        print(number)

statuses = ["paid", "paid", "unpaid", "paid", "unpaid"]
for status in statuses:
    if status == "unpaid":
        print("You have an unpaid invoice!")
        break
    print(status)

amounts = [120, -40, 300, -15, 85]
total = 0
for amount in amounts:
    if amount < 0:
        continue
    total = total + amount
print(f"Total: ${total}")
