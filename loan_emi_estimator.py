principal = float(input("Loan Amount: "))
rate = float(input("Annual Interest Rate: "))
years = int(input("Loan Period: "))

monthly_rate = rate / 12 / 100
months = years * 12

emi = principal * monthly_rate * (1 + monthly_rate) ** months
emi /= (1 + monthly_rate) ** months - 1

print("Estimated Monthly EMI:", round(emi, 2))
