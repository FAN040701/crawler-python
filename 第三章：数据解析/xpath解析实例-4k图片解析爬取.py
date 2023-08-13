from lxml import etree
import requests
import os
#需求：爬取图片 https://pic.netbian.com/4kmeinv/

num = int(input('你想看几页(别超过68): '))
if __name__ == "__main__":
    url = 'https://pic.netbian.com/4kmeinv/'
    #UA伪装
    headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    #获取到页面源码数据
    response = requests.get(url=url,headers=headers)
    response.encoding = 'gbk'
    #text改成content作用是一样的
    page_text = response.text

    #数据解析：src的属性值 alt属性值
    tree = etree.HTML(page_text)
    li_list = tree.xpath('/html/body/div[@class="wrap clearfix"]//li')
    if not os.path.exists('./meinv'):
        os.mkdir('./meinv')
    for i in li_list:
        #局部解析
        wangzhi = 'https://pic.netbian.com' + i.xpath('./a/img/@src')[0]
        meinv_name = i.xpath('./a/img/@alt')[0] + '.jpg'

        """通用处理中文乱码的解决方案
        meinvname = meinvname.encode('iso-8859-1').decode('gbk')"""

        #print(meinv_name,wangzhi)
        #持久化存储
        meinv_data = requests.get(url=wangzhi,headers=headers).content
        #content返回的是二进制形式的图片数据
        meinv_path = 'meinv/' + meinv_name
        with open(meinv_path,'wb') as fp:
            fp.write(meinv_data)
            print(meinv_name,'下载成功！! !')
    
    def get_meinv(num, url='https://pic.netbian.com/4kmeinv/'):
        if num > 1:
            url = 'https://pic.netbian.com/4kmeinv/index_' + str(num) + '.html'
        response = requests.get(url=url_next,headers=headers)
        response.encoding = 'gbk'
        page_text = response.text
        tree = etree.HTML(page_text)
        li_list = tree.xpath('/html/body/div[@class="wrap clearfix"]//li')
        for i in li_list:
            wangzhi = 'https://pic.netbian.com' + i.xpath('./a/img/@src')[0]
            meinv_name = i.xpath('./a/img/@alt')[0] + '.jpg'
            meinv_data = requests.get(url=wangzhi,headers=headers).content
            meinv_path = 'meinv/' + meinv_name
            with open(meinv_path,'wb') as fp:
                fp.write(meinv_data)
                print(meinv_name,'下载成功！! !')
    
    if num > 1:
        for i in range(1,num):
            url_next = 'https://pic.netbian.com/4kmeinv/index_' + str(num) + '.html'
            response = requests.get(url=url_next,headers=headers)
            response.encoding = 'gbk'
            page_text = response.text
            tree = etree.HTML(page_text)
            li_list = tree.xpath('/html/body/div[@class="wrap clearfix"]//li')
            for i in li_list:
                wangzhi = 'https://pic.netbian.com' + i.xpath('./a/img/@src')[0]
                meinv_name = i.xpath('./a/img/@alt')[0] + '.jpg'
                meinv_data = requests.get(url=wangzhi,headers=headers).content
                meinv_path = 'meinv/' + meinv_name
                with open(meinv_path,'wb') as fp:
                    fp.write(meinv_data)
                    print(meinv_name,'下载成功！! !')
            