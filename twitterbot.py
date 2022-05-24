import tweepy


def setupAPI():
    #logs into the twitter api using keys from a text file. returns the api object
    f = open("apicodes.txt", 'r')
    keys = f.readlines()
    keys = [key.strip() for key in keys]
    f.close()

    auth = tweepy.OAuthHandler(keys[0], keys[1])
    auth.set_access_token(keys[2], keys[3])

    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

def makeTweet(api, message):
    #takes in api object and string to tweet the string
    api.update_status(message)

def replyTweet(api, message, tweet_id):
    #uses api object, string, and a tweet id to reply to a tweet
    api.update_status(message, in_reply_to_status_id = tweet_id)


def getRecentTweetId(api):
    #takes in api opject and returns the tweet id of the most recent tweet in the accounts' timeline
    tweet_ids = []
    timeline = api.user_timeline(user_id = 'HotMovieTakes_')

    for tweet in timeline:
        tweet_ids.append(tweet.id)

    return tweet_ids[0]


def tweetList(api, tweet_list):
    #takes in api object, and list containing messages to be tweeted in a chain.
    #it tweets the first element of the list normally. afterwards it replies to the previous tweet, creating a thread
    c = 0
    current_id = ''
    for tweet in tweet_list:
        if c < 0:

            makeTweet(api, tweet)
            c = 1
            current_id = getRecentTweetId(api)
        else:
            replyTweet(api, tweet, current_id)
            current_id = getRecentTweetId(api)
