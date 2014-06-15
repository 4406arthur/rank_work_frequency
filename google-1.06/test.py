# Get the first 20 hits for: "Breaking Code" WordPress blog
from google import search
for url in search('"Breaking Code" WordPress blog', stop=20):
    print(url)
