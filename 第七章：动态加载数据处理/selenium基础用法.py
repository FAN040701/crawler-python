from selenium import webdriver
from selenium.webdriver.edge.service import Service
from time import sleep
from lxml import etree
import os
#实例化一个edge浏览器对象(传入浏览器的驱动程序)
#打印电影名称
current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, 'msedgedriver.exe')
driver = webdriver.ChromiumEdge(service=Service(image_path))

driver.get('https://m.douban.com/movie/')
sleep(2)

#获取浏览器当前页面的页面源码数据
page_text = driver.page_source

#解析电影名称
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="app"]/div/section[1]/div[2]/div/a')
for li in li_list:
    name = li.xpath('./div[2]/div[1]/text()')[0]
    print(name)

driver.quit()