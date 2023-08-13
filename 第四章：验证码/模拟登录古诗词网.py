import requests
from lxml import etree
import os
from Chaojiying_Python import chaojiying
#创建一个session对象
session = requests.Session()
#1.验证码的识别，获取验证码图片的文字数据
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',}
            #'Cookie': 'xxxx'}
#对验证码图片的请求对应的url地址发起请求，获取页面数据
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
img_src = 'https://so.gushiwen.org' + tree.xpath('//*[@id="imgCode"]/@src')[0]
#xpath中的*表示任意标签，@src表示标签中的src属性值
img_data = session.get(url=img_src, headers=headers).content
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
print("验证码已成功获取，文件 code.jpg 已被成功删除")
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
#使用session发起请求，cookie保存在其中
response = session.post(url=login_url, headers=headers, data=data)
if response.status_code == 200:
    print('登录成功')

#爬取个人主页对应页面的数据
detail_url = 'https://so.gushiwen.cn/user/collect.aspx'
#使用session进行请求发送
response = session.get(url=detail_url, headers=headers)
response.encoding = 'utf-8'
detail_page_text = response.text
path2 = os.path.join(current_directory, 'gushiwen.html')
with open(path2, 'w', encoding='utf-8') as fp:
    fp.write(detail_page_text)
    #模拟登陆成功
