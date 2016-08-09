# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector

# How to follow links and pagination
# How to extract and parse the field
# Must define 3 attributes: name, start urls, parsing method XPATH

class SFWeeklySpider(scrapy.Spider):
    name = "sfspider"
    allowed_domains = ["sfweekly.com"]
    start_urls = (
        'http://www.sfweekly.com/sanfrancisco/EventSearch?narrowByDate=Today',
    )

    def parse(self, response):
    	filename = response.url.split("/")[-2] + '.html'
    	with open(filename, 'wb') as f:
    		f.write(response.body)