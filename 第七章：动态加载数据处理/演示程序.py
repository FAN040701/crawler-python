from selenium import webdriver
from selenium.webdriver.edge.service import Service
from time import sleep
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, 'chromedriver.exe')
driver = webdriver.Chrome(service=Service(image_path))
#用get打开百度页面
driver.get("https://www.baidu.com")
#查找页面的设置元素，并进行点击
driver.find_element('link text', "设置")[0].click()
sleep(2)
#查找页面的搜索设置元素，并进行点击,设置为每页显示50条
driver.find_element('link text', "搜索设置")[0].click()
sleep(2)
#选中每页显示50条
m=driver.find_element('id', "nr")
sleep(2)
m.find_element('//*[@id="nr"]/option[3]').click()
m.find_element('//option[3]').click()
sleep(2)
#保存设置的信息
driver.find_element('class name', "prefpanelgo").click()
sleep(2)
#接受警告信息,确定accept，取消dismiss
driver.switch_to().accept()
sleep(2)
#找到百度的输入框，并输入 美女
driver.find_element('id', "kw").send_keys(u"美女")
sleep(2)
#点击搜索按钮
driver.find_element('id', "su").click()
sleep(2)
#在打开的页面中找到“Selenium - 开源中国社区”，并打开这个页面
driver.find_element('link text', "美女_百度图片").click()
sleep(2)
#关闭浏览器
driver.quit()
input('Press Enter to exit...')

