import re

password = input("Enter password: ")
checks = {
    "Length": len(password) >= 12,
    "Uppercase": bool(re.search(r"[A-Z]", password)),
    "Lowercase": bool(re.search(r"[a-z]", password)),
    "Number": bool(re.search(r"\d", password)),
    "Special character": bool(re.search(r"[^a-zA-Z0-9]", password))
}
for rule, passed in checks.items():
    print(rule, ":", "Passed" if passed else "Failed")
print("Strength:", sum(checks.values()), "/ 5")
