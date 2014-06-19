#!/usr/bin/python

import sys
import json
from pprint import pprint
#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

f = file(str(sys.argv[1]) ,  'r')
g = file( "wiki.keys",'w')

json_data = json.load(f)
#print json_data['content']
#for item in json_data:
# print item[][] 
for title in json_data['title']:
  print title.encode('utf-8').strip()
for content in json_data['content']:
  print content.encode('utf-8').strip()
 # for word in content:
    # word = word.encode('utf-8').strip()
    # print word
    # print >> word+'\n', g
