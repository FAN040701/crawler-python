#由于人人网无法注册，这里我还是采用上一节用过的古诗文网站、
#1.验证码的识别，获取验证码图片的文字数据
#2.对post请求进行发送（处理请求参数）
#3.对响应数据进行解析

import requests
from lxml import etree
import os
from Chaojiying_Python import chaojiying
#1.验证码的识别，获取验证码图片的文字数据
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
#对验证码图片的请求对应的url地址发起请求，获取页面数据
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
img_src = 'https://so.gushiwen.org' + tree.xpath('//*[@id="imgCode"]/@src')[0]
#xpath中的*表示任意标签，@src表示标签中的src属性值
img_data = requests.get(url=img_src, headers=headers).content
#将验证码图片保存到当前目录
current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, 'code.jpg')
with open(image_path, 'wb') as fp:
    fp.write(img_data)
#使用超级鹰识别验证码图片中的数据

chaojiying = chaojiying.Chaojiying_Client('18198010362', 'onetwo123456', '96001')
im = open(image_path, 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
#print('识别结果为：', chaojiying.PostPic(im, 1902)['pic_str'])
code = chaojiying.PostPic(im, 1902)['pic_str']

#删除验证码图片
os.remove(image_path)
print(f"验证码已成功获取，文件 '{image_path}' 已被成功删除")
#f-string是python3.6版本新增的一种字符串格式化方法，它能够以更简单、更直观的方式代替传统的字符串格式化方法。

#2.对post请求进行发送（处理请求参数）
__VIEWSTATE = tree.xpath('//*[@id="__VIEWSTATE"]/@value')[0]
login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
data = {'__VIEWSTATE': __VIEWSTATE,
'__VIEWSTATEGENERATOR': 'C93BE1AE',
'from': 'http://so.gushiwen.cn/user/collect.aspx',
'email': '1527045331@qq.com',
'pwd': 'onetwo123456',
'code': code,
'denglu': '登录',}
response = requests.post(url=login_url, headers=headers, data=data)
print(response.status_code)
#用于获取服务器的响应状态码，200表示成功，404表示失败

response.encoding = 'utf-8'
page_text = response.text

'''path = os.path.join(current_directory, 'gushiwen.html')
with open(path, 'w', encoding='utf-8') as fp:
    fp.write(page_text)'''

#登录失败，验证码识别错误
