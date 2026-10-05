import csv
from openpyxl import Workbook

f = open('jobs.csv', 'r')
rows = csv.reader(f)
next(rows)  # Skip header row

wb = Workbook()
ws = wb.active
ws.append(["customer", "fare"])  # Add header row to Excel

total = 0
for row in rows:
    ws.append([row[0], int(row[1])])  # Append each row to Excel
    total = total + int(row[1])  # Calculate total fare

ws.append(["Total", total])  # Add total row to Excel
f.close()
wb.save('report.xlsx')  # Save the Excel file
