projects = {
    "AI_App": 3,
    "Website": 10,
    "Dashboard": 1
}

for project, days in projects.items():
    print(project, "-", days, "days left")

    if days <= 2:
        print("Deadline approaching")
