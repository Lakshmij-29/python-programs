
reviews = [
    "excellent service",
    "poor delivery",
    "great product",
    "bad experience"
]

positive = ["excellent", "great", "good", "happy"]
negative = ["poor", "bad", "slow", "terrible"]

for review in reviews:
    score = sum(word in review for word in positive)
    score -= sum(word in review for word in negative)
    sentiment = "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"
    print(review, "-", sentiment)
