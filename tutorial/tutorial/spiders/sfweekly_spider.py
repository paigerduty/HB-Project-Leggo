import scrapy

class SFWeeklySpider(scrapy.Spider):
	name = "sfweekly"
	allowed_domains = ["sfweekly.com"]
	start_urls = ["http://archives.sfweekly.com/sanfrancisco/EventSearch?narrowByDate=Today"]

	def parse(self,response):
		""" For each 'event' grab the name and the url."""

		filename = response.url.split("/")[-2] + '.html'
		with open(filename, 'wb') as f:
			f.write(response.body)

		for sel in response.xpath('//*[@id="searchResults"/div/div/div'):
			name = sel.xpath('a/span').extract()
			url = sel.xpath('a/@href').extract()
			# Location! Tell Scrapy to recursively scrape the event page 

	def parse_yay(self, response):
		""" Follows the url to grab the element 'span.street-address' """
		pass
		# yield { 'address': response.css('span. street-address')}