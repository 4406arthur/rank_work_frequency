from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from finalproject.items import FinalprojectItem
from test import showsome

class StockSpider(Spider):
    name = 'finalproject'

    def __init__(self, query=None, *args, **kwargs):
        super(StockSpider, self).__init__(*args, **kwargs)
        self.start_urls = showsome(query)
    def parse(self, response):
        self.log('URL: %s' % response.url)
        hxs = HtmlXPathSelector(response)
        item = FinalprojectItem()
        item['title'] = hxs.select('//title/text()').extract()
        item['content'] = hxs.select('//p/text()').extract()
        return item
