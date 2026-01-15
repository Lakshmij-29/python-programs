email = input("Enter your email: ")

username, domain = email.split("@")

print("Username:", username)
print("Domain:", domain)

if domain == "gmail.com":
    print("Gmail user detected")