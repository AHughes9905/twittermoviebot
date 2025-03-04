from imdbscraper import *
from twitterbot import *
from savejson import *
import random
import sys



def chooseMovieForReview():
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
        header = f'''{name}, {rating}/10, #{ranking}/250\n'''
    new_tweet = f'''{header}\"{bad_review}\"'''

    if len(new_tweet) <= 270:
        return [new_tweet]
    else:
        new_tweet = splitBadReview(new_tweet)
        return new_tweet



def main():
    if len(sys.argv) > 1:
        review_url = sys.argv[1]
    else: 
        for i in range(100):
            n = chooseMovieForReview()
            movie_url = get250MovieURL(n)
            bad_reviews_url, movie_info = getReviewsandInfo(movie_url)
            review_url = getRandomReviewPage(bad_reviews_url)
            if checkNewReview(review_url) and not inRecentMovies(review_url):
                break
    bad_review = getReviewFromPage(review_url)
    tweet = checkTweet(movie_info, bad_review)
    client = setupClient()
    tweetList(client, tweet)
    updateRecentMovies(movie_url)
    addReview(review_url,movie_url)

def test():
    for i in range(100):

        n = chooseMovieForReview()
        movie_url = get250MovieURL(n)
        bad_reviews_url, movie_info = getReviewsandInfo(movie_url)
        review_url = getRandomReviewPage(bad_reviews_url)
        if checkNewReview:
            break
    bad_review = getReviewFromPage(review_url)
    tweet = checkTweet(movie_info, bad_review)
    addReview(review_url,movie_url)
    updateRecentMovies(movie_url)
    if not inRecentMovies(movie_url):
        updateRecentMovies(movie_url)

main()