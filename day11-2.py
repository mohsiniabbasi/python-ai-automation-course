class Hotel:
    def __init__(self, number, beds, price):
        self.number = number
        self.beds = beds
        self.price = price
        self.weekly = price * 7
        self.status = "free"

number = input("enter room number: ")
beds = int(input("How many beds: "))
price = float(input("Price per night: "))

r = Hotel(number, beds, price)

print("Rooms", r.number, "costs", r.weekly, "Per week")
print(r.status)
