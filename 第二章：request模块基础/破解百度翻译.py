import requests
import json

if __name__ == '__main__':
    #1.指定url
    post_url = 'https://fanyi.baidu.com/sug'
    #2.进行UA伪装
    headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    #3.post请求参数处理(同get请求一致)
    words = input('enter a word: ')
    data = {'kw': words}

    #4.请求发送
    response = requests.post(url=post_url, data = data, headers=headers)
    #5.获取响应数据:json()方法返回的是obj(如果确认响应数据是json类型的，才可以使用json()方法)
    dic_obj = response.json()

    #持久化存储
    filename = words+'.json'
    fp = open(filename,'w',encoding='utf-8')
    '''json.dump(): 用于将 Python 对象转换为 JSON 并将其写入文件。
    它接受一个 Python 对象和一个文件对象作为参数，并将 JSON 数据写入文件中。'''
    json.dump(dic_obj, fp, ensure_ascii=False)
    #由于json文件中的中文是Unicode编码，所以需要在json.dump()中添加ensure_ascii=False参数
    fp.close()

    #试着用text方法获取响应数据，查看结果
    page = response.text
    filename2 = words+'.html'
    with open(filename2, 'w', encoding='utf-8') as fp2:
        fp2.write(page)
    #json文件在html中的显示效果不好，所以还是用json.dump()方法
    print('over!!!')
