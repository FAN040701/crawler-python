#需求：爬取58二手房中的房源信息
import requests
from lxml import etree

if __name__ == "__main__":
    #爬取到页面源码数据
    url = 'https://bj.58.com/ershoufang/'
    headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    page_text = requests.get(url=url, headers=headers).text

    #数据解析
    tree = etree.HTML(page_text)
    #存储的就是标签对象
    r_list = tree.xpath('//div[@class="property"]//h3/text()')
    #print(r_list)
    fp = open('58.txt', 'w', encoding='utf-8')
    for r in r_list:
        print(r)
        fp.write(r+'\n')
#./表示当前目录下
#../表示上一级目录
    fp.close()