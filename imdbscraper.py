import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
import csv
import random
from pw_scrape import *
from playwright.sync_api import sync_playwright as p


def soupify(url):
    webpage = requests.get(url , headers={'User-Agent': 'Mozilla/5.0'})
    return bs(webpage.content, "lxml")


def getMoviePageSoup(n):
    
    html = get_top_250_html()
    soup = bs(html, "lxml")

    print(n)
    atag = soup.find_all('div', class_ = "ipc-metadata-list-summary-item__c")[n].find('a')
    movie_page = atag['href']
    movie_url = "https://www.imdb.com" + movie_page
    return soupify(movie_url)



def movieInfo(msoup, n):
    movieinfo = {'name': '' , 'rating': '', 'ranking': '', 'review': '', 'user_rating': ''}

    movieinfo['name'] = msoup.find('h1').string
    movieinfo['rating'] = msoup.find(class_ = 'sc-d541859f-1 imUuxf').string
    movieinfo['ranking'] = str(n+1)

    return movieinfo

def getReviewPage(msoup):
    dropdown_pref = '&sort=user_rating%2Casc'
    directory = msoup.find('a', class_ = 'ipc-link ipc-link--baseAlt ipc-link--touch-target sc-b782214c-2 kqhWjl isReview')['href']
    review_page = "https://www.imdb.com" + directory.split('?')[0] + dropdown_pref
    return soupify(review_page)

def specificReviewPage(csoup):
    n = random.randrange(0,80, 4)
    review_url = csoup.find(class_ = 'lister-list').findAll('a')[n]['href']

    url = 'https://www.imdb.com' + review_url + '?ref_=tt_urv'
    return soupify(url)

def reviewFromSpecificPage(ssoup):
    return ssoup.find(class_ = 'content').find(class_ = 'text show-more__control').text


def getBadReview(csoup):
    n = random.randrange(0,20)
    bad_review = csoup.find(class_ = 'lister-list').find_all(class_ = 'text show-more__control')[n].text
    #user_rating = csoup.find(class_ = 'ipl-icon ipl-star-icon').find('span').text
    return bad_review
