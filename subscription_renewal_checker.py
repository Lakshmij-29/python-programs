days_left = int(input("Days left for subscription: "))

if days_left <= 0:
    print("Subscription expired ")
elif days_left <= 5:
    print("Renew soon ")
else:
    print("Subscription active ")

print("Status checked")
