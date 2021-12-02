#Data Cleaning - Crypto Tweets
#============== import necessary libraries ===================
from numpy import vectorize
import pandas as pd

import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
##Load tweets csv
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

##Export cleaned dataset to csv
tweets.to_csv('tweets_clean.csv')