# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MovieproPipeline:
    conn = None
    def open_spider(self,spider):
        self.conn = spider.conn
    def process_item(self, item, spider):
        dic = {
            "name":item["name"],
            "type":item["type"]
        }
        print(dic)
        self.conn.lpush("movie",dic)
        return item