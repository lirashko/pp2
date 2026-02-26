from datetime import datetime

date1 = datetime(2024, 1, 1, 12, 0, 0)
date2 = datetime(2024, 1, 1, 12, 10, 0)

difference = date2 - date1

print("Difference in seconds:", difference.total_seconds())