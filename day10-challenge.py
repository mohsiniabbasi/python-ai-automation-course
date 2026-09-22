import csv

total = 0
good = 0
bad = 0

f = open("messy_leads.csv", "r")
rows = csv.reader(f)
next(rows)

for row in rows:
    try:
        total = total + int(row[2])
        good = good + 1
    except ValueError:
        bad = bad + 1
        print("bad row:", row)
    except ValueError:
        bad = bad + 1
        print("bad row (not a number):", row)
    except IndexError:
        bad = bad + 1
        print("bad row (missing column):", row)
f.close()

print("good rows:", good)
print("bad rows:", bad)
print("total budget:", total)