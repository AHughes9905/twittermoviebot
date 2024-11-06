import tweepy


def setupAPI():
    f = open("apicodes.txt", 'r')
    keys = f.readlines()
    keys = [key.strip() for key in keys]
    f.close()

    auth = tweepy.OAuthHandler(keys[0], keys[1])
    auth.set_access_token(keys[2], keys[3])

    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

def makeTweet(api, message):
    api.update_status(message)

def replyTweet(api, message, tweet_id):
    api.update_status(message, in_reply_to_status_id = tweet_id)


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
