import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from fbsPro.items import FbsproItem

class FbsSpider(RedisCrawlSpider):
    name = "fbs"
    #allowed_domains = ["www.xxx.com"]
    #start_urls = ["https://www.xxx.com"]

    redis_key = "sun"

    rules = (Rule(LinkExtractor(allow=r"id=1&page=\d+"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[3]/div[3]/ul[2]/li')
        for li in li_list:
            new_num = li.xpath('./span[1]/text()').extract_first()
            new_title = li.xpath('./span[3]/a/text()').extract_first()

            item = FbsproItem()
            item['new_num'] = new_num
            item['title'] = new_title

            yield item
