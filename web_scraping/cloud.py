from BA_reviews import reviews_neg,reviews
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import gensim
from gensim import corpora
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
t=''.join(map(str,reviews_neg))
t_=''.join(map(str,reviews))
r=t+' '+t_
'''
stopwords = set(STOPWORDS)
stopwords.update(['will','British Airways','Trip', 'Verified', 'Not','British',
				 'Airway','British Airway','London','airline', 'BA','Trip Verified',
				 'Not Verified','airlines','Gatwick','Heathrow','Airways'])
wordcloud = WordCloud(stopwords=stopwords,background_color="white").generate(r)
print(wordcloud)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

doc_clean = [clean(doc).split() for doc in reviews_neg]
dct=Dictionary(doc_clean)
doc_term_matrix = [dct.doc2bow(doc) for doc in doc_clean]
Lda = gensim.models.ldamodel.LdaModel

ldamodel = Lda(doc_term_matrix, num_topics=10, id2word = dct, passes=50)

print(ldamodel.print_topics(num_topics=10, num_words=3))
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer 
from sklearn.decomposition import LatentDirichletAllocation as LDA
from nltk import corpus
from nltk.corpus import stopwords
count_vect=CountVectorizer(stop_words=stopwords.words('english'),lowercase=True)
x_counts=count_vect.fit_transform(reviews_neg)
x_counts.todense()

tfidf_transformer = TfidfTransformer()
x_tfidf = tfidf_transformer.fit_transform(x_counts)

dimension = 10
lda = LDA(n_components = dimension)
lda_array = lda.fit_transform(x_tfidf)

components = [lda.components_[i] for i in range(len(lda.components_))]
features = count_vect.get_feature_names_out()
features = list(features)
important_words = [sorted(features, key = lambda x: components[j][features.index(x)], reverse = True)[:3] for j in range(len(components))]
print(important_words)
'''