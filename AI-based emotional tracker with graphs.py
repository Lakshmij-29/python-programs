from textblob import TextBlob
import matplotlib.pyplot as plt

texts = ["I am happy", "I feel sad", "This is exciting!", "I am angry"]
emotions = {'Positive':0, 'Negative':0, 'Neutral':0}

for text in texts:
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0: emotions['Positive'] += 1
    elif polarity < 0: emotions['Negative'] += 1
    else: emotions['Neutral'] += 1

plt.bar(emotions.keys(), emotions.values(), color=['green','red','blue'])
plt.title("Emotion Distribution")
plt.show()
