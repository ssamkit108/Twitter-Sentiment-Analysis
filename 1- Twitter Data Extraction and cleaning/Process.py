import os
import re
from pymongo import MongoClient

def main():
    client = MongoClient("mongodb+srv://samkit:umjtCNkj65nVUct9@cluster0.vbtql.mongodb.net/RawDb?retryWrites=true&w=majority")
    db_raw = client.RawDb
    db_processed = client.ProcessedDb

    data = db_raw.tweets

    tweetlist= data.find()
    for tweet_row in tweetlist:
        try:
            tweet_row['Content'] = clean(tweet_row['Content'])
            tweet_row['Username'] = clean(tweet_row['Username'])
            tweet_row['User ScreenName'] = clean(tweet_row['User ScreenName'])
            tweet_row['User Location'] = clean(tweet_row['User Location'])
            if "Content - Original Tweet" in tweet_row:
                tweet_row['Content - Original Tweet'] = clean(tweet_row['Content - Original Tweet'])
            if "Username - Original Tweet" in tweet_row:
                tweet_row['Username - Original Tweet'] = clean(tweet_row['Username - Original Tweet'])
            if "User ScreenName - Original Tweet" in tweet_row:
                tweet_row['User ScreenName - Original Tweet'] = clean(tweet_row['User ScreenName - Original Tweet'])
            if "User Location - Original Tweet" in tweet_row:
                tweet_row['User Location - Original Tweet'] = clean(tweet_row['User Location - Original Tweet'])
            
            tweetId =db_processed.tweets.insert_one(tweet_row).inserted_id

            print("Tweet:")
            print(tweet_row)
            
        except Exception:
            print("Exception generated")
            pass
        

def clean(text):
    try:
        text = re.sub(r"http\S+", '', text)

        text = re.sub(r'\\u[A-Za-z0-9]{4}', '', text)

        text = re.sub(r'&amp;', '&', text)

        text = re.sub(r"[^a-zA-Z0-9@',.:\$& ]+", '', text)

        text = re.sub(r'\\n', ' ', text)

        text = re.sub(r'\s+', ' ',text)
    except:
        pass
    return text

if __name__ == "__main__":
    main()