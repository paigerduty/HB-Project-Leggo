import scrapy
from tutorial.sfweekly_items import SFWeeklyItem
from scrapy.utils.markup import remove_tags

class SFWeeklySpider(scrapy.Spider):
	name = "sfweekly"
	allowed_domains = ["sfweekly.com"]
	base_url = 'http://archives.sfweekly.com/sanfrancisco/EventSearch?narrowByDate=Today'
	baser_url = 'http://archives.sfweekly.com/sanfrancisco/EventSearch?narrowByDate=Today&page=%s'
	start_urls = []

	start_urls.append(base_url)
	for num in range(2,9):
		start_urls.append(baser_url % num)
	
	def parse(self, response):
		''' Grabs a list of links to follow'''
		for url in self.start_urls:
			yield scrapy.Request(url, callback=self.parse_yays)

	# Scrapes each event calendar page for events
	def parse_yays(self,response):
		''' Extracts relevant event info from page saves as SFWeeklyItem'''
		items = []

		for sel in response.xpath('//*[@id="searchResults"]/div/div'):	
			item = SFWeeklyItem()

			name = sel.xpath('div[1]/a/span/text()').extract()
			url = sel.xpath('div[1]/a/@href').extract()
			location = sel.xpath('div[2]/div/span[1]/text()').extract()

			for i in name:
				str(i)
				name = i 

			for i in url:
				str(i)
				url = i

			for i in location:
				str(i)
				location = i

			item['name'] = name
			item['url'] = url
			item['location'] = location
			items.append(item)
			# yield item

		# Iterates through items and writes their values to file
		with open('scraped_items.txt','r+') as f:
			for item in items:
				f.write("%s | %s | %s\n" % (item['name'], item['url'], item['location']))
			f.close()

			



