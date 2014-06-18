#!/usr/bin/python
import sys
import urllib
import urllib2
import json
from pprint import pprint

URL = "https://sentinelprojects-skyttle20.p.mashape.com/"
#text = sys.args[]
text = raw_input()

opener = urllib2.build_opener(urllib2.HTTPHandler)
params = {'text': text, 'lang': 'en', 'keywords': 1, 'sentiment': 1}
headers = {'X-Mashape-Authorization': 'LQSCTPT8fZ6riueYRFlIV3RK2FPXDncw'}

request = urllib2.Request(URL, urllib.urlencode(params), headers=headers)
response = opener.open(request)
opener.close()
data = json.loads(response.read())

keywords = ''
for docs in data['docs']:
  for terms in docs['terms']:
    for term in terms['term']:
      keywords += term
    keywords += ' '

#print 'test: ' + keywords + ':end'

if( len(keywords) == 0 ):
	keywords = text

print keywords

