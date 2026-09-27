applications = {
    "LN101": "Approved",
    "LN102": "Pending",
    "LN103": "Rejected",
    "LN104": "Approved"
}

approved = list(applications.values()).count("Approved")
pending = list(applications.values()).count("Pending")

print("Total Applications:", len(applications))
print("Approved:", approved)
print("Pending:", pending)

print("Approval Rate:", round(approved / len(applications) * 100, 2), "%")
