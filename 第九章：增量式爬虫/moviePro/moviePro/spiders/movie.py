import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redis import Redis
from moviePro.items import MovieproItem

class MovieSpider(CrawlSpider):
    name = "movie"
    #allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.4567kp.com/frim/index1.html"]

    rules = (Rule(LinkExtractor(allow=r"/frim/index1-\d+\.html"), callback="parse_item", follow=True),)
    #创建redis连接对象
    redis = Redis(host='127.0.0.1',port=6379)

    #解析电影详情页
    def parse_item(self, response):
        li_list = response.xpath("//div[@class='stui-pannel_bd']/ul[@class='stui-vodlist clearfix']/li")
        for li in li_list:
            detail_url = li.xpath("./div[@class='stui-vodlist__box']/a/@href").extract_first()

            #将详情页的url存入redis中
            exxists = self.redis.sadd("movie_url",detail_url)
            if exxists == 1:
                print("该url未被爬取, 可以进行爬取")
                yield scrapy.Request(detail_url,callback=self.parse_detail)
            else:
                print("数据已存在，不需要爬取")

    #解析详情页中的电影名称和类型，进行持久化存储
    def parse_detail(self, response):
        item = MovieproItem()
        item["name"] = response.xpath("//h1/text()").extract_first()
        item["type"] = response.xpath("//span[contains(text(),'类型')]/following-sibling::a/text()").extract()
        
        yield item
