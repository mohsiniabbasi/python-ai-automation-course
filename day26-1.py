import csv
f = open('jobs.csv', 'r')
rows = csv.reader(f)
next(rows)
total = 0
for row in rows:
    print(row[0], row[1])

    total += int(row[1])
print("Total:", total)