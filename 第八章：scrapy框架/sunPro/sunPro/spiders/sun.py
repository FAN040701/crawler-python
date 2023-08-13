import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunPro.items import SunproItem, DetailItem

#需求：爬取阳光政务网中所有的政务新闻标题，编号，新闻内容，标号
class SunSpider(CrawlSpider):
    name = "sun"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://wz.sun0769.com/political/index/politicsNewest?id=1&page=1"]

    #链接提取器：根据指定规则(allow="正则")进行指定链接的提取
    link = LinkExtractor(allow=r"id=1&page=\d+")
    link_detail = LinkExtractor(allow=r"/political/politics/index\?id=\d+")

    rules = (
        #规则解析器：将链接提取器提取到的链接进行指定规则的解析
        Rule(link, callback="parse_item", follow=True),
        #follow=True:表示链接提取器提取到的链接还要经过规则解析器进行解析
        #将链接提取器 继续作用到 链接提取器提取到的链接上
        Rule(link_detail, callback="parse_detail")
    )

    #解析新闻标题，编号，新闻内容，标号
    #如下两个解析方法中是不可以实现请求传参的，无法将两个解析数据存储到一个item中
    def parse_item(self, response):
        #注意：xpath表达式中不要出现tbody标签，因为xpath默认会补全tbody标签
        li_list = response.xpath('/html/body/div[3]/div[3]/ul[2]/li')
        for li in li_list:
            new_num = li.xpath('./span[1]/text()').extract_first()
            new_title = li.xpath('./span[3]/a/text()').extract_first()

            #print(new_num, new_title)
            item = SunproItem()
            item['new_num'] = new_num
            item['title'] = new_title

            yield item

    #解析新闻内容和新闻编号
    def parse_detail(self, response):
        new_id = response.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/span[5]/text()').extract_first()
        new_content = response.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/pre/text()').extract()
        new_content = ''.join(new_content)

        #print(new_id, new_content)

        item = DetailItem()
        item['new_id'] = new_id
        item['new_content'] = new_content

        yield item
