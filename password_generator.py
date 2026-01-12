import random
import string

print("Password Generator")

length = int(input("Enter password length: "))

password = ""
for i in range(length):
    password += random.choice(string.ascii_letters + string.digits)

print("Generated Password:", password)