import scrapy


class MiddleSpider(scrapy.Spider):
    #爬取百度
    name = "middle"
    #allowed_domains = ["www.xxx.com"]
    start_urls = ["http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=ip"]

    def parse(self, response):
        page_text = response.text

        with open("ip.html","w",encoding="utf-8") as fp:
            fp.write(page_text)

