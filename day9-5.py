import csv
f = open("lead.csv", "w", newline="")
writer = csv.writer(f)

writer.writerow(["name", "email", "budget"])
writer.writerow(["amir", "amir@emaple.com", "4000"])


#for row in reader:
 #   print (row)

f.close()
print("written")


budget = "5000"
print(int(budget) + 1000)