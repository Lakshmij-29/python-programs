
login_attempts = {
    "User_A": 2,
    "User_B": 7,
    "User_C": 1,
    "User_D": 9
}

for user, attempts in login_attempts.items():
    if attempts > 5:
        print(user, "- Security Alert")
    else:
        print(user, "- Normal Activity")

print("Security monitoring completed")
