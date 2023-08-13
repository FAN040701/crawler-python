import scrapy


class MeinvSpider(scrapy.Spider):
    number = int(input("你想看几页(别超过70): "))
                 
    name = "meinv"
    # allowed_domains = ["pic.netbian.com"]
    start_urls = ["https://pic.netbian.com/4kmeinv/index.html"]

    #生成一个通用的url模板（不可变）
    url = "https://pic.netbian.com/4kmeinv/index_%d.html"
    page_num = 2

    count = 0

    def parse(self, response):

        b_list = response.xpath("//div[@class='slist']/ul//b")
        for b in b_list:
            self.count = self.count + 1
            image_name = b.xpath("./text()").extract_first()
            print(image_name)
        
        if self.page_num <= self.number:
            #拼接新的url，并且手动请求发送给调度器入队列
            new_url = format(self.url%self.page_num)
            self.page_num += 1
            #手动请求发送：callback回调函数是专门用于数据解析
            yield scrapy.Request(url=new_url,callback=self.parse)
        else:
            print("总共有" + str(self.count) + "张图片")
