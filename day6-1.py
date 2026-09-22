def total_invoices(amounts):
    total = 0
    for amount in amounts:
        if amount < 0:
            continue
        total = total + amount
    return total

total_invoices([120, -40, 300, -15, 85])
total_invoices([50, 200, -10])

result = total_invoices([120, -40, 300, -15, 85])
print("result holds:", result)
