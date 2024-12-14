import json

def checkReview(rurl, movie):
    f = open('reviewURLS.json')
    data = json.load(f)
    f.close()
    if movie not in data:
        return False
    reviews = data[movie]
    for url in reviews:
        if url == rurl:
            return False
    return True

def pastFewMovies():
    return

def addReview(rurl, movie):
    f = open('reviewURLS.json')
    data = json.load(f)
    f.close()
    if movie in data:
        reviews = data[movie]
        reviews.append(rurl)
        data[movie] = reviews
    else:
        data[movie] = rurl
    
    with open('data.txt', 'w') as f:
        json.dump(data, f, ensure_ascii=False)
    return

