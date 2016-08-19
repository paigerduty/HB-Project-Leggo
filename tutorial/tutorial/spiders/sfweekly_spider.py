import scrapy
from tutorial.sfweekly_items import SFWeeklyItem
from scrapy.utils.markup import remove_tags

class SFWeeklySpider(scrapy.Spider):
	# Necessary variables for setting up a spider
	name = "sfweekly"
	allowed_domains = ["sfweekly.com"]
	start_urls = ["http://archives.sfweekly.com/sanfrancisco/EventSearch?narrowByDate=Today"]

	
	def parse(self, response):
		''' Grabs a list of links to follow'''
		for num in response.xpath('//*[@id="PaginationBottom"]/a/@data-page').extract():
			url = self.start_urls[0] + "&page=" + num
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
			yield item

		fields = ["name", "url", "location"]
		with open('scraped_items.txt','r+') as f:
			for field in fields:
				f.write("{}\n".format(field))

			for item in items:
				vals = item.values()
				for vals in vals:
					f.write("{}\n".format(vals))

			



