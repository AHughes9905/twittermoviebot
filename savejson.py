import json
import pickle
Q_SIZE = 7

def checkNewReview(rurl):
    with open('data/reviewURLS.json', 'r') as f:
        data = json.load(f)
    if rurl not in data:
        return True
    return False

def inRecentMovies(movie):
    with open('data/recentmovies.txt', 'rb') as saved_q:
        q = pickle.load(saved_q)
    if movie in q:
        return True
    return False

def updateRecentMovies(movie):
    with open('data/recentmovies.txt', 'wb+') as saved_q:
        pickle.dump([], saved_q)
    with open('data/recentmovies.txt', 'rb') as saved_q:
        q = pickle.load(saved_q)
    q.append(movie)
    if len(q) > Q_SIZE:
        q.pop(0)
    with open('data/recentmovies.txt', 'wb+') as saved_q:
        pickle.dump(q, saved_q)
    
def addReview(rurl, movie):
    with open('data/reviewURLS.json', 'r') as f:
        data = json.load(f)
    data[rurl] = movie
    with open('data/reviewURLS.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


