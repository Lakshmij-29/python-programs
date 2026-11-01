password = input("Enter password: ")

score = 0
score += len(password) >= 12
score += any(c.isupper() for c in password)
score += any(c.islower() for c in password)
score += any(c.isdigit() for c in password)
score += any(not c.isalnum() for c in password)

print("Strength Score:", score, "/5")
print("Strong" if score >= 4 and len(password) >= 12 else "Needs Improvement")
