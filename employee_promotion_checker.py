employees = {
    "Aman": [4.5, 92],
    "Riya": [3.2, 88],
    "Kiran": [5.1, 95],
    "Neha": [2.8, 91]
}

for name, data in employees.items():
    experience, performance = data
    eligible = experience >= 4 and performance >= 90
    print(name, "-", "Eligible" if eligible else "Not Eligible")
