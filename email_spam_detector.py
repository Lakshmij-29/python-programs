
message = input("Enter email message: ").lower()
spam_words = ["win money", "claim prize", "free offer", "urgent payment"]

matches = [word for word in spam_words if word in message]
score = len(matches)

print("Suspicious Phrases:", matches)
print("Risk Score:", score)

if score >= 2:
    print("Potential Spam")
elif score == 1:
    print("Review Email Carefully")
else:
    print("No Known Spam Phrases Found")
