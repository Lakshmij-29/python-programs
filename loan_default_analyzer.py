
borrowers = {
    "Customer_A": [45000, 12000],
    "Customer_B": [30000, 18000],
    "Customer_C": [65000, 15000],
    "Customer_D": [25000, 16000]
}

for name, data in borrowers.items():
    income, emi = data
    ratio = emi / income * 100
    risk = "High" if ratio > 50 else "Low"
    print(name, "- EMI Ratio:", round(ratio, 2), "% -", risk)
