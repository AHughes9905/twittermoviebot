from imdbscraper import *
from twitterbot import *
import random



def chooseMovieForReview():
    #asks user through console whether to get a review from a specific or random  movie in the IMDb top 250 and returns its ranking
    print("Would you like to manually or randomly choose a movie? \n")
    inp = input("m or r? ")
    if inp == 'm':
        print("Choose a movie in the top 250. ")
        inp = input("Choose 1 through 250 ")
        movie_number = int(inp) - 1
    elif inp == 'r':
        movie_number = random.randint(0, 249)
    return movie_number


def splitBadReview2(bad_review):
    #this takes in a string and seperates it into a list, seperating at the nearest space to the 270 characters.
    #this is because the max tweet length is 280 characters, so it divides long reviews into multiple tweets if necessary
    #if the bad review is longer than 1 tweet, the function adds a fraction to the end of the tweets indicating how long the thread is
    split_up_tweet = []
    while len(bad_review) > 0:
        if len(bad_review) > 270:
            cutoff = bad_review.rfind(' ', 0, 270)
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
            split_up_tweet[i] = split_up_tweet[i] + ending

    return split_up_tweet

def splitBadReview(bad_review):
    #outdated function used to split up long reviews into a list
    split_up_tweet = []
    counter = 1
    for i in range(len(bad_review)//270):
        tweet_section = bad_review[(270*(counter-1)):(270*counter)] + f' ({counter}/{range(len(bad_review)//270)[-1]+1})'
        split_up_tweet.append(tweet_section)
        counter += 1
    return split_up_tweet

def checkTweet(movie_info, bad_review):
    name = movie_info['name']
    rating = movie_info['rating']
    new_tweet = f'''{name}, {rating}/10
    \"{bad_review}\"'''
    if len(new_tweet) <= 270:
        print(new_tweet)
        inp = input("The tweet is less than 280 characters, would you like use this tweet? (Y/N) ")
        if inp == 'y' or inp == 'Y':
            return [new_tweet]
        else:
            return False
            checkTweet(movie_info, bad_review)
    else:
        new_tweet = splitBadReview2(new_tweet)
        print(new_tweet)
        inp = input("The tweet is longer than 280 characters, would you like use this tweet? (Y/N) ")
        if inp == 'y' or inp == 'Y':
            return new_tweet
        else:
            return False
            checkTweet(movie_info, bad_review)



def main():
    n = chooseMovieForReview()
    movie_page_soup = getMoviePageSoup(n)
    movie_info = movieInfo(movie_page_soup)
    review_page_soup = getReviewPage(movie_page_soup)
    bad_review_page_soup = specificReviewPage(review_page_soup)
    bad_review = reviewFromSpecificPage(bad_review_page_soup)
    tweet = checkTweet(movie_info, bad_review)



    api = setupAPI()
    tweetList(api, tweet)

main()
