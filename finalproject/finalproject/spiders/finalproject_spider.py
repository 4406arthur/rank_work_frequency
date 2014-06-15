from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from finalproject.items import FinalprojectItem
from search import showsome

class StockSpider(BaseSpider):
	name = 'finalproject'
	#allowed_domains = ['br.financas.yahoo.com']
	start_urls = showsome('NBA champion')
	def parse(self, response):
		self.log('URL: %s' % response.url)

		hxs = HtmlXPathSelector(response)
		item = FinalprojectItem()
		item['title'] = hxs.select('//title/text()').extract()
		item['content'] = hxs.select('//p/text()').extract()
		return item
