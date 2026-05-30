tasks = {
    "Alex": 15,
    "Sam": 8,
    "Neha": 20
}

for employee, completed in tasks.items():
    print(employee, "- Tasks:", completed)

    if completed >= 15:
        print("High productivity")
