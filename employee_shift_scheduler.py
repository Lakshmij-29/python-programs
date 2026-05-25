employees = ["Aman", "Riya", "John", "Sara"]

for i, employee in enumerate(employees):
    if i % 2 == 0:
        shift = "Morning"
    else:
        shift = "Evening"

    print(employee, "->", shift)

print("Shift allocation completed")
