import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem
import os
from selenium.webdriver.edge.service import Service

class WangyiSpider(scrapy.Spider):
    name = "wangyi"
    #allowed_domains = ["www.xxx.com"]
    start_urls = ["https://news.163.com/"]

    models_urls = []  #存储四个板块对应详情页的url

    #实例化一个浏览器对象
    def __init__(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(current_directory, 'chromedriver.exe')
        self.bro = webdriver.Chrome(service = Service(path))

    #解析板块对应详情页的url
    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[3]/div[2]/div[2]/div[2]/div/ul/li')
        alist = [1, 2, 4, 5]
        for index in alist:
            model_url = li_list[index].xpath('./a/@href').extract_first()
            self.models_urls.append(model_url)
        #print(self.models_urls)

        #对每一个板块对应的页面进行请求
        for url in self.models_urls:
            yield scrapy.Request(url=url, callback=self.parse_model)

    #每一个板块对应的新闻标题相关的内容都可能是动态加载出来的
    def parse_model(self, response):
        #解析每一个板块页面中对应新闻的标题和新闻详情页的url
        # response.xpath()
        div_list = response.xpath('/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:
            #新闻标题
            title = div.xpath('./div[1]/div[1]/h3/a/text() | ./div[1]/h3/a/text()').extract_first()
            #新闻详情页的url
            new_detail_url = div.xpath('./div[1]/div[1]/h3/a/@href | ./div[1]/h3/a/@href').extract_first()
            #print(title, new_detail_url)

            item = WangyiproItem()
            item['title'] = title

            #对新闻详情页的url发起请求
            yield scrapy.Request(url = new_detail_url, callback=self.parse_detail, meta={'title':title, 'detail_url':new_detail_url})

    
    def pare_detail(self, response):#解析新闻内容和新闻编辑
        content = response.xpath('//*[@id="content"]/div[2]//text()').extract()
        content = ''.join(content)
        print(content)

        item = response.meta['item']
        item['content'] = content

        yield item

    def closed(self, spider):
        self.bro.quit()

