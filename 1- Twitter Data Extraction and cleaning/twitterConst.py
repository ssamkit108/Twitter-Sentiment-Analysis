# constants to work with twitter developer api
# credentials to access twitter API
T_CONSUMER_API_KEY = '7zi90AhjTpw87VoJ640jvt2eP'
T_CONSUMER_API_SECRET_KEY = '3WQAKOvqpan9HdwUz8FHRYCb86lLSdUluuxUd2ijnyduB6Dpqd'
T_ACCESS_TOKEN = '766466154894327809-97vuqWzx1PK3zKnkgODimmCBJC1cHwB'
T_ACCESS_TOKEN_SECRET = 'awqOTzEyGz98jtPn7qVsRlHq3hNMBZs4dmv7M4nzNViaG'

host = 'cluster0-shard-00-01.vbtql.mongodb.net'
port = 27017
username = 'samkit'
password = 'umjtCNkj65nVUct9'
database = 'RawDb'

# search Keywords
T_SEARCH_KEYWORDS = ['Storm', 'Winter', 'Canada', 'Temperature', 'Flu','Snow','Indoor','Safety']

# no of tweets
NO_OF_TWEETS_SEARCH = 2000
NO_OF_TWEETS_STREAM = 1000

# tweet types
TWEET = 'Tweet'
EXTENDED_TWEET = 'EXTENDED_TWEET'
RETWEET = 'RETWEET'
QUOTED_TWEET = 'QUOTED_TWEET'

# tweet obeject fields
T_CREATED_AT = 'Timestamp'
T_TWEET_ID = 'ID'
T_TEXT = 'Content'
T_USER_NAME = 'Username'
T_USER_SCREEN_NAME = 'User ScreenName'
T_USER_LOCATION = 'User Location'
T_TRUNCATED = 'Truncated'
T_EXTENDED_TWEET = 'Extended Tweet'
O_T_CREATED_AT = 'Timestamp - Original Tweet'
O_T_TWEET_ID = 'ID - Original Tweet'
O_T_TEXT = 'Content - Original Tweet'
O_T_USER_NAME = 'Username - Original Tweet'
O_T_USER_SCREEN_NAME = 'User ScreenName - Original Tweet'
O_T_USER_LOCATION = 'User Location - Original Tweet'

# twitter dataset field names
T_FIELDNAMES = [T_CREATED_AT, T_TWEET_ID, T_TEXT, T_USER_NAME, T_USER_SCREEN_NAME, T_USER_LOCATION, T_TRUNCATED, T_EXTENDED_TWEET,O_T_CREATED_AT, O_T_TWEET_ID, O_T_TEXT, O_T_USER_NAME, O_T_USER_SCREEN_NAME, O_T_USER_LOCATION]

T_RETWEETED_STATUS = 'retweeted_status'
T_QUOTED_STATUS = 'quoted_status'
E_T_TRUNCATED = 'truncated'
S_CREATED_AT = 'created_at'
S_TWEET_ID = 'id'
S_TEXT = 'text'
S_USER = 'user'
S_USER_NAME = 'name'
S_USER_SCREEN_NAME = 'screen_name'
S_USER_LOCATION = 'location'

T_TRUNCATED = 'Truncated'
T_EXTENDED_TWEET = 'Extended Tweet'

S_T_RETWEETED = 'retweeted_status'
S_T_CREATED_AT = 'created_at'
S_T_TWEET_ID = 'id'
S_T_TEXT = 'text'
S_T_USER = 'user'
S_T_USER_NAME = 'name'
S_T_USER_SCREEN_NAME = 'screen_name'
S_T_USER_LOCATION = 'location'