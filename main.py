import os

import tweepy
import tweepy as tw
import pandas as pd
import urllib
import json
import keys



auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)

number_of_tweets = 200
tweets = []
likes = []
time = []

for i in tweepy.Cursor(api.user_timeline, id="murraiscanlon", tweet_mode="extended").items(number_of_tweets):
    tweets.append(i.full_text)
    likes.append(i.favorite_count)
    time.append(i.created_at)

df = pd.DataFrame({'tweets':tweets, 'likes':likes, 'time':time})
print(df)
# cursor = tweepy.Cursor(api.search, q='flu',tweet_mode="extended").items(1)
# for i in cursor:
#     # print(dir(i))
#     print(i.full_text)







