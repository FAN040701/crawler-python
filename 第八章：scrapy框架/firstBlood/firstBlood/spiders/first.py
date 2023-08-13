import scrapy


class FirstSpider(scrapy.Spider):
    #爬虫文件的名称：就是爬虫源文件的一个唯一标识
    name = "first"
    #允许的域名：用来限定start_urls列表中哪些url可以进行请求发送，不在列表中的url不进行请求发送
    #allowed_domains = ["www.baidu.com"]

    """通常不会用域名限定"""

    #起始的url列表：该列表中存放的url会被scrapy自动进行请求的发送
    #url可以自己改
    start_urls = ["https://www.baidu.com/", "https://www.sogou.com/"]

    #用作于数据解析：response参数表示的就是请求成功后对应的响应对象
    #会被调用多次，每次传递进来的response就是请求成功后对应的响应对象
    def parse(self, response):
        print(response)
        pass
