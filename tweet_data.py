#=========== Preparing the tweet data ===================
# Merging tweet csv files,
#  removing unneeded columns, 
# and creating calculated column
#========================================================
##Import needed libraries
import pandas as pd
##Read in each _tweets.csv file
bitcoin = pd.read_csv('bitcoin_hashtag_tweets.csv')
crypto = pd.read_csv('crypto_hashtag_tweets.csv')
cryptocom = pd.read_csv('cryptocom_tweets.csv')
doge = pd.read_csv('dogecoin_hastag_tweets.csv')
elon = pd.read_csv('elon_tweets.csv')
##Combine _tweets dataframes using concat
bitcoin.shape
crypto.shape
cryptocom.shape
doge.shape
elon.shape
tweets_data =  pd.concat([bitcoin, crypto, cryptocom, doge, elon])
tweets_data.shape
##Remove duplicate records
tweets_data.drop_duplicates()
##Remove tweets not in English
tweets_data = tweets_data[tweets_data['language']=='en']
##Remove unneeded columns
tweets_data.columns
tweets_data = tweets_data.drop(columns=['id', 'conversation_id', 'created_at', 'time', 'timezone', 'user_id', 'name', 
'place', 'language', 'mentions', 'urls', 'photos', 'link', 'retweet', 'quote_url', 'video', 'thumbnail', 'near', 
'geo', 'source', 'user_rt_id', 'user_rt', 'retweet_id', 'reply_to', 'retweet_date', 'translate', 'trans_src', 'trans_dest'])
tweets_data.columns
##Create interactions column by adding replies, retweets, and likes counts
interactions = tweets_data['replies_count'] + tweets_data['retweets_count'] + tweets_data['likes_count']
tweets_data['interactions'] = interactions
###Remove individual count columns
tweets_data = tweets_data.drop(columns=['replies_count', 'retweets_count', 'likes_count'])
tweets_data.columns
##Ensure dtype is correct for all variables
tweets_data.date
##Change date from string to datetime data type
tweets_data['date'] = pd.to_datetime(tweets_data['date'])
##Export final dataframe to csv
tweets_data.to_csv('tweets_data_11.30.csv')