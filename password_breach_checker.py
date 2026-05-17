common = ["123456", "password", "admin123"]

password = input("Enter password: ")

if password in common:
    print("Password compromised ")
else:
    print("Password looks safe ")

print("Security scan complete")
