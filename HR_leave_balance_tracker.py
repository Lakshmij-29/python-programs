name = input("Employee name: ")
total_leave = 24
used = int(input("Leaves used this year: "))

balance = total_leave - used

print("Employee:", name)
print("Leave balance:", balance)

if balance < 5:
    print("Low leave balance ")
