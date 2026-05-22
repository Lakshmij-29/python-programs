employees = {
    "Rahul": 45000,
    "Anu": 52000,
    "David": 61000
}

for name, salary in employees.items():
    tax = salary * 0.10
    net = salary - tax

    print(name, "Net Salary:", net)

print("Payroll generated successfully")
