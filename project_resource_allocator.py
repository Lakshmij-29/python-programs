team_members = 12
projects = 3

members_per_project = team_members // projects

for i in range(1, projects + 1):
    print("Project", i,
          "gets", members_per_project, "members")

print("Allocation Complete")
