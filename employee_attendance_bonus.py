days = int(input("Days attended this month: "))

if days >= 26:
    bonus = 5000
elif days >= 22:
    bonus = 2000
else:
    bonus = 0

print("Attendance bonus:", bonus)
print("Calculation complete")
