# Get the first 20 hits for: "Breaking Code" WordPress blog
from google import search

def showsome(searchfor):
    url = []
    for h in search(searchfor ,stop=20):
      url.append(h)
    return url
#url = showsome('apple')
#print(url)
