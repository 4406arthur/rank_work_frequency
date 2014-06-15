import json
import urllib

def showsome(searchfor):
  urls = []
  query = urllib.urlencode({'q': searchfor})
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
  search_response = urllib.urlopen(url)
  search_results = search_response.read()
  results = json.loads(search_results)
  data = results['responseData']
  print 'Total results: %s' % data['cursor']['estimatedResultCount']
  hits = data['results']
  print 'For more results, see %s' % data['cursor']['moreResultsUrl']
  for h in hits: 
    urls.append(h['url'].encode('utf-8'))
  return urls

showsome('apple')
