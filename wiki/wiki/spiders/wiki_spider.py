from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from wiki.items import WikiItem

class WikiSpider(BaseSpider):
  name = 'wiki'
  start_urls = ["http://en.wikipedia.org/wiki/Nba"]
  def parse(self,rep):
    hxs = HtmlXPathSelector(rep)
    item = WikiItem()   
    item['blue'] = hxs.select("//div[@class='mw-body-content']//a/@title").extract() 
    item['underline']= hxs.select("//span[@class='toctext']/text()").extract()
    return item
