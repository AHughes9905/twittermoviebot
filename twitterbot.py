import tweepy


def setupAPI():
    f = open("apicodes.txt", 'r')
    keys = f.readlines()
    keys = [key.strip() for key in keys]
    consumer = keys[0]
    consumer_secret = keys[1]
    access = keys[2]
    access_secret = keys[3]
    f.close()
    
    auth = tweepy.OAuthHandler(consumer, consumer_secret)
    auth.set_access_token(access, access_secret,)

    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

def setupClient():
    f = open("apicodes.txt", 'r')
    keys = f.readlines()
    keys = [key.strip() for key in keys]
    consumer = keys[0]
    consumer_secret = keys[1]
    access = keys[2]
    access_secret = keys[3]
    f.close()

    client = tweepy.Client(consumer_key = consumer, consumer_secret=consumer_secret, access_token=access, access_token_secret=access_secret)
    return client

def makeTweet(client, message):
    return client.create_tweet(text=message)

def replyTweet(client, message, tweet_id):
    return client.create_tweet(text=message, in_reply_to_tweet_id=tweet_id)


def getRecentTweetId(api):
    tweet_ids = []
    timeline = api.user_timeline(user_id = 'HotMovieTakes_')

    for tweet in timeline:
        tweet_ids.append(tweet.id)

    return tweet_ids[0]


def tweetList(api, tweet_list):
    c = 0
    current_id = ''
    for tweet in tweet_list:
        if c < 0:

            makeTweet(api, tweet)
            c += 1
            current_id = getRecentTweetId(api)
        else:
            replyTweet(api, tweet, current_id)
            current_id = getRecentTweetId(api)

def tweetList2(client, tweet_list):
    c = 0
    current_id = ''
    for tweet in tweet_list:
        if c == 0:

            response = makeTweet(client, tweet)
            current_id = response.data['id']
            c += 1

        else:
            response = replyTweet(client, tweet, current_id)
            current_id = response.data['id']
