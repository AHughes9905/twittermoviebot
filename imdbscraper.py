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


def get250MovieURL(n):
    html = get_top_250_html()
    soup = bs(html, "lxml")

    atag = soup.find_all('div', class_ = "ipc-metadata-list-summary-item__c")[n].find('a')
    movie_page = atag['href']
    movie_url = "https://www.imdb.com" + movie_page
    return movie_url

def getReviewsandInfo(url):
    soup = soupify(url)

    dropdown_pref = '/reviews/?ref_=tt_ov_ururv&sort=user_rating%2Casc'
    title_ref = url.split('/')[4]
    review_url = "https://www.imdb.com/title/" + title_ref + dropdown_pref

    info = movieInfo(soup)
    return review_url, info


def getRandomReviewPage(url):
    soup = soupify(url)
    reviews = soup.find_all('article', class_ = lambda t: t and 'user-review-item' in t)
    n = random.randrange(0, len(reviews))
    review_url = reviews[n].find('a', class_ = 'ipc-title-link-wrapper')['href']
    url = 'https://www.imdb.com' + review_url + '?ref_=tt_urv'
    return url

def getReviewFromPage(url):
    soup = soupify(url)
    return soup.find(class_ = 'ipc-html-content-inner-div').text

def getMoviePageSoup(n):
    
    html = get_top_250_html()
    soup = bs(html, "lxml")

    atag = soup.find_all('div', class_ = "ipc-metadata-list-summary-item__c")[n].find('a')
    movie_page = atag['href']
    movie_url = "https://www.imdb.com" + movie_page
    return soupify(movie_url)



def movieInfo(msoup):
    movieinfo = {'name': '' , 'rating': '', 'ranking': 'NA', 'review': '', 'user_rating': ''}

    movieinfo['name'] = msoup.find('h1').string
    movieinfo['rating'] = msoup.find(class_ = 'sc-d541859f-1 imUuxf').string
    top_rated = msoup.find('a', class_ = 'ipc-link ipc-link--base ipc-link--inherit-color top-rated-link')
    if top_rated:
        movieinfo['ranking'] = top_rated.string.split('#')[1]

    return movieinfo

