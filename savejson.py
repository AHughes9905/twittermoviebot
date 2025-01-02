import json
import queue


def checkNewReview(rurl, movie):
    with open('reviewURLS.json', 'r') as f:
        data = json.load(f)
        f.close()
        if movie not in data:
            return False
        reviews = data[movie]
        for url in reviews:
            if url == rurl:
                return False
        return True
    return False

def inRecentMovies(movie):
    with open('past.json', 'r') as f:
        data = json.load(f)
        f.close()
        q = data['movies']
        if movie in q:
            return True
        return False
    return False

def updateRecentMovies(movie):
    with open('past.json', 'r') as f:
        data = json.load(f)
    f.close()
    q = data['movies']
    if len(q) > 10:
        q.empty()
        q.put(movie)
        data['movies'] = q
    with open('past.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return True
    

def addReview(rurl, movie):
    with open('reviewURLS.json', 'r') as f:
        data = json.load(f)
    if movie in data:
        reviews = data[movie]
        reviews.append(rurl)
        data[movie] = reviews
    else:
        data[movie] = [rurl]
    with open('past.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return True


