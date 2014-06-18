# Get the first 20 hits for: "Breaking Code" WordPress blog
from google import search

def showsome(searchfor):
    url = []
    for h in search(searchfor ,stop=10):
      url.append(h)
    return url
