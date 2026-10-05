from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.append(["customer", "fare"])
ws.append(["Alice", 12])
ws.append(["Bob", 20])
wb.save("report.xlsx")
