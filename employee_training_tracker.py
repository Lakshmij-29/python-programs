employees = ["Aman", "Neha", "John", "Sara"]
completed = ["Aman", "Sara"]

for employee in employees:
    if employee in completed:
        print(employee, "- Training Complete")
    else:
        print(employee, "- Training Pending")

completion = len(completed) / len(employees) * 100
print("Completion Rate:", completion, "%")
