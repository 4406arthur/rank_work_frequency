from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from wiki.items import WikiItem

class WikiSpider(Spider):
  name = 'wiki'
  def __init__(self, query=None, *args, **kwargs):
    super(WikiSpider, self).__init__(*args, **kwargs)
    self.start_urls = ['http://en.wikipedia.org/wiki/%s' % query]
  def parse(self,rep):
    hxs = HtmlXPathSelector(rep)
    item = WikiItem()   
    item['blue'] = hxs.select("//div[@class='mw-body-content']//a/@title").extract() 
    item['underline']= hxs.select("//span[@class='toctext']/text()").extract()
    return item
