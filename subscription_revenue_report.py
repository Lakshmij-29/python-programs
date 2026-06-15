subscriptions = [499, 999, 499, 1999, 999]

revenue = sum(subscriptions)
average = revenue / len(subscriptions)

print("Total Revenue:", revenue)
print("Average Revenue:", average)

premium = subscriptions.count(1999)
print("Premium Subscribers:", premium)
