
products = {
    "Laptop": {"Python": 5, "Gaming": 4},
    "Phone": {"Python": 2, "Gaming": 3},
    "Tablet": {"Python": 3, "Gaming": 2},
    "PC": {"Python": 5, "Gaming": 5}
}

user_interest = "Python"

ranked = sorted(
    products.items(),
    key=lambda item: item[1][user_interest],
    reverse=True
)

for product, scores in ranked:
    print(product, "-", scores[user_interest])
