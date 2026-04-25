income = float(input("Monthly income: "))
credit = int(input("Credit score: "))
existing_loan = input("Existing loan? yes/no: ").lower()

if income >= 30000 and credit >= 700 and existing_loan == "no":
    print("Loan Approved ")
elif income >= 20000 and credit >= 650:
    print("Loan Under Review ")
else:
    print("Loan Rejected ")

print("Decision completed")
