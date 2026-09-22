bill = float(input("enter bill amount $"))
tip_percent = int(input("tip percentage %"))
tip = bill * tip_percent / 100
print(f"tip: ${tip: .2f}")
print(f"total bill: ${bill + tip: .2f} ")
