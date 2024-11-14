from imdbscraper import *
from twitterbot import *
import random



def chooseMovieForReview():
    print("Would you like to manually or randomly choose a movie? \n")
    inp = input("m or r? ")
    if inp == 'm':
        print("Choose a movie in the top 250. ")
        inp = input("Choose 1 through 250 ")
        movie_number = int(inp) - 1
    elif inp == 'r':
        movie_number = random.randint(0, 249)
    return movie_number


def splitBadReview(bad_review):
    max_len = 260
    split_up_tweet = []
    
    while len(bad_review) > 0:
        if len(bad_review) > max_len:
            cutoff = bad_review.rfind(' ', 0, max_len)
            section = bad_review[0:cutoff]
            split_up_tweet.append(section)
            bad_review = bad_review[cutoff:]

        else:
            split_up_tweet.append(bad_review)
            bad_review = ''

    tweet_len = len(split_up_tweet)
    if tweet_len > 0:
        for i in range(tweet_len):
            ending = f' ({i+1}/{tweet_len})'
            if i > 0:
                ending += ' @HM_Takes'
            split_up_tweet[i] = split_up_tweet[i] + ending

    return split_up_tweet


def checkTweet(movie_info, bad_review):
    name = movie_info['name']
    rating = movie_info['rating']
    ranking = movie_info['ranking']
    if ranking == 'NA':
        header = f'''{name}, {rating}/10\n'''
    else: 
        header = f'''{name}, {rating}/10, #{ranking}\n'''
    new_tweet = f'''{header}\"{bad_review}\"'''

    if len(new_tweet) <= 270:
        print(new_tweet)
        inp = input("The tweet is less than 280 characters, would you like use this tweet? (Y/N) ")
        if inp == 'y' or inp == 'Y':
            return [new_tweet]
        else:
            return False
            #checkTweet(movie_info, bad_review)
    else:
        new_tweet = splitBadReview(new_tweet)
        print(new_tweet)
        inp = input("The tweet is longer than 280 characters, would you like use this tweet? (Y/N) ")
        if inp == 'y' or inp == 'Y':
            return new_tweet
        else:
            return False
            #checkTweet(movie_info, bad_review)



def main():
    
    n = chooseMovieForReview()
    movie_url = get250MovieURL(n)
    bad_reviews_url, movie_info = getReviewsandInfo(movie_url)
    review_url = getRandomReviewPage(bad_reviews_url)
    bad_review = getReviewFromPage(review_url)
    tweet = checkTweet(movie_info, bad_review)
    client = setupClient()
    tweetList2(client, tweet)
    '''
    movie_page_soup = getMoviePageSoup(n)
    movie_info = movieInfo(movie_page_soup)
    review_page_soup = getReviewPage(movie_page_soup)
    bad_review_page_soup = specificReviewPage(review_page_soup)
    bad_review = reviewFromSpecificPage(bad_review_page_soup)
    tweet = checkTweet(movie_info, bad_review)
    client = setupClient()
    tweetList2(client, tweet)
    q'''

    #client = setupClient()
    #client.create_tweet(text='Test')
    

main()
