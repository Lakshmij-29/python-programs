customer = input("Customer name: ")
points = int(input("Reward points: "))

if points >= 1000:
    tier = "Gold"
elif points >= 500:
    tier = "Silver"
else:
    tier = "Bronze"

print("Customer:", customer)
print("Membership Tier:", tier)
print("Points:", points)
