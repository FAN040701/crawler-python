from selenium import webdriver
from selenium.webdriver.edge.service import Service
from time import sleep
import os
#实现无可视化界面的
from selenium.webdriver.chrome.options import Options
#实现规避检测
from selenium.webdriver import ChromeOptions

#实现无可视化界面的操作 不用背下来
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#如何让selenium规避被检测到的风险 不用背下来
#option = ChromeOptions()
#option.add_experimental_option('excludeSwitches',['enable-automation'])

current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, 'chromedriver.exe')
#webdriver.phantomjs.service_args = ['--load-images=no','--disk-cache=yes']
bro = webdriver.Chrome(service=Service(image_path), options=chrome_options)

#无可视化界面，无头浏览器  phantomJs
bro.get('https://www.baidu.com/')
print(bro.page_source)
sleep(2)
bro.quit()