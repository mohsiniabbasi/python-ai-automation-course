from datetime import datetime
class Expense:
    
    def __init__(self, date, category, description, amount):
        self.category = category
        self.description = description
        self.amount = amount
        self.date = date

exp1 = Expense(datetime(2026, 9, 2), "Fuel", "Shell Dewsbury", 62.40)
exp2 = Expense(datetime(2026, 9, 3), "Insurance", "Monthly premium", 148.65)
exp3 = Expense(datetime(2026 , 9, 4), "Fuel", "ASDA Batley", 55.10)
exp4 = Expense(datetime(2026, 9, 5), "Car wash", "Mini Valet", 15)
exp5 = Expense(datetime(2026, 9, 6), "Repairs", "New front tyre", 75)
exp6 = Expense(datetime(2026, 9, 8), "Fuel", "BP Dewsbury", 35.80)

all_expenses = [exp1, exp2, exp3, exp4, exp5, exp6]

total_expenses = 0

for expenses in all_expenses:
    print(f"{expenses.date.strftime('%A %d %B %Y')} -  {expenses.description}  {expenses.category} £ {expenses.amount:.2f}")
    total_expenses = total_expenses + expenses.amount

print(f"Total expenses: £{total_expenses:.2f}")

fuel_total = 0
for expenses in all_expenses:
    if expenses.category == "Fuel":
        fuel_total = fuel_total + expenses.amount

print(f"Total Fuel: £{fuel_total:.2f}")

income = 94.35
profit = income - total_expenses
print(f"Profit: £{profit:.2f}")