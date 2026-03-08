password = input("Enter password: ")
length = len(password)

has_digit = any(ch.isdigit() for ch in password)
has_upper = any(ch.isupper() for ch in password)

if length >= 8 and has_digit and has_upper:
    print("Strong password ")
elif length >= 6:
    print("Medium password ")
else:
    print("Weak password ")

print("Password length:", length)
