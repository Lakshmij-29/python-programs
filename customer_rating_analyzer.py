
ratings = [5, 4, 3, 5, 2, 4, 5, 3]

average = sum(ratings) / len(ratings)
positive = len([rating for rating in ratings if rating >= 4])

print("Average Rating:", round(average, 2))
print("Positive Ratings:", positive)
print("Total Reviews:", len(ratings))

print("Customer Satisfaction:", round(positive / len(ratings) * 100, 2), "%")
