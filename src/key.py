#!/usr/bin/python

import urllib
import urllib2
import json
from pprint import pprint

URL = "https://sentinelprojects-skyttle20.p.mashape.com/"

text = raw_input();

opener = urllib2.build_opener(urllib2.HTTPHandler)
params = {'text': text, 'lang': 'en', 'keywords': 1, 'sentiment': 1}
headers = {'X-Mashape-Authorization': 'LQSCTPT8fZ6riueYRFlIV3RK2FPXDncw'}

request = urllib2.Request(URL, urllib.urlencode(params), headers=headers)
response = opener.open(request)
opener.close()
data = json.loads(response.read())

#pprint(data)

keywords = ''
for docs in data['docs']:
  for terms in docs['terms']:
    for term in terms['term']:
      c = term.encode('utf-8').strip()
      keywords += c
    keywords += ' '


if( len(keywords) == 0 ):
  keywords = text
else:
  keywords = keywords[:-1]

print keywords
