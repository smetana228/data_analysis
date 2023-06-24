from BA_reviews import reviews_neg,reviews
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import gensim
from gensim import corpora
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()
u=reviews+reviews_neg
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

doc_clean = [clean(doc).split() for doc in u]
merged = [element for each_list in doc_clean for element in each_list]
Counter = Counter(merged)
most_occur = Counter.most_common(25)
print(most_occur)
most_occur.pop(24)
most_occur.pop(23)
most_occur.pop(19)
most_occur.pop(18)
most_occur.pop(9)
most_occur.pop(7)
most_occur.pop(5)
most_occur.pop(2)
most_occur.pop(1)
