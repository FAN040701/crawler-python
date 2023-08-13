import scrapy
from bossPro.items import BossproItem

class BossSpider(scrapy.Spider):
    name = "boss"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.zhipin.com/web/geek/job?query=python&city=101010100"]

    url = "https://www.zhipin.com/web/geek/job?query=python&city=101010100&page=%d"
    page_num = 2

    number = int(input("请输入你要爬取的页数:"))

    #回调函数接受item参数
    def parse_detail(self,response):
        item = response.meta['item']
        job_desc = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[1]/div[2]//text()').extract()
        job_desc = "".join(job_desc).strip()

        #print(job_desc)
        item["job_desc"] = job_desc

        yield item

    #解析首页的数据
    def parse(self, response):
        li_list = response.xpath('//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[2]/ul/li')
        for li in li_list:
            item = BossproItem()
            job_name = li.xpath('.//div[@class="job-title clearfix"]/span[@class="job-name"]/text()').extract_first()
            item["job_name"] = job_name

            #print(job_name)

            detail_url = 'https://www.zhipin.com' + li.xpath('.//a/@href').extract_first()
            #对详情页发起请求获取详情页的页面源码数据
            '''手动请求的发送
            meta参数: 在不同的解析函数之间传递数据,是一个字典类型'''
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={"item":item})
        
        #分页操作
        if self.page_num <= self.number:
            new_url = format(self.url % self.page_num)
            self.page_num += 1
            #手动请求的发送
            yield scrapy.Request(new_url,callback=self.parse)
