#!/usr/bin/python
import sys
import json
from pprint import pprint
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

f = file(str(sys.argv[1]) ,  'r')
g = file('test','w')
json_data = json.load(f)
for item in json_data:
   #print item["content"]
   for word in item["content"]:
       w = word.encode('utf-8').strip()
       g.write( w + '\n' )


