
visitors = 15000
signups = 2400
purchases = 850

signup_rate = signups / visitors * 100
conversion_rate = purchases / visitors * 100

print("Total Visitors:", visitors)
print("Signups:", signups)
print("Purchases:", purchases)
print("Signup Rate:", round(signup_rate, 2), "%")
print("Conversion Rate:", round(conversion_rate, 2), "%")
