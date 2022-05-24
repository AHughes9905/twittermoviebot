import requests
from bs4 import BeautifulSoup as bs
import csv
import random

#baseurl = "https://www.imdb.com"
#url = 'https://www.imdb.com/chart/top/'
#r = requests.get(url)
#ranking = random.randrange(0, 249)

#soup = bs(r.content, 'html.parser')

def soupify(url):
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    return soup

#body = soup.tbody

def getMoviePage(toppage_soup, n):
    body = toppage_soup.tbody
    atag = body.find_all('tr')[n].findAll('a')
    movie_page = atag[-1]['href']
    movie_url = "https://www.imdb.com" + movie_page
    return soupify(movie_url)


def getMoviePageSoup(n):
    url = 'https://www.imdb.com/chart/top/'
    soup = soupify(url)

    body = soup.tbody
    atag = body.find_all('tr')[n].findAll('a')
    movie_page = atag[-1]['href']
    movie_url = "https://www.imdb.com" + movie_page
    return soupify(movie_url)


#def getMovieURL(n):
#atag = body.find_all('tr')[2].findAll('a')

#movie_page = atag[-1]['href']
#movie_url = baseurl + movie_page
#return movie_url
#print(movie_url)



#m = requests.get(movie_url)

#msoup = bs(m.content, 'html.parser')
#print(msoup.prettify())
#print(msoup.find('h1').string)
#print(msoup.find(class_ = 'sc-7ab21ed2-1 jGRxWM').string)
#print(msoup.find_all('a', class_ = 'ipc-title ipc-title--section-title ipc-title--base ipc-title--on-textPrimary ipc-title-link-wrapper')[2]['href'])

#thingy = msoup.find_all('a', class_ = 'ipc-title ipc-title--section-title ipc-title--base ipc-title--on-textPrimary ipc-title-link-wrapper')[2]['href']

#print(thingy.split('?')[0])

#review_page = baseurl + thingy.split('?')[0]

def movieInfo(msoup):
    movieinfo = {'name': '' , 'rating': '', 'ranking': '', 'review': '', 'user_rating': ''}

    movieinfo['name'] = msoup.find('h1').string
    movieinfo['rating'] = msoup.find(class_ = 'sc-7ab21ed2-1 jGRxWM').string
    movieinfo['ranking'] = msoup.find(class_ = 'sc-edc76a2-2 geydkP').text

    return movieinfo

def getReviewPage(msoup):
    dropdown_pref = '?sort=userRating&dir=asc&ratingFilter=0'
    thingy = msoup.find_all('a', class_ = 'ipc-title ipc-title--section-title ipc-title--base ipc-title--on-textPrimary ipc-title-link-wrapper')[2]['href']
    review_page = "https://www.imdb.com" + thingy.split('?')[0] + dropdown_pref
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



def randomMovieReview():
    #top_movies = soupify('https://www.imdb.com/chart/top/')

    url = 'https://www.imdb.com/chart/top/'
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')

    movie_page = getMoviePage(soup, random.randrange(0,249))
    movie_info = movieInfo(movie_page)
    review_page = getReviewPage(movie_page)
    bad_review = getBadReview(review_page)
    movie_info['review'] = bad_review
    return movie_info

#dropdown_pref = '?sort=userRating&dir=asc&ratingFilter=0'

#msoup = getMoviePageSoup(0)
#csoup = getReviewPage(msoup)
#ssoup = specificReviewPage(csoup)
#print(reviewFromSpecificPage(ssoup))
