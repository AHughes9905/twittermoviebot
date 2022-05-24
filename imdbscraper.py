import requests
from bs4 import BeautifulSoup as bs
import csv
import random


def soupify(url):
    #takes in a url and returns a beautiful soup object
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    return soup


def getMoviePageSoup(n):
    #takes number 1-250 and returns beautiful soup object of its specific page
    url = 'https://www.imdb.com/chart/top/'
    soup = soupify(url)

    body = soup.tbody
    atag = body.find_all('tr')[n].findAll('a')
    movie_page = atag[-1]['href']
    movie_url = "https://www.imdb.com" + movie_page
    return soupify(movie_url)



def movieInfo(msoup):
    #takes movie page soup object abd returns a list containing basic information about the movie
    movieinfo = {'name': '' , 'rating': '', 'ranking': '', 'review': '', 'user_rating': ''}

    movieinfo['name'] = msoup.find('h1').string
    movieinfo['rating'] = msoup.find(class_ = 'sc-7ab21ed2-1 jGRxWM').string
    movieinfo['ranking'] = msoup.find(class_ = 'sc-edc76a2-2 geydkP').text

    return movieinfo

def getReviewPage(msoup):
    #uses movie page soup object to go to the negative review page for the movie
    dropdown_pref = '?sort=userRating&dir=asc&ratingFilter=0'
    thingy = msoup.find_all('a', class_ = 'ipc-title ipc-title--section-title ipc-title--base ipc-title--on-textPrimary ipc-title-link-wrapper')[2]['href']
    review_page = "https://www.imdb.com" + thingy.split('?')[0] + dropdown_pref
    return soupify(review_page)

def specificReviewPage(csoup):
    #this chooses a random review on the movie review page and returns the soup object for just the review page
    #this is done because reviews may be shortened on the page containing all reviews for the movie
    n = random.randrange(0,80, 4)
    review_url = csoup.find(class_ = 'lister-list').findAll('a')[n]['href']

    url = 'https://www.imdb.com' + review_url + '?ref_=tt_urv'
    return soupify(url)

def reviewFromSpecificPage(ssoup):
    #this returns a string of the negative review from the review page
    return ssoup.find(class_ = 'content').find(class_ = 'text show-more__control').text

