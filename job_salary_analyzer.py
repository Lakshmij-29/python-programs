

jobs = {
    "Data Analyst": 600000,
    "AI Engineer": 1200000,
    "Python Developer": 750000,
    "ML Engineer": 1100000
}

average = sum(jobs.values()) / len(jobs)

for role, salary in jobs.items():
    print(role, "- ₹", salary)

print("Average Salary:", round(average))
print("Highest Paying Role:", max(jobs, key=jobs.get))
