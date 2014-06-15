# Get the first 20 hits for: "Breaking Code" WordPress blog
from google import search

def showsome(searchfor):
    url = []
    for h in search(searchfor ,stop=20):
      url.extend(h)
    return url
showsome('apple')
print(url)
