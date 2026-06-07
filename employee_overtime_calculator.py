hours = int(input("Hours worked this week: "))

regular = min(hours, 40)
overtime = max(hours - 40, 0)

pay = (regular * 20) + (overtime * 30)

print("Regular Hours:", regular)
print("Overtime Hours:", overtime)
print("Weekly Pay:", pay)
