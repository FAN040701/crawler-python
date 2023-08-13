"""#!/user/bin/env python
#-*- coding:utf-8 -*-"""
"""第一行 #!/usr/bin/env python 是一个shebang注释，
它告诉操作系统要使用哪个解释器来执行脚本。在这个例子中，
python表示使用Python解释器来执行脚本。
/usr/bin/env是一个常见的Unix系统路径，它用于查找可执行文件所在的位置。
第二行 #-*- coding:utf-8 -*- 是一个字符编码声明，
它指定了脚本中使用的字符编码方式。在这个例子中，
utf-8表示使用UTF-8编码。UTF-8是一种通用的字符编码，支持包含各种语言字符的文本。"""
from bs4 import BeautifulSoup
import os
if __name__ == "__main__":
    # 将本地的html文档中的数据加载到该对象中
    current_directory = os.path.dirname(os.path.abspath(__file__))
    #print(current_directory)
    image_path = os.path.join(current_directory, 'sogou.html')
    #print(image_path)
    fp = open(image_path, 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, 'lxml')
    #print(soup)

    #print(soup.div) # soup.tagName 返回的是html中第一次出现的tagName标签
    #print(soup.a)

    #print(soup.find('div')) # soup.find('tagName') 返回的是html中第一次出现的tagName标签
    #等同于print(soup.div)

    #print(soup.find('div', class_='song'))
    #注意class后面有下划线

    #print(soup.find_all('a')) 
    # soup.find_all('tagName') 返回的是html中所有的tagName标签

    #print(soup.select('.song')) # soup.select('.class') 返回的是html中所有class=class的标签
    #.class 代表的是class属性

    #print(soup.select('.top-nav > ul > li > span'))
    # > 表示一个层级
    #print(soup.select('.top-nav > ul > li span')[0].get_text())
    #空格表示多个层级

    print(soup.select('.top-nav > ul a')[0]['href'])