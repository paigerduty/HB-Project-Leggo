import scrapy
from tutorial.sfweekly_items import SFWeeklyItem
from scrapy.utils.markup import remove_tags

class SFWeeklySpider(scrapy.Spider):
	name = "sfweekly"
	allowed_domains = ["sfweekly.com"]
	base_url = 'http://archives.sfweekly.com/sanfrancisco/EventSearch?narrowByDate=Today&page=%s'
	start_urls = []

	for num in range(1,10):
		start_urls.append(base_url % num)
	
	def parse(self, response):
		''' Grabs a list of links to follow'''
		for url in start_urls:
			yield scrapy.Request(url, callback=self.parse_yays)

	# Scrapes each event calendar page for events
	def parse_yays(self,response):
		''' Extracts relevant event info from page saves as SFWeeklyItem'''
		items = []

		for sel in response.xpath('//*[@id="searchResults"]/div/div'):	
			item = SFWeeklyItem()
			item['name'] = sel.xpath('div[1]/a/span/text()').extract()
			item['url'] = sel.xpath('div[1]/a/@href').extract()
			item['location'] = sel.xpath('div[2]/div/span[1]/text()').extract()
			items.append(item)
			# yield item

		# Iterates through items and writes their values to file
		with open('scraped_items.txt','r+') as f:
			for item in items:
				f.write("%s | %s | %s\n" % (item['name'], item['url'], item['location']))
			f.close()

			



