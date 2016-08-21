import scrapy
from tutorial.sfweekly_items import SFWeeklyItem
from scrapy.utils.markup import remove_tags

class SFWeeklySpider2(scrapy.Spider):
	# Necessary variables for setting up a spider
	name = "sfweekly2"
	allowed_domains = ["sfweekly.com"]
	start_urls = ["http://archives.sfweekly.com/sanfrancisco/EventSearch?narrowByDate=Today"]

	activity_list_xpath = '//*[@id="searchResults"/div/div'
	item_fields = {
		'name': './/div[1]/a/span/',
		'url': './/div[1]/a/@href',
		'location' : './/div[2]/div/span[1]/'
	}

	def parse(self, response):
		''' Grabs a list of links to follow'''
		# grab all events from all possible pages
		for num in response.xpath('//*[@id="PaginationBottom"]/a/@data-page').extract():
			url = self.start_urls[0] + "&page=" + num
			yield scrapy.Request(url, callback=self.parse_yays)

	# Scrapes each event calendar page for events
	def parse_yays(self,response):
		''' Extracts relevant event info from page saves as SFWeeklyItem'''
		# HtmlXPathSelector handles the response of when we request a webpage
		# Provides ability to select certain parts
		selector = HtmlXPathSelector(response)

		for activity in selector.select(self.activity_list_xpath):	
			# XPathItemLoader to load data into item_fields
			loader = XPathItemLoader(SFWeeklyItem(), selector=activity)

			# Defines processors
			# MapCompose cleans up extracted data
			# Join will join elements that are processed
			loader.default_input_processor = MapCompose(unicode.strip)
			loader.default_output_processor = Join()

			# Iterate over fields and add xpaths to the loader
			# iteritems returns an iterator over key-value pairs
			for field, xpath, in self.item_fields.iteritems():
				loader.add_xpath(field, xpath)
			yield loader.load_item()

	# 	fields = ["name", "url", "location"]
	# 	with open('scraped_items.txt','r+') as f:
	# 		for field in fields:
	# 			f.write("{}\n".format(field))

	# 		for item in items:
	# 			vals = item.values()
	# 			# for vals in vals:
	# 			f.write("{0} {1} {2}\n".format(vals[0], vals[1], vals[2]))

			

