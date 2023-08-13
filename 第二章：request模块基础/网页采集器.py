import requests
#反爬
"""UA检测:门户网站的服务器会检测对应请求的载体身份标识，
如果检测到请求的载体身份标识为某一款浏览器，说明该请求是一个正常的请求。
但是，如果检测到请求的载体身份标识不是基于某一款浏览器的，
则表示该请求为不正常的请求(爬虫)，则服务器端很有可能拒绝该次请求。
UA：User-Agent(请求载体的身份标识)"""

#反反爬
"""UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器。"""

if __name__ == '__main__':
    #将对应的UA封装到一个字典中(UA伪装)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    url = 'https://www.sogou.com/web?'#问号可以不保留
    #这个网址是不完整的，但是只保留query也不影响爬取
    kw = input('enter a word: ')
    #处理url携带的参数：封装到字典中
    param = {'query': kw}
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text
    filename = kw+'.html'
    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(filename,'保存成功！！！')
