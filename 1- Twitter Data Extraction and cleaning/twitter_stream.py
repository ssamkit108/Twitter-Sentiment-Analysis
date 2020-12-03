import twitterConst as twitterConst
import tweepy
import Twitter_Stream_listener as streamListener
import csv
import sys
import json

# authenticating user's identity
auth = tweepy.OAuthHandler(twitterConst.T_CONSUMER_API_KEY, twitterConst.T_CONSUMER_API_SECRET_KEY)

# assign access token
auth.set_access_token(twitterConst.T_ACCESS_TOKEN, twitterConst.T_ACCESS_TOKEN_SECRET)

# instance of TwitterStreamListener
twitterStreamListener = streamListener.TwitterStreamListener()

# assigning listener for the stream of tweets
twitterStream = tweepy.Stream(auth, twitterStreamListener)

# filtering based on the provided list of keywords
twitterStream.filter(track=twitterConst.T_SEARCH_KEYWORDS)