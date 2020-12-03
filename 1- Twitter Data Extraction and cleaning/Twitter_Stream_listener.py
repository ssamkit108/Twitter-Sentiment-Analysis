import tweepy
import csv
import sys
import json
import twitterConst as twitterConst
import re
from pymongo import MongoClient


class TwitterStreamListener(tweepy.streaming.StreamListener):
    tweetCounter = 0

    def compose_streaming_tweet_row(self,tweet, tweet_type):
        
        tweet_row = {}
        tweet_row['Timestamp'] = tweet["created_at"]
        tweet_row['ID'] = tweet["id"]
        tweet_row['Content'] = tweet["text"]
        tweet_row['Username'] = tweet["user"]["name"]
        tweet_row['User ScreenName'] = tweet["user"]["screen_name"]
        tweet_row['User Location'] = tweet["user"]["location"]

        # Extended Tweet Attributes
        tweet_row['Truncated'] = tweet["truncated"] if hasattr(tweet, 'Truncated') else ''
        tweet_row['Extended Tweet'] = tweet["extended_tweet"]['full_text'] if hasattr(tweet, 'Truncated') else ''

        return tweet_row

    def on_data(self, data):            
        client = MongoClient("mongodb+srv://samkit:umjtCNkj65nVUct9@cluster0.vbtql.mongodb.net/RawDb?retryWrites=true&w=majority")
        db = client.RawDb            

        # print(data)

        tweet = json.loads(data)
        # print(tweet)
        # print(tweet["created_at"])
        tweet_row = self.compose_streaming_tweet_row(tweet, 'Tweet')
        tweetId = db.tweets.insert_one(tweet_row).inserted_id
        print(tweet_row)
            
        # print(tweet_row[twitterConst.S_TEXT])
        TwitterStreamListener.tweetCounter += 1

        if TwitterStreamListener.tweetCounter == twitterConst.NO_OF_TWEETS_STREAM:
            sys.exit()
        else:
            pass
        
    def on_error(self, error):
        print(error)
        
