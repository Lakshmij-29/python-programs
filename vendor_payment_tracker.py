vendors = {
    "Tech_Solutions": 25000,
    "Cloud_Services": 12000,
    "Office_Supplies": 8000
}

budget = 50000
total_due = sum(vendors.values())

print("Total Payments Due:", total_due)
print("Remaining Budget:", budget - total_due)

if total_due > budget:
    print("Budget exceeded")
