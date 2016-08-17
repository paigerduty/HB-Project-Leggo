import scrapy
from tutorial.sfweekly_items import SFWeeklyItem

class SFWeeklySpider(scrapy.Spider):
	name = "sfweekly"
	allowed_domains = ["sfweekly.com"]
	start_urls = ["http://archives.sfweekly.com/sanfrancisco/EventSearch?narrowByDate=Today"]

	def parse(self,response):
		""" For each 'event' grab the name and the url."""
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



