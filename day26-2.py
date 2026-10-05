import csv
f = open('big_jobs.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(['customer', 'fare'])
writer.writerow(['Ali', 12])
f.close()
