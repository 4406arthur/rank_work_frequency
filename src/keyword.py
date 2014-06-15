import urllib
import urllib2
import json
from pprint import pprint

URL = "https://sentinelprojects-skyttle20.p.mashape.com/"

text = "We have visited this restaurant a few times in the past, and the meals have been ok, but this time we were deeply disappointed."

opener = urllib2.build_opener(urllib2.HTTPHandler)
params = {'text': text, 'lang': 'en', 'keywords': 1, 'sentiment': 1}
headers = {'X-Mashape-Authorization': 'LQSCTPT8fZ6riueYRFlIV3RK2FPXDncw'}

request = urllib2.Request(URL, urllib.urlencode(params), headers=headers)
response = opener.open(request)
opener.close()
data = json.loads(response.read())

pprint(data)

