from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from finalproject.items import FinalprojectItem
from test import showsome
import json

x = 0
class StockSpider(Spider):
    name = 'finalproject'
    def __init__(self, query=None, *args, **kwargs):
        super(StockSpider, self).__init__(*args, **kwargs)
        self.start_urls = showsome(query)
    def parse(self, response):
        #self.log('URL: %s' % response.url)
        global x
        w = open('out/web.'+str(x+1),'w')
        hxs = HtmlXPathSelector(response)
        item = FinalprojectItem()
	ob = {}
        item['title'] = hxs.select('//title/text()').extract()
        item['content'] = hxs.select('//p/text()').extract()
	#print self.start_urls[1]
        item['url'] = self.start_urls[x]

	ob['title'] = hxs.select('//title/text()').extract()
	ob['content'] = hxs.select('//p/text()').extract()
	ob['url'] = self.start_urls[x]
	
        x += 1
	json.dump(ob,w)
	#print result
        #print >> w, result 
	return item
