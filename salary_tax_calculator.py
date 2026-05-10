salary = float(input("Enter salary: "))

if salary > 1000000:
    tax = salary * 0.30
elif salary > 500000:
    tax = salary * 0.20
else:
    tax = salary * 0.10

print("Tax:", tax)
print("Net Salary:", salary - tax)
