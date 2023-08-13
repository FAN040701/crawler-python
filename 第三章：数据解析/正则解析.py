#爬取某个网站的所有图片

import requests
import re #正则表达式模块
import os #操作系统模块
if __name__ == "__main__":
    #创建一个文件夹，保存所有的图片
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')
    url = "https://699pic.com/tupian-304474806.html"
    headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    
    # 使用requests模块的get方法请求url，对一整张页面进行爬取
    page_text = requests.get(url=url, headers=headers).text

    # 使用聚焦爬虫将页面中所有的图片进行解析/提取
    ex = r'<img.*?src="(.*?images.*?\.(?:jpg|png))".*?>'
    img_src_list = re.findall(ex, page_text, re.S)
    for i in img_src_list:
        print(i)

    for src in img_src_list:
        # 拼接出一个完整的图片url
        src = "https:" + src
        # 请求到了图片的二进制数据
        img_data = requests.get(url=src, headers=headers).content
        # 生成图片名称
        img_name = src.split('/')[-1]
        # 图片存储的路径
        imgPath = './picLibs/' + img_name
        with open(imgPath, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '下载成功！！！')
