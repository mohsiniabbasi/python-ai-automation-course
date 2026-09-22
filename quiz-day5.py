amounts = [120, -40, 300, -15, 85]
total = 0
for amount in amounts:
    if amount < 0:
        continue
    total = total + amount
print(f"Total: ${total}")

amounts = [120, -40, 300, -15, 85]
for amount in amounts:
    total = 0
    if amount < 0:
        continue
    total = total + amount
print(f"Total: ${total}")