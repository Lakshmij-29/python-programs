
login_attempts = {
    "192.168.1.10": 3,
    "192.168.1.15": 9,
    "192.168.1.20": 2,
    "192.168.1.25": 12
}

for address, attempts in login_attempts.items():
    if attempts >= 10:
        status = "High Alert"
    elif attempts >= 5:
        status = "Suspicious"
    else:
        status = "Normal"

    print(address, "-", attempts, "-", status)
