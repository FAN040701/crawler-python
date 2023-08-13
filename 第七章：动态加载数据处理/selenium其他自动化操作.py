from selenium import webdriver
from selenium.webdriver.edge.service import Service
from time import sleep
from lxml import etree
import os
#实例化一个edge浏览器对象(传入浏览器的驱动程序)
current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, 'msedgedriver.exe')
bro = webdriver.ChromiumEdge(service=Service(image_path))

bro.get('https://www.taobao.com/')

#标签定位
search_input = bro.find_element('id','q')
#标签交互   
search_input.send_keys('Iphone')

#执行一组js程序
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)
#点击搜索按钮
btn = bro.find_element('css selector', '.btn-search')
btn.click()

sleep(3)

bro.get('https://www.baidu.com/')
sleep(2)
#回退
bro.back()
sleep(2)
#前进
bro.forward()
sleep(2)
bro.quit()