from datetime import datetime, timedelta
week_ago = datetime.now() - timedelta(days=7)

print(datetime(2026, 9, 9) > week_ago)
print(datetime(2026, 9, 1) > week_ago)