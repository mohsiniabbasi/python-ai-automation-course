from datetime import datetime, timedelta
class Taxi:
    def __init__(self, pickup, dropoff, fare, miles, date):
        self.pickup = pickup
        self.dropoff = dropoff
        self.fare = fare
        self.miles = miles
        self.date = date
        self.paid = False

    def cost_per_miles(self):
        return self.fare/self.miles
    def mark_paid(self):
        self.paid = True

j1 = Taxi("Dewsbury" , "Wakefield", 18.40, 9.2, datetime(2026, 9, 8))
j2 = Taxi("Wakefield" , "Leeds", 36.3, 14.6, datetime(2026, 9, 5))
j3 = Taxi("Leeds" , "Bradford", 12.75, 6.1, datetime(2026, 9, 4))
j4 = Taxi("Bradford" , "Dewsbury", 26.90, 11.8, datetime(2026, 9, 2))

jobs = [j1, j2, j3, j4]

total_fare = 0
total_miles = 0

for job in jobs:
    print(f"{job.date.strftime('%A %d %B %Y')} - {job.pickup} to {job.dropoff} £ {job.fare:.2f}")
    total_fare = total_fare + job.fare
    total_miles = total_miles + job.miles
print(f"Total earned: £{total_fare:.2f}")
print(f"Total miles drove: {total_miles:.2f}")
print(f"Average per mile: £{total_fare / total_miles:.2f}")

week_ago = datetime.now() - timedelta(days=7)
week_ago = week_ago.replace(hour=0, minute=0, second=0, microsecond=0)
recent_total = 0

for job in jobs:
    if job.date >= week_ago:
        recent_total = recent_total + job.fare

print(f"Earned in the last 7 days: £{recent_total:.2f}")

