from lxml import etree

if __name__ == "__main__":
    #实例化一个etree对象，且需要将被解析的源码数据加载到该对象中
    parser = etree.HTMLParser(encoding='utf-8')
    tree = etree.parse('sogou.html', parser=parser)
    #r = tree.xpath('/html/body/div')
    #r = tree.xpath('/html//div')
    #r = tree.xpath('//div')
    #r = tree.xpath('//div[@class="song"]') #属性定位
    #r = tree.xpath('//div[@class="song"]/p[1]') #索引定位,从1开始
    #r = tree.xpath('//div[@class="tang"]//li[5]/a/text()')[0] #文本定位
    #r = tree.xpath('//li[7]//text()') #文本定位
    #r = tree.xpath('//div[@class="song"]//text()') #文本定位
    r = tree.xpath('//div[@class="song"]/image/@src')[0] #文本定位
    print(r)