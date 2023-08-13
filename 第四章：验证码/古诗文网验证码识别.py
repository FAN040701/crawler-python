#将验证码图片下载到本地
'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
import requests
from lxml import etree
from Chaojiying_Python import chaojiying
import os
#封装识别验证码图片的函数

if __name__ == "__main__":
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    #对验证码图片的请求对应的url地址发起请求，获取页面数据
    page_text = requests.get(url=url, headers=headers).text
    #解析验证码图片img中src属性值
    tree = etree.HTML(page_text)
    img_src = 'https://so.gushiwen.org' + tree.xpath('//*[@id="imgCode"]/@src')[0]
    #print(img_src)
    img_data = requests.get(url=img_src, headers=headers).content
    #将验证码图片保存到本地
    current_directory = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_directory, 'code.jpg')
    with open(image_path, 'wb') as fp:
        fp.write(img_data)
    
    #识别验证码图片中的数据---》超级鹰
    chaojiying = chaojiying.Chaojiying_Client('18198010362', 'onetwo123456', '96001')
    	#用户中心>>软件ID 生成一个替换 96001
    im = open(image_path, 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    print('识别结果为：', chaojiying.PostPic(im, 1902)['pic_str'])
