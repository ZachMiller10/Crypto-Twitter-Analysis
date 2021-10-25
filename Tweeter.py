#Twitter Crypto Scrape Using Twint

import twint
import pandas as pd


### Crypto Search
c = twint.Config()
c.Search = ['#crypto']  #topic
c.Limit = 10  #number of tweets to scrape
c.Store_csv = True  #store tweets to csv file
c.Output = "crypto_hashtag_tweets.csv"  #path to csv file
c.Since = "2018-12-31"
c.Until = "2021-12-31"
twint.run.Search(c)


df1 = pd.read_csv('crypto_hashtag_tweets.csv')

###Dogecoin Search
d = twint.Config()
d.Search = ['#dogecoin']  #topic
d.Limit = 1000000   #number of tweets to scrape
d.Store_csv = True  #store tweets to csv file
d.Output = "dogecoin_hastag_tweets.csv"  #path to csv file

twint.run.Search(d)


df2 = pd.read_csv('dogecoin_hastag_tweets.csv')

###Bitcoin search
b = twint.Config()
b.Search = ['#bitcoin']  #topic
b.Limit = 1000000   #number of tweets to scrape
b.Store_csv = True  #store tweets to csv file
b.Output = "bitcoin_hashtag_tweets.csv"  #path to csv file

twint.run.Search(b)


df3 = pd.read_csv('bitcoin_hastag_tweets.csv')