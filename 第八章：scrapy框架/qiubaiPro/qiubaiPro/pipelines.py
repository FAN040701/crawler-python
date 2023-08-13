# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class QiubaiproPipeline:
    fp = None
    #重写父类的一个方法：该方法只在开始爬虫的时候被调用一次
    def open_spider(self, spider):
        print('开始爬虫......')
        self.fp = open('./qiubai.txt', 'w', encoding='utf-8')
    
    #专门用来处理item类型对象
    #该方法可以接受爬虫文件提交过来的item对象
    #该方法每接受一个item就被调用一次
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']

        self.fp.write(author+':'+content+'\n')

        return item #会传递给下一个即将被执行的管道类
    
    def close_spider(self, spider):
        print('结束爬虫......')
        self.fp.close()

#管道文件中一个管道类对应将一组数据存储到一个平台或载体中
class mysqlPipeLine(object):
    conn = None
    cursor = None
    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1',port = 3306, user = 'root',password = '123456', db = 'qiubai',charset = 'utf8')

    def procees_item(self, item, spider):
        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute('insert into qiubai values("%s", "%s")' % (item['author'], item['content']))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
            
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

#爬虫文件提交的item类型的对象最终会提交给哪一个管道类？
    #会将item提交给优先级数值最低的管道类
    


'''在Python中, self是一个约定俗成的参数名称, 通常用于类的方法中。它表示对类的实例的引用。
当你调用一个类的方法时, self参数会自动传递给方法, 以便你可以访问和操作该类的属性和方法。 '''
