#Data Cleaning - Crypto Tweets
#============== import necessary libraries ===================
from numpy import vectorize
import pandas as pd
import os

import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer, PorterStemmer
##Load tweets csv
os.chdir(r'C:\Users\wsalm\OneDrive\Documents\Programming for Data Science\Crypto Project\Crypto-Twitter-Analysis-main')
tweets = pd.read_csv('tweets_data_11.30.csv')
tweets.columns

##Make all text lowercase
tweets['tweet'] = tweets['tweet'].apply(lambda x: " ".join(x.lower() for x in x.split()))

tweets['tweet'][37894]
tweets['tweet'][75]

##Remove @mentions
mention_pattern = '(@[A-Za-z0-9]+)'
tweets['tweet'] = tweets['tweet'].str.replace(mention_pattern,'')
tweets['tweet'][37894]
tweets['tweet'][75]

##Remove Punctuation
punc_pattern = '[^\w\s]'
tweets['tweet'] = tweets['tweet'].str.replace(punc_pattern,'')
tweets['tweet'][37894]
tweets['tweet'][75]

##Remove Numeric Values
digit_pattern = '\\b[0-9]+\\b'
tweets['tweet'] = tweets['tweet'].str.replace(digit_pattern,'')
tweets['tweet'][37894]
tweets['tweet'][75]

##Remove the links 
link_pattern = '\\b[https][a-z0-9]+'
tweets['tweet'] = tweets['tweet'].str.replace(link_pattern,'')
tweets['tweet'][37894]
tweets['tweet'][75]

#Remove stop words using stop_words dataset in nlkt library
stop = stopwords.words('english')
tweets['tweet'] = tweets['tweet'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
tweets['tweet'][37894]
tweets['tweet'][75]

##Remove unneeded whitespace
space_pattern = '(\w+:\/\/\S+)'
tweets['tweet'] = tweets['tweet'].str.replace(space_pattern,'')
tweets['tweet'][37894]
tweets['tweet'][75]

##Stem the words
porstem = PorterStemmer()
tweets['tweet'] = tweets['tweet'].apply(lambda x: " ".join([porstem.stem(word) for word in x.split()]))
tweets['tweet'][37894]
tweets['tweet'][75]

##Topic Modeling 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, plot_confusion_matrix

#Using Latent Dirichlet allocation (LDA) to create 5 topics#
vectorizer = CountVectorizer(max_df=0.8, min_df=4, stop_words='english')

doc_term_matrix = vectorizer.fit_transform(tweets['tweet'].values.astype('U'))

LDA = LatentDirichletAllocation(n_components=5, random_state=35)
LDA.fit(doc_term_matrix)

first_topic = LDA.components_[0]
top_topic_words = first_topic.argsort()[-10:]

for i in top_topic_words:
    print(vectorizer.get_feature_names()[i])

for i,topic in enumerate(LDA.components_):
    print(f'Top 10 words for topic #{i}:')
    print([vectorizer.get_feature_names()[i] for i in topic.argsort()[-10:]])
    print('\n')
#Add a new column to your dataframe containing the LDA topic number#
topic_values = LDA.transform(doc_term_matrix)

topic_values.shape

tweets['LDA topic'] = topic_values.argmax(axis=1)

tweets.head()

#Generate 5 topics using Non-Negative Matrix Factorization (NMF)#
tfidf_vect = TfidfVectorizer(max_df=0.8, min_df=5, stop_words='english')

doc_term_matrix2 = tfidf_vect.fit_transform(tweets['tweet'].values.astype('U'))

nmf = NMF(n_components=5, random_state=42)
nmf.fit(doc_term_matrix2)

first_topic = nmf.components_[0]
top_topic_words = first_topic.argsort()[-10:]

for i in top_topic_words:
    print(tfidf_vect.get_feature_names()[i])

for i,topic in enumerate(nmf.components_):
    print(f'Top 10 words for topic #{i}:')
    print([tfidf_vect.get_feature_names()[i] for i in topic.argsort()[-10:]])
    print('\n')

#Add a new column to your dataframe for the NMF topic number#
topic_values2 = nmf.transform(doc_term_matrix2)

tweets['NMF topic'] = topic_values2.argmax(axis=1)

tweets.head()

##Export cleaned dataset to csv
df = pd.DataFrame(tweets)
tweets.to_csv('tweets_topic_modeling.csv')