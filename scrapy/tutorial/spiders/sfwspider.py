# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector

# How to follow links and pagination
# How to extract and parse the field
# Must define 3 attributes: name, start urls, parsing method XPATH

class SFWeeklySpider(scrapy.Spider):
    name = "sfwspider"
    allowed_domains = ["sfweekly.com"]
    start_urls = (
        'http://www.sfweekly.com/sanfrancisco/EventSearch?narrowByDate=Today',
    )

    def parse(self, response):
    	hxs = HtmlXPathSelector(response)
    	sites = hxs.select('//ul/li')
    	items = []
    	# For each page in SF Weekly Events for this date extract the following
    	# Event name, URL for more info, and description

    	for site in sites:
    	    item = SFWItem()
    		item['title'] = site.select('//div[@class="').extract()
    		item['link'] = site.select
    		item['desc'] = site.select
    	  items.append(item)
    return items
    	