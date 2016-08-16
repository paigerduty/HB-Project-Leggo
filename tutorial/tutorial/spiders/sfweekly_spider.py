import scrapy

class YayObject(scrapy.Spider):
	name = 'sfweekly'
	allowed_domains = ['sfweekly.com']
	start_urls = ['http://archives.sfweekly.com/sanfrancisco/EventSearch?narrowByDate=Today']

	def parse(self,response):
		""" For each 'event' grab the name and the url."""
		for sel in response.xpath

	def parse_yay(self, response):
		""" Follows the url to grab the element 'span.street-address' """
		pass
		# yield { 'address': response.css('span. street-address')}