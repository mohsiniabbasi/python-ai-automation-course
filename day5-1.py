cities = ["leeds", "london", "manchester", "birmingham", "bristol" ]
print("--break--")
for city in cities:
    if city == "manchester":
        break
    print("hohoho ", city.title())      #← this one

for city in cities:
    if city == "manchester":
        continue
    print("hohoho ", city.title())

for number in range(0, 5):
    print(number)
count = 3
while count > 0:
    print(count)
    count -= 1
print("Blast off!")
