
posts = {
    "Post_1": [1200, 85, 42],
    "Post_2": [2100, 160, 75],
    "Post_3": [900, 60, 25]
}

for post, metrics in posts.items():
    views, likes, shares = metrics
    engagement = (likes + shares) / views * 100
    print(post, "-", round(engagement, 2), "%")

best = max(posts, key=lambda x: (posts[x][1] + posts[x][2]) / posts[x][0])
print("Highest Engagement:", best)
