import csv
f = open('jobs.csv', 'r')
rows = csv.reader(f)
next(rows)

out = open('big_jobs.csv', 'w', newline='')
writer = csv.writer(out)
writer.writerow(['customer', 'fare'])

for row in rows:
    if int(row[1]) > 10:
        writer.writerow(row)

f.close()
out.close()