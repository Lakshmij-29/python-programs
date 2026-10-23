
employees = {
    "Aman": [2, 4],
    "Riya": [6, 9],
    "Kiran": [1, 3],
    "Neha": [5, 8]
}

for name, data in employees.items():
    years, satisfaction = data

    if years < 2 and satisfaction <= 4:
        risk = "High"
    elif satisfaction <= 5:
        risk = "Medium"
    else:
        risk = "Low"

    print(name, "- Attrition Risk:", risk)
