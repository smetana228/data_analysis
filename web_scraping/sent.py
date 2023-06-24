import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt
nltk.download('vader_lexicon')
data = pd.read_csv('BA_reviews.csv')
sia = SentimentIntensityAnalyzer()
def classify_sentiment(text):
    sentiment = sia.polarity_scores(text)
    compound_score = sentiment['compound']
    if compound_score >= 0.1:
        return 'Positive'
    elif compound_score <= -0.1:
        return 'Negative'
    else:
        return 'Neutral'
data['sentiment'] = data['reviews'].apply(classify_sentiment)
sentiment_counts = data['sentiment'].value_counts()
labels = sentiment_counts.index
sizes = sentiment_counts.values
font = {'size'   : 10}

plt.rc('font', **font)
colors = ['#29a329','#ab2121','#8c8c8c']
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,colors=colors)
ax.axis('equal')

plt.title('Sentiment Distribution')
plt.show()