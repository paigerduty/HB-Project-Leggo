import scrapy

class YayObject(scrapy.Spider):
	name = 'sfweekly'
	allowed_domains = ['sfweekly.com']
	start_urls = ['http://archives.sfweekly.com/sanfrancisco/EventSearch?narrowByDate=Today']

	def parse(self,response):
		""" For each 'event' grab the name and the url."""
		filename = response.url.split("/")[-2] + '.html'
		with open(filename,'wb') as f:
			f.write(response.body)

	def parse_yay(self, response):
		""" Follows the url to grab the element 'span.street-address' """
		pass
		# yield { 'address': response.css('span. street-address')}