attempts = [True, False, False, False, True]

failed = attempts.count(False)

print("Failed Logins:", failed)

if failed >= 3:
    print("Security Alert Triggered")
else:
    print("System Secure")

print("Monitoring completed")
