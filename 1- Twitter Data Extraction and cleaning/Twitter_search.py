import tweepy
import csv
import twitterConst as twitterConst
import re
import os
from pymongo import MongoClient

def main():
    tweets_count = 0
    quoted_tweets_count = 0
    retweeted_tweets_count = 0
    
    client = MongoClient("mongodb+srv://samkit:umjtCNkj65nVUct9@cluster0.vbtql.mongodb.net/RawDb?retryWrites=true&w=majority")
    db = client.RawDb

    # authenticating user's identity
    auth = tweepy.OAuthHandler(twitterConst.T_CONSUMER_API_KEY, twitterConst.T_CONSUMER_API_SECRET_KEY)

    # assign access token
    auth.set_access_token(twitterConst.T_ACCESS_TOKEN, twitterConst.T_ACCESS_TOKEN_SECRET)

    # set variable to use tweepy
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # Creating a search query for search data based on keywords 
    try:
        OR = ' ' + 'OR' + ' '
        query = OR.join(twitterConst.T_SEARCH_KEYWORDS)
    except:
        print("Error while composing twitter search keywords query")

    print("Constructed search query: " + query)

    tweets = tweepy.Cursor(api.search, q=query).items(2000)
    for index, tweet in enumerate(tweets, start=1):
        try:
            
            # Retweets
            if hasattr(tweet, twitterConst.T_RETWEETED_STATUS):
                tweet_row = compose_tweet_row(tweet, twitterConst.RETWEET)
                
                tweetId = db.tweets.insert_one(tweet_row).inserted_id
                # print('Inserted TweetId:' + tweetId)
                
                print(tweet_row['Content'])
                retweeted_tweets_count = retweeted_tweets_count + 1

            # Quoted tweets
            elif hasattr(tweet, twitterConst.T_QUOTED_STATUS):
                tweet_row = compose_tweet_row(tweet, twitterConst.QUOTED_TWEET)
                                
                tweetId = db.tweets.insert_one(tweet_row).inserted_id
                # print('Inserted TweetId:' + tweetId)
                

                print(tweet_row['Content'])
                quoted_tweets_count = quoted_tweets_count + 1

            # Extended Tweets
            elif hasattr(tweet, twitterConst.E_T_TRUNCATED):
                tweet_row = compose_tweet_row(tweet, twitterConst.EXTENDED_TWEET)
                                
                tweetId = db.tweets.insert_one(tweet_row).inserted_id
                # print('Inserted TweetId:' + tweetId)
                

                print(tweet_row['Content'])
                tweets_count = tweets_count + 1

            # All other tweets except retweets or quoted tweets
            else:
                tweet_row = compose_tweet_row(tweet, twitterConst.TWEET)
                                
                tweetId = db.tweets.insert_one(tweet_row).inserted_id
                # print('Inserted TweetId:' + tweetId)
                

                print(tweet_row['Content'])
                tweets_count = tweets_count + 1
        except Exception:
            pass

    print("Total number of Retweets:", retweeted_tweets_count)
    print("Total number of Quoted Tweets:", quoted_tweets_count)
    print("All other Tweets:", tweets_count)

# This method is responsible to create an row (metadata) of tweet
def compose_tweet_row(tweet, tweet_type):
    try:
        tweet_row = {}

        # Normal Tweet Attributes
        tweet_row['Timestamp'] = tweet.created_at
        tweet_row['ID'] = tweet.id
        tweet_row['Content'] = tweet.text
        tweet_row['Username'] = tweet.user.name
        tweet_row['User ScreenName'] = tweet.user.screen_name
        tweet_row['User Location'] = tweet.user.location

        # Extended Tweet Attributes
        tweet_row['Truncated'] = tweet.truncated if hasattr(tweet, 'Truncated') else ''
        tweet_row['Extended Tweet'] = tweet.extended_tweet.full_text if hasattr(tweet, 'Truncated') else ''

        # Retweet Attributes
        if tweet_type == twitterConst.RETWEET:
            tweet_row['Timestamp - Original Tweet'] = tweet.retweeted_status.created_at
            tweet_row['ID - Original Tweet'] = tweet.retweeted_status.id
            tweet_row['Content - Original Tweet'] = tweet.retweeted_status.text
            tweet_row['Username - Original Tweet'] = tweet.retweeted_status.user.name
            tweet_row['User ScreenName - Original Tweet'] = tweet.retweeted_status.user.screen_name
            tweet_row['User Location - Original Tweet'] = tweet.retweeted_status.user.location

        # Quoted Tweet Attributes
        if tweet_type == twitterConst.QUOTED_TWEET:
            tweet_row['Timestamp - Original Tweet'] = tweet.quoted_status.created_at
            tweet_row['ID - Original Tweet'] = tweet.quoted_status.id
            tweet_row['Content - Original Tweet'] = tweet.quoted_status.text
            tweet_row['Username - Original Tweet'] = tweet.quoted_status.user.name
            tweet_row['User ScreenName - Original Tweet'] = tweet.quoted_status.user.screen_name
            tweet_row['User Location - Original Tweet'] = tweet.quoted_status.user.location

    except:
        print("Error while composing the individual tweet row for CSV file")

    return tweet_row    

if __name__ == "__main__":
    main()
