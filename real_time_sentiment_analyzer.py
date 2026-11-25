from transformers import pipeline

analyzer = pipeline("sentiment-analysis")
reviews = [
    "The product quality is excellent",
    "Delivery was extremely disappointing",
    "The service was average"
]
for review in reviews:
    result = analyzer(review)[0]
    print("Review:", review)
    print("Sentiment:", result["label"])
    print("Confidence:", round(result["score"], 3))
