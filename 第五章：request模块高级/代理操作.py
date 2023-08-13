#需求：45.142.246.167
import requests
import os
url = 'https://www.baidu.com/s?wd=ip'
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',}

page_text = requests.get(url=url, headers=headers, proxies={"https":'45.142.246.167'}).text
current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, 'ip.html')
with open(image_path, 'w', encoding='utf-8') as fp:
    fp.write(page_text)

#反爬机制：封IP
#反反爬策略：使用代理IP进行爬取

#由于目标计算机积极拒绝，无法连接。所以代理IP失效了