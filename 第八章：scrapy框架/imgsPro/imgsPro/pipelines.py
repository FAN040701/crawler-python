# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy

'''class ImgsproPipeline:
    def process_item(self, item, spider):
        return item'''
from scrapy.pipelines.images import ImagesPipeline
class imgsPipeLine(ImagesPipeline):
    #根据图片地址就行图片数据的请求
    def get_media_requests(self, item, info):
        yield scrapy.Request(item["img_src"],meta={"item":item})

    #指定图片存储的路径
    def file_path(self, request, response=None, info=None, *, item=None):
        #获取图片名字
        img_name = request.meta["item"]["img_name"]
        #返回图片名字
        return img_name
    
    def item_completed(self, results, item, info):
        return item #返回给下一个即将被执行的管道类
