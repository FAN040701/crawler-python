#需求：爬取糗图百科中糗图板块下的所有的糗图图片

import requests

if __name__ == "__main__":
    #如何爬取图片数据
    url = "https://s0.2mdn.net/simgad/11839480896507019181"
    img_data = requests.get(url=url).content
    #content返回的是二进制形式的图片数据
    """text返回的是字符串形式的图片数据
       content返回的是二进制形式的图片数据
       json返回的是对象形式的数据"""
    
    with open('./qiutu.jpg','wb') as fp:
        fp.write(img_data)
        print("图片下载成功！")

#由于糗图百科没有了，随便找了一张别的图片
