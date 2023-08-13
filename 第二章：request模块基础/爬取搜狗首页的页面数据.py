#需求：爬取搜狗首页的页面数据
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests

if __name__ == '__main__':
    """if __name__ == '__main__':是一个常见的Python编程惯用语句，
    它的作用是判断当前模块是否作为主程序直接运行。
    在Python中，每个模块都有一个特殊的属性__name__，
    当模块被直接运行时，__name__的值会被设置为'__main__'；
    而当模块被作为导入的模块时，__name__的值会是模块的名字。
    因此,使用if __name__ == '__main__':可以判断当前模块是否作为主程序直接运行。
    如果是主程序直接运行，则会执行if语句块中的代码；
    如果是作为导入的模块，则if语句块中的代码不会被执行。
    在给定的代码中，if __name__ == '__main__':
    的作用是确保只有当该脚本作为主程序直接运行时才会执行其中的代码。
    这样可以避免在导入该脚本时自动执行其中的代码，只在需要时手动调用该脚本。"""
    #1.ָ指定url
    url = 'https://www.sogou.com/'
    #2.发起请求
    #get方法会返回一个响应对象
    response = requests.get(url=url)
    #3.获取响应数据.text返回的是字符串形式的响应数据
    page_text = response.text
    print(page_text)
    #4.持久化存储
    with open('./sogou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
        """使用as fp的好处是，在with语句块结束后，文件对象会自动关闭。
        这样可以确保及时释放文件资源，并且无需手动调用close()方法关闭文件。"""
    print('爬取数据结束！！！')
    