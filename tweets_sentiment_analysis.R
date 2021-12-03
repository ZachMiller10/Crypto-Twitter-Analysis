library(tidyverse)
library(tidytext)
library(SnowballC)
library(wordcloud)
library(udpipe)
library(lattice)
library(textdata)
library(reshape2)
library(wordcloud)
library(udpipe)
library(lattice)

wd = "C:\\Users\\wsalm\\OneDrive\\Documents\\Programming for Data Science\\Crypto Project\\Crypto-Twitter-Analysis-main"
setwd(wd)

table = paste(wd, "\\tweets_topic_modeling.csv", sep = "")
tweets_data = read.csv(table, header = TRUE)
summary(tweets_data)

tweets = select(tweets_data, tweet)
tweet_dataset = unnest_tokens(tweets, word, tweet)

#Sentiment Analysis#
get_sentiments('bing') %>%
  distinct(sentiment)

get_sentiments('nrc') %>%
  distinct(sentiment)

#Generate a new variable assessing the difference between joy and sadness.#
newjoin = inner_join(tweet_dataset, get_sentiments('bing'))
counts = count(newjoin, sentiment)
spread1 = spread(counts, sentiment, n, fill = 0)
(mutate(spread1, diffsent = positive - negative))

nrc_joysad = get_sentiments('nrc') %>%
  filter(sentiment == 'joy' | 
           sentiment == 'sadness')

nrow(nrc_joysad)

newjoin2 = inner_join(tweet_dataset, nrc_joysad)
newjoin2

counts2 = count(newjoin2, word, sentiment)
spread2 = spread(counts2, sentiment, n, fill = 0)
spread2

content_data = mutate(spread2, contentment = joy - sadness, linenumber = row_number())
tweet_joysad = arrange(content_data, desc(contentment))
tweet_joysad

#Plot for the top 20 values for joy and sadness.#
(tweet_joysad2 = tweet_joysad %>%
    slice(1:10,368:377))

ggplot(tweet_joysad2, aes(x=linenumber, y=contentment, fill=word)) +
  coord_flip() +
  theme_light(base_size = 15) +
  labs(
    x='Index Value',
    y='Contentment'
  ) +
  theme(
    legend.position = 'bottom',
    panel.grid = element_blank(),
    axis.title = element_text(size = 10),
    axis.text.x = element_text(size = 10),
    axis.text.y = element_text(size = 10)
  ) +
  geom_col()

#Generate a new variable assessing the difference between positive and negative.#
nrc_posneg = get_sentiments('nrc') %>%
  filter(sentiment == 'positive' |
           sentiment == 'negative')

nrow(nrc_posneg)

newjoin3 = inner_join(tweet_dataset, nrc_posneg)
newjoin3

counts3 = count(newjoin3, word, sentiment)
spread3 = spread(counts3, sentiment, n, fill = 0)
spread3

posneg_data = mutate(spread3, positivity = positive - negative, linenumber = row_number())
tweet_posneg = arrange(posneg_data, desc(positivity))
tweet_posneg

#Plot the top 20 values for positive and negative.#
(tweet_posneg3 = tweet_posneg %>%
    slice(1:10,1137:1146))

ggplot(tweet_posneg3, aes(x=linenumber, y=positivity, fill=word)) +
  coord_flip() +
  theme_light(base_size = 15) +
  labs(
    x='Index Value',
    y='Contentment'
  ) +
  theme(
    legend.position = 'bottom',
    panel.grid = element_blank(),
    axis.title = element_text(size = 10),
    axis.text.x = element_text(size = 10),
    axis.text.y = element_text(size = 10)
  ) +
  geom_col()