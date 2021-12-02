import pandas as pd
import numpy as np
import os
import requests
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')


from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags

df = pd.read_excel('C:\\Users\\johnm\OneDrive\\Documents\\GitHub\\Crypto-Twitter-Analysis\\tweets_data_11.30.xlsx')

# print(df)

df = pd.DataFrame(df)


df['tweet']= df['tweet'].astype('string')
print(df.dtypes)


###Tokenize
post1 = pos_tag(word_tokenize(df['tweet']))
print(post1)

tree1 = ne_chunk(post1)
print(tree1)

entityp = []
entityo = []
entityg = []
entitydesc = []

for x in str(tree1).split('\n'):
    if 'PERSON' in x:
        entityp.append(x)
    elif 'ORGANIZATION' in x:
        entityo.append(x)
    elif 'GPE' in x or 'GSP' in x:
        entityg.append(x)
    elif '/NN' in x:
        entitydesc.append(x)

entityp
entityo
entityg
entitydesc

iob_tag = tree2conlltags(tree1)
for i in iob_tag: print(i)

tree1['NN'] = ''
tree1['JJ'] = ''
tree1['VB'] = ''
tree1['GEO'] = ''

def tweet_ner(chunker):
    treestruct = ne_chunk(pos_tag(word_tokenize(chunker)))
    entitynn = []
    entityjj = []
    entityg_air = []
    entityvb = []
    for y in str(treestruct).split('\n'):
        if 'GPE' in y or 'GSP' in y:
            entityg_air.append(y)
        elif '/VB' in y:
            entityvb.append(y)
        elif '/NN' in y:
            entitynn.append(y)
        elif '/JJ' in y:
            entityjj.append(y)
    stringnn = ''.join(entitynn)
    stringjj = ''.join(entityjj)
    stringvb = ''.join(entityvb)
    stringg = ''.join(entityg_air)
    return stringnn, stringjj, stringvb, stringg


