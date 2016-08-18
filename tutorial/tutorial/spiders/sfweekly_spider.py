import scrapy
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors.sgml import SgmlLinkExtractor
# from scrapy.linkextractors import LinkExtractor 
from tutorial.sfweekly_items import SFWeeklyItem

class SFWeeklySpider(scrapy.Spider):
	# Necessary variables for setting up a spider
	name = "sfweekly"
	allowed_domains = ["sfweekly.com"]
	start_urls = ["http://archives.sfweekly.com/sanfrancisco/EventSearch?narrowByDate=Today"]

	# Defines how a spider follows links
	# Allow defines the link href
	# Callback calls the parsing function
	# Follow instructs spider to continue following links
	# rules = Rule(SgmlLinkExtractor(allow=(), 
	# 	                       restrict_xpaths=('//*[@id="PaginationBottom"]/a'),
	# 	                       callback="parse_yays", 
	# 	                       follow=True)
	# )

	
	def parse(self, response):
		''' Grabs a list of links to follow'''
		for num in response.xpath('//*[@id="PaginationBottom"]/a/@data-page').extract():
			url = self.start_urls[0] + "&page=" + num
			yield scrapy.Request(url, callback=self.parse_yays)

	# Scrapes each event calendar page for events
	def parse_yays(self,response):
		''' Extracts relevant event info from page'''
		for sel in response.xpath('//*[@id="searchResults"]/div/div'):	
			item = SFWeeklyItem()
			item['name'] = sel.xpath('div[1]/a/span').extract()
			item['url'] = sel.xpath('div[1]/a/@href').extract()
			item['location'] = sel.xpath('div[2]/div/span[1]').extract()
			yield item

		# next_page = response.xpath('//*[@id="PaginationBottom"]/a')
		# for page in next_page:
		# 	url = response.urljoin(next_page.extract())
		# 	yield scrapy.Request(url, self.parse)



