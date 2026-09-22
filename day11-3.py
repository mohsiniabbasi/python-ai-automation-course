class Taxi:
    def __init__(self, pickup, dropoff, fare, miles):
        self.pickup = pickup
        self.dropoff = dropoff
        self.fare = fare
        self.miles = miles
        self.paid = False

    def cost_per_mile(self):
        return self.fare / self.miles
    def mark_paid(self):
        self.paid = True

pickup = input("Pickup from: ")
dropoff = input("Drof off at: ")

while True:
    try:
        miles = float(input("How many miles you travelled: "))
        break
    except ValueError:
        print("Miles should be 15 or 15.65 format only")

while True:
    try:
        fare = float(input("How much you got paid: $"))
        break
    except ValueError:
        print("Fares should be 15 or 15.65 format only")

j = Taxi(pickup, dropoff, fare, miles)
print(j.pickup, "to" ,j.dropoff)
print("Fare:", j.fare)
print(j.paid)
print("Cost per mile:", j.cost_per_mile())

j.mark_paid()
print("Yes got paid", j.paid)