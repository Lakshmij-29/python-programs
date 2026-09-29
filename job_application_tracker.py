applications = {
    "Company_A": "Interview",
    "Company_B": "Rejected",
    "Company_C": "Applied",
    "Company_D": "Selected"
}

for company, status in applications.items():
    print(company, "-", status)

selected = list(applications.values()).count("Selected")
print("Selected Applications:", selected)
