import scrapy


class ImgSpider(scrapy.Spider):
    name = "img"
    #allowed_domains = ["www.xxx.com"]
    start_urls = ["https://pic.netbian.com/4kmeinv/"]

    def parse(self, response):
        li_list = response.xpath('//*[@id="main"]/div[3]/ul/li')
        for li in li_list:
            #注意如果图片懒加载，要用src2这个伪属性
            
            img_src = "http://pic.netbian.com" + li.xpath('./a/img/@src')[0].extract()
            #print(img_src)
            img_name = li.xpath('./a/b/text()')[0].extract() + ".jpg"
            item = {}
            item["img_src"] = img_src
            item["img_name"] = img_name
            yield item
